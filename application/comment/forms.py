from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", [validators.Length(min=3,max=8192,message="Comment has to be between 3 to 8192 characters long.")])
 
    class Meta:
        csrf = False
