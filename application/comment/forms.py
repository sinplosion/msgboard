from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CommentForm(FlaskForm):
    comment = StringField("Comment", [validators.Length(min=3,max=8192,message="Comment has to be between 3 to 8192 characters long.")])
 
    class Meta:
        csrf = False
