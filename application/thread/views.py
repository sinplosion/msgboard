from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.thread.models import Thread
from application.thread.forms import ThreadForm
from application.auth.models import User
from application.comment.forms import CommentForm


@app.route("/thread/new/")
@login_required
def thread_form():
    return render_template("thread/new.html", form = ThreadForm())

@app.route("/thread/", methods=["POST"])
@login_required
def thread_create():

    threadform = ThreadForm(request.form)

    if not threadform.validate():
        return render_template("thread/new.html", form = threadform)

    t = Thread(title=threadform.title.data, content=threadform.content.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("thread_index"))

@app.route("/thread", methods=["GET"])
def thread_index():
    return render_template("thread/list.html", thread=Thread.query.all())

@app.route("/thread/show/<thread_id>", methods=["GET","POST"])
@login_required
def thread_show(thread_id):
    form = CommentForm(request.form)
    thread = Thread.query.get(thread_id)

    return render_template("thread/show.html", form = form, thread = thread)


