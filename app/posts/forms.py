from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from app.users.models import User
from app.posts.models import Tag


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=150)])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('news', 'News'),
        ('publication', 'Publication'),
        ('tech', 'Tech'),
        ('other', 'Other')
    ], validators=[DataRequired()])

    author_id = SelectField('Author', coerce=int, validators=[DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)

    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.author_id.choices = [(u.id, u.username) for u in User.query.order_by('username')]
        self.tags.choices = [(t.id, t.name) for t in Tag.query.order_by('name')]