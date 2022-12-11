from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.html5 import URLField

class GroupForm(FlaskForm):
    name = StringField("Servers", [DataRequired()])
    image_url = URLField('Group Image')
    submit = SubmitField("Create Group")
