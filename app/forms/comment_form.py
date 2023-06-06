from flask_wtf import FlaskForm
from wtforms import (
    TextAreaField,
    IntegerField,
)
from wtforms.validators import DataRequired, Email, ValidationError, Length
from datetime import date


class CommentForm(FlaskForm):
    user_id = IntegerField("userId", validators=[DataRequired()])
    project_id = IntegerField("projectId", validators=[DataRequired()])
    comment = TextAreaField("comment", validators=[DataRequired()])
