from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.comment.models import Comment
from application.comment.forms import CommentForm
from application.auth.models import User
from application.thread import views

@app.route("/comment/delete/<comment_id>/", methods=["POST"])
@login_required
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)

    db.session().delete(comment)
    db.session().commit()

    return redirect(url_for("thread_index"))

@app.route("/comment/edit/<comment_id>", methods=["POST"])
@login_required
def comment_edit(comment_id):
    form = CommentForm(request.form)
    comment = Comment.query.get(comment_id)

    if not form.validate():
        return render_template("thread/editComment.html", id=comment_id, form=form)

    Comment.query.filter_by(id=comment_id).update(
        dict(content=form.comment.data))

    db.session.commit()

    return redirect(url_for("thread_index"))
