from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ThreadForm(FlaskForm):
    title = StringField("Title: ", [validators.Length(min=3,max=128,message="Title has to be between 3 to 128 characters long.")])
 
    class Meta:
        csrf = False
