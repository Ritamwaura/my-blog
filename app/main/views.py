from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PostForm,SubscriberForm,CommentForm
from ..import db,photos
from ..models import User,Post,Role,Subscriber,Comment
from flask_login import login_required,current_user
import markdown2
from ..email import mail_message
from ..request import get_quote

@main.route("/",methods=['GET','POST'])
def index():
    """
    View root page function that returns the index page and its data
    """
    posts = Post.query.all()
    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber=Subscriber(email=email)
        new_subscriber.save_subscriber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)

    title = "Welcome to Rita Blog"
    
    name  = "Quote"
    quote = get_quote()
    
    return render_template('index.html',title=title,posts=posts,subscriber_form=form,name=name,quote=quote)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
