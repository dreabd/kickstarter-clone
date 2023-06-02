from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import date

class Project(db.Model):
    __tablename__ = "projects"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(255),nullable=False,unique=True)
    description = db.Column(db.String(255),nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"),nullable=False)
    money_goal = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    location = db.Column(db.String(255),nullable=False,)
    story = db.Column(db.String(10000),nullable=False)
    project_image = db.Column(db.String,nullable=False,)
    end_date = db.Column(db.Date,nullable=False)
    created_at = db.Column(db.Date,nullable=False,default=date.today())

    reward_name = db.Column(db.String(255))
    reward_amount = db.Column(db.Integer)
    reward_description = db.Column(db.String(2000))

    category = db.relationship("Category",back_populates="project")
    funding = db.relationship("Funding",back_populates="project")

    def to_dict(self):
      return{
          "id":self.id,
          "project_name":self.project_name,
          "description":self.description,
          "category_id":self.category_id,
          "money_goal":self.money_goal,
          "user_id":self.user_id,
          "location":self.location,
          "story":self.story,
          "project_image":self.project_image,
          "end_date":self.end_date,
          "created_at":self.created_at,
          "reward_name":self.reward_name,
          "reward_amount":self.reward_amount,
          "reward_description":self.reward_description,
      }
