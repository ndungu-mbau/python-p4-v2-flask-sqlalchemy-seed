#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet

from faker import Faker
from random import choice as rc

fake = Faker()

with app.app_context():
    Pet.query.delete()

    # Species Types
    species = ["cat", "dog", "hamster", "snake"]
    # Create an empty list
    pets = []

    # Add some Pet instances to the list
    for _ in range(10):
        pets.append(Pet(name=fake.first_name(), species=rc(species)))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()
