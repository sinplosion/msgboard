from flask_wtf import FlaskForm
from wtforms import StringField, validators,TextAreaField

class ThreadForm(FlaskForm):
    title = StringField("Title:", [validators.Length(min=3,max=8192,message="Comment has to be between 3 to 8192 characters long.")])
    content = TextAreaField("Content: ", [validators.Length(min=3,max=8192,message="Comment has to be between 3 to 8192 characters long.")])
 
    class Meta:
        csrf = False
