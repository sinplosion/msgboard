from application import app, db
from flask import redirect, render_template, request, url_for
from application.comment.models import Comment


@app.route("/comment", methods=["GET"])
def comment_index():
    return render_template("comment/list.html", comment = Comment.query.all())

@app.route("/comment/new/")
def comment_form():
    return render_template("comment/new.html")

@app.route("/comment/", methods=["POST"])
def comment_create():
    t = Comment(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("comment_index"))


@app.route("/comment/delete/<comment_id>/", methods=["POST"])
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)

    db.session().delete(comment)
    db.session().commit()

    return redirect(url_for("comment_index"))
