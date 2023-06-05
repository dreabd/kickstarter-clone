from flask_wtf import FlaskForm
from wtforms import StringField,TextField,SelectField,IntegerField,DateField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from datetime import date

from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.AWS_helpers import ALLOWED_EXTENSIONS

from app.models import Category

# category_choices = Category.query.all()
# choices = [category.type for category in category_choices]

def date_checker(form, field):
    form_date = field.data
    if form_date < date.today():
        raise ValidationError("Please provide a valid date that is after today's date.")

class ProjectForm(FlaskForm):
    project_name = StringField('Project Name',validators=[DataRequired()])
    description = TextField('Project Name',validators=[DataRequired(),Length(min=25,max=255,message="Description must be between 25 to 255 characters.")])
    category_id = IntegerField("Category ID", validators =[DataRequired()])
    # category = SelectField("Category", choices=choices, validators=[DataRequired()])
    money_goal = IntegerField("Money Goal", validators = [DataRequired(),])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired(),Length(min=2,max=2,message="Please use the state's two character abbreviation.")])
    story = TextField("Story",validators=[DataRequired(),Length(min=200,message="Story must be at least 200 characters.")])
    project_image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    end_date = DateField("End Date", validators=[DataRequired(),date_checker])
    reward_name = StringField('Reward Name', validators = [DataRequired()])
    reward_amount = IntegerField("Reward Amount", validators = [DataRequired()])
    reward_description = TextField("Reward Description", validators = [DataRequired()])
