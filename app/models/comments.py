from .db import db, environment, SCHEMA, add_prefix_for_prod


class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    user = db.relationship('User', back_populates='comments')
    project = db.relationship('Project', back_populates='comments')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'project_id': self.project_id,
            'comment': self.comment
        }
