from flask_wtf import FlaskForm
from wtforms.fields import (
     StringField, SubmitField
)
from wtforms.validators import DataRequired, URL

class GroupForm(FlaskForm):
    name = StringField("Servers", validators=[DataRequired()])
    image_url = StringField('Group Image', URL(require_tld=False, message='Must be Url'))
    submit = SubmitField("Create Group")
