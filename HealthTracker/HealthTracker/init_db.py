# init_db.py

from main import db, app  # Adjust the import path based on your directory structure

from main import User, Stats  # Import your SQLAlchemy models

# Initialize the database
with app.app_context():
    # Create all tables
    db.create_all()
    print("Database tables created successfully.")
