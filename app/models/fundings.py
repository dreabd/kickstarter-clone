from .db import db, environment, SCHEMA, add_prefix_for_prod


class Funding(db.Model):
    __tablename__ = 'funding'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('projects.id')), nullable=False)
    amount_donated = db.Column(db.Integer, nullable=False)
    reward = db.Column(db.Boolean,nullable=False)

    user = db.relationship('User', back_populates='funding')
    project = db.relationship('Project', back_populates='funding')

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user_id,
            'project_id': self.project_id,
            'amount_donated': self.amount_donated
        }
