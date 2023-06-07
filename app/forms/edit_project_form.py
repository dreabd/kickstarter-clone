from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    IntegerField,
    DateField,
    TextAreaField,
)
from wtforms.validators import DataRequired, ValidationError, Length
from datetime import date

from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.AWS_helpers import ALLOWED_EXTENSIONS


def date_checker(form, field):
    form_date = field.data
    if form_date < date.today():
        raise ValidationError("Please provide a valid date that is after today's date.")


class EditForm(FlaskForm):
    project_name = StringField("Project Name", validators=[DataRequired()])
    description = TextAreaField(
        "Project Name",
        validators=[
            DataRequired(),
        ],
    )
    category_id = IntegerField("Category ID", validators=[DataRequired()])
    money_goal = IntegerField(
        "Money Goal",
        validators=[DataRequired()],
    )
    city = StringField("City", validators=[DataRequired()])
    state = StringField(
        "State",
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=2,
                message="Please use the state's two character abbreviation.",
            ),
        ],
    )
    story = TextAreaField(
        "Story",
        validators=[DataRequired()],
    )
    project_image = FileField(
        "Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))]
    )
    end_date = DateField("End Date", validators=[DataRequired(), date_checker])
    reward_name = StringField("Reward Name", validators=[DataRequired()])
    reward_amount = IntegerField("Reward Amount", validators=[DataRequired()])
    reward_description = TextAreaField(
        "Reward Description", validators=[DataRequired()]
    )
