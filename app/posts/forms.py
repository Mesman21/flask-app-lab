from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=150)])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('news', 'News'),
        ('publication', 'Publication'),
        ('tech', 'Tech'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save')