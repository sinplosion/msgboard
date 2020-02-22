from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.comment.models import Comment
from application.comment.forms import CommentForm
from application.auth.models import User


@app.route("/comment", methods=["GET"])
def comment_index():
    return render_template("comment/list.html", comment=Comment.query.all())

@app.route("/comment/new/")
@login_required
def comment_form():
    return render_template("comment/new.html", form = CommentForm())

@app.route("/comment/", methods=["POST"])
@login_required
def comment_create(thread_id):

    form = CommentForm(request.form)

    if not form.validate():
        return render_template("comment/new.html", form = form)

    c = Comment(content=form.comment.data)
    c.thread_id = thread_id
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("comment_index"))


@app.route("/comment/delete/<comment_id>/", methods=["POST"])
@login_required
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)

    db.session().delete(comment)
    db.session().commit()

    return redirect(url_for("comment_index"))

@app.route("/comment/edit/<comment_id>", methods=["POST"])
@login_required
def comment_edit(comment_id):
    form = CommentForm(request.form)
    comment = Comment.query.get(comment_id)

    if not form.validate():
        return render_template("comment/edit.html", id=comment_id, form=form)

    Comment.query.filter_by(id=comment_id).update(
        dict(content=form.comment.data))

    db.session.commit()

    return redirect(url_for("comment_index"))
