# Implementation Plan for Flask IAM Lab

## Information Gathered:

- **Project structure**: Flask API with React frontend
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: bcrypt for password hashing, Flask sessions for auth state
- **Test files**: Located in `server/testing/` for models and app routes

## Plan:

### Step 1: Update `models.py` ⬅️ IN PROGRESS

- [ ] User Model with id, username, \_password_hash, image_url, bio
- [ ] Password hash property with bcrypt encryption
- [ ] User authentication method
- [ ] Unique username constraint
- [ ] User-Recipe relationship
- [ ] Recipe Model with id, title, instructions (50+ chars), minutes_to_complete, user_id

### Step 2: Run Migrations

- [ ] Initialize flask db
- [ ] Generate and run migrations

### Step 3: Implement Routes in `app.py`

- [ ] Signup Resource (POST /signup)
- [ ] CheckSession Resource (GET /check_session)
- [ ] Login Resource (POST /login)
- [ ] Logout Resource (DELETE /logout)
- [ ] RecipeIndex Resource (GET/POST /recipes)

### Step 4: Run Tests

- [ ] Run model tests
- [ ] Run app tests

## Dependent Files to be Edited:

1. `/home/calton/Development/code/phase4/labs/python-p4-iam-putting-it-all-together-lab/server/models.py`
2. `/home/calton/Development/code/phase4/labs/python-p4-iam-putting-it-all-together-lab/server/app.py`

## Followup Steps:

1. Initialize and run migrations
2. Test model tests pass
3. Test app tests pass
4. Optionally seed database with `python seed.py`
