from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    BooleanField
)
from wtforms.validators import DataRequired, Email, ValidationError, Length
from datetime import date


class FundingForm(FlaskForm):
    reward = BooleanField("Reward", validators=[DataRequired()])
    amount_donated = IntegerField("Amount Donated", validators=[DataRequired()])
    project_id = IntegerField("Project ID",validators=[DataRequired()])
