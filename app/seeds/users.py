from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        first_name = "Demo",
        last_name = "User",
        bio = "Demo is an innovative startup revolutionizing the world of product trials. Founded in 2022, Demo connects consumers with a diverse range of companies offering exclusive trial experiences for their latest products. By seamlessly bridging the gap between businesses and potential customers, Demo is reshaping the way people discover, experience, and provide feedback on cutting-edge innovations.",
        username='Demo',
        email='demo@aa.io',
        password='password',
        city = "Tacoma",
        state = "WA"
        )
    marnie = User(
        first_name = "Mary",
        last_name = "Nguyen",
        bio = "Marnie, a visionary illustrator with an unmatched flair for storytelling, is on a mission to bring her imaginative creations to life through Kickstarter. With a portfolio brimming with whimsy and wonder, Marnie captivates audiences with her unique blend of vibrant colors and intricate details. Back Marnie's Kickstarter campaign to embark on a visual journey filled with enchanting characters, captivating narratives, and the magic of art.",
        username='marnie',
        email='marnie@aa.io',
        password='password',
        city = "Albany",
        state = "NY"
        )
    bobbie = User(
        first_name = "Robert",
        last_name = "Smith",
        bio = "Bobbie, a visionary creator at the intersection of technology and design, is launching an exciting Kickstarter campaign to bring his innovative products to the world. With an unwavering commitment to both functionality and aesthetics, Bobbie's designs seamlessly integrate cutting-edge technology into sleek and intuitive devices. Join Bobbie's Kickstarter journey to support the birth of groundbreaking tech products that elevate the user experience and redefine what's possible in the realm of design and technology.",
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        city = "Chicago",
        state = "IL"
        )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
