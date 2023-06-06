from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    IntegerField,
    DateField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Email, ValidationError, Length
from datetime import date

from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.AWS_helpers import ALLOWED_EXTENSIONS

# removed for testing
def date_checker(form, field):
    form_date = field.data
    if form_date < date.today():
        raise ValidationError("Please provide a valid date that is after today's date.")


class ProjectForm(FlaskForm):
    project_name = StringField("Project Name", validators=[DataRequired()])
    description = TextAreaField(
        "Project Name",
        validators=[
            DataRequired()
        ],
    )
    category_id = IntegerField("Category ID", validators=[DataRequired()])
    # category = SelectField("Category", choices=choices, validators=[DataRequired()])
    money_goal = IntegerField(
        "Money Goal",
        validators=[
            DataRequired()
        ],
    )
    city = StringField("City", validators=[DataRequired()])
    state = StringField(
        "State",
        validators=[
            DataRequired()
        ],
    )
    story = TextAreaField(
        "Story",
        validators=[
            DataRequired()
            # Length(min=200, message="Story must be at least 200 characters."),
        ],
    )
    project_image = FileField(
        "Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))]
    )
    # project_image = FileField("Image File")
    end_date = DateField("End Date", validators=[DataRequired()])
    reward_name = StringField("Reward Name", validators=[DataRequired()])
    reward_amount = IntegerField("Reward Amount", validators=[DataRequired()])
    reward_description = TextAreaField(
        "Reward Description", validators=[DataRequired()]
    )
