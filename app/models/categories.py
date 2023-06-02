from .db import db, environment, SCHEMA, add_prefix_for_prod

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50),nullable=False,unique=True)

    project = db.relationship("Project",back_populates="category")

    def to_dict(self):
        return{
            "id":self.id,
            "type":self.type,
            }
