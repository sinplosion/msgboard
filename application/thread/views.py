from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.thread.models import Thread
from application.thread.forms import ThreadForm
from application.auth.models import User
from application.comment.forms import CommentForm
from application.comment.models import Comment
from application.thread import models
from application.comment import views


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
    return render_template("thread/list.html", listthreads=Thread.listAllThreads())

@app.route("/thread/show/<thread_id>", methods=["GET","POST"])
def thread_show(thread_id):
    form = CommentForm(request.form)
    thread = Thread.query.get(thread_id)

    return render_template("thread/show.html", form = form, thread = thread, threadinfo = Thread.threadsInfo(thread_id), comment = Comment.listComments(thread_id))


@app.route("/thread/comment/<thread_id>", methods=["POST"])
@login_required
def thread_comment(thread_id):
 
    form = CommentForm(request.form)

    if not form.validate():
        return redirect(url_for("thread_show", thread_id=thread_id, form = form))

    c = Comment(content=form.comment.data)
    c.thread_id = thread_id
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
  

    return redirect(url_for("thread_show", thread_id=thread_id))



@app.route("/thread/listComments/<thread_id>", methods=["GET"])
def thread_listcomments(thread_id):
    return render_template("thread/listComments.html", comment = Comment.listComments(thread_id))


@app.route("/thread/comment/delete/<comment_id>/", methods=["POST"])
@login_required
def thread_comment_delete(comment_id):
    comment = Comment.query.get(comment_id)
    db.session().delete(comment)
    db.session().commit()

    return redirect(url_for("thread_index"))

@app.route("/thread/comment/edit/<comment_id>", methods=["POST"])
@login_required
def thread_comment_edit(comment_id):
    form = CommentForm(request.form)
    comment = Comment.query.get(comment_id)
    
    if not form.validate():
        return render_template("thread/editComment.html", id=comment_id, form=form)
    
    Comment.query.filter_by(id=comment_id).update(
        dict(content=form.comment.data))

    db.session.commit()

    comment = Comment.query.get(comment_id)
    return redirect(url_for("thread_index"))

@app.route("/thread/edit/<thread_id>", methods=["POST"])
@login_required
def thread_edit(thread_id):
    form = ThreadForm(request.form)
    thread = Thread.query.get(thread_id)
    
    if not form.validate():
        return render_template("thread/editThread.html", id=thread_id, form=form)
    
    Thread.query.filter_by(id=thread_id).update(
        dict(content=form.content.data, title= form.title.data))

    db.session.commit()

    return redirect(url_for("thread_index"))

@app.route("/thread/delete/<thread_id>", methods=["POST"])
@login_required
def thread_delete(thread_id):
    thread = Thread.query.get(thread_id)
    Comment.deleteCommentsThread(thread_id)
    db.session().delete(thread)
    db.session().commit()

    return redirect(url_for("thread_index"))