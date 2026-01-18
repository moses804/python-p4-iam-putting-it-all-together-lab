from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    image_url = db.Column(db.String)
    bio = db.Column(db.String)

    # Relationship to Recipe (one-to-many)
    recipes = db.relationship('Recipe', backref='user', lazy=True)

    @hybrid_property
    def password_hash(self):
        # Raise AttributeError when attempting to access password_hash
        raise AttributeError("Password hashes cannot be accessed directly.")

    @password_hash.setter
    def password_hash(self, password):
        # Encrypt the password using bcrypt
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def authenticate(self, password):
        """Authenticate user with password. Returns True if password matches."""
        return bcrypt.check_password_hash(self._password_hash.encode('utf-8'), password)

    @validates('username')
    def validate_username(self, key, username):
        """Ensure username is present."""
        if not username:
            raise ValueError("Username is required.")
        return username

    def to_dict(self):
        """Return user data for JSON response."""
        return {
            'id': self.id,
            'username': self.username,
            'image_url': self.image_url,
            'bio': self.bio
        }

class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    minutes_to_complete = db.Column(db.Integer, nullable=False)

    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @validates('title')
    def validate_title(self, key, title):
        """Ensure title is present."""
        if not title:
            raise ValueError("Title is required.")
        return title

    @validates('instructions')
    def validate_instructions(self, key, instructions):
        """Ensure instructions are present and at least 50 characters long."""
        if not instructions:
            raise ValueError("Instructions are required.")
        if len(instructions) < 50:
            raise ValueError("Instructions must be at least 50 characters long.")
        return instructions

    def to_dict(self):
        """Return recipe data for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'instructions': self.instructions,
            'minutes_to_complete': self.minutes_to_complete,
            'user': self.user.to_dict() if self.user else None
        }

