from app.models import db, environment, SCHEMA, Funding
from sqlalchemy.sql import text
from datetime import date
from random import choice, randint


def seed_fundings():
    funding_list = []
    for i in range(0, 10000):
        funding_seed = Funding(
            user_id=choice([1, 2, 3, 12, 13, 14]),
            project_id=randint(1, 95),
            amount_donated=randint(1, 200),
            reward=False,
        )
        funding_list.append(funding_seed)

    [db.session.add(funding) for funding in funding_list]
    db.session.commit()


def undo_fundings():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.fundings RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM fundings"))

    db.session.commit()
