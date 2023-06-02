from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.categories import Category


def seed_categories():
    arts = Category(
        type = "Arts")
    comic_illustration = Category(
        type = "Comics & Illustration")
    design_tech = Category(
        type = "Design & Tech")
    film = Category(
        type = "Film")
    food_craft = Category(
        type = "Food & Craft")
    games = Category(
        type = "Games")
    music = Category(
        type = "Music")
    publishing = Category(
        type = "Publishing")

    db.session.add(arts)
    db.session.add(comic_illustration)
    db.session.add(design_tech)
    db.session.add(film)
    db.session.add(food_craft)
    db.session.add(games)
    db.session.add(music)
    db.session.add(publishing)
    db.session.commit()


def undo_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM categories"))

    db.session.commit()
