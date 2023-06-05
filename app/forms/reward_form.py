from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextField
from wtforms.validators import DataRequired

class RewardForm(FlaskForm):
    reward_name = StringField('Reward Name', validators = [DataRequired()])
    reward_amount = IntegerField("Reward Amount", validators = [DataRequired()])
    reward_description = TextField("Reward Description", validators = [DataRequired()])


