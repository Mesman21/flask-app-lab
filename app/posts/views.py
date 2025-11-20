from flask import render_template, redirect, url_for, flash, request, abort
from . import post_bp
from .models import Post, Tag
from .forms import PostForm
from app import db


@post_bp.route('/post')
def all_posts():
    posts = db.session.query(Post).order_by(Post.posted.desc()).all()
    return render_template("posts/posts.html", posts=posts)


@post_bp.route('/post/<int:id>')
def post_detail(id):
    post = db.session.get(Post, id)
    if not post:
        abort(404)
    return render_template("posts/detail_post.html", post=post)


@post_bp.route('/post/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            user_id=form.author_id.data,
            is_active=form.is_active.data
        )

        selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()
        post.tags.extend(selected_tags)

        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('posts.all_posts'))

    return render_template("posts/add_post.html", form=form, legend="Create Post")


@post_bp.route('/post/<int:id>/update', methods=['GET', 'POST'])
def update_post(id):
    post = db.session.get(Post, id)
    if not post:
        abort(404)

    form = PostForm(obj=post)

    if request.method == 'GET':
        form.author_id.data = post.user_id
        form.tags.data = [tag.id for tag in post.tags]

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.user_id = form.author_id.data
        post.is_active = form.is_active.data

        post.tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()

        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('posts.post_detail', id=post.id))

    return render_template("posts/add_post.html", form=form, legend="Update Post")


@post_bp.route('/post/<int:id>/delete', methods=['POST', 'GET'])
def delete_post(id):
    post = db.session.get(Post, id)
    if not post:
        abort(404)

    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash('Post has been deleted!', 'success')
        return redirect(url_for('posts.all_posts'))

    return render_template("posts/delete_confirm.html", post=post)