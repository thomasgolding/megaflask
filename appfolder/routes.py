from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

from appfolder import demoapp, db
from appfolder.forms import LoginForm, RegistrationForm
from appfolder.models import User


@demoapp.route('/')
@demoapp.route('/index')
@login_required
def index():
    #user = {'username': 'thomas'}
    user = current_user
    posts = [
        {
            'author': {'username': 'kjell'},
            'body': 'the book animal farm by george orwell',
        },
        {
            'author': {'username': 'randi'},
            'body': 'considering a liberal vote next time...'
        }
    ]

    return render_template('index.html', 
        title='Title for the page', 
        user=user,
        posts=posts)


@demoapp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    ## this happens if the submitbutton is hit. 
    if form.validate_on_submit():
        
        ## get the user
        user = User.query.filter_by(username=form.username.data).first()
        
        ## check if user-pw does not exist
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        
        ## user-pw dows exist, so now the user is logged in.
        login_user(user, remember=form.remember_me.data)
        ## since we are using login_requested we are getting a potential argument in the url string:
        ## /login?next=/index. 
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        
        return redirect(next_page)

    return render_template('login.html', title="Sign in", form=form)

@demoapp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@demoapp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        redirect(url_for('index'))
    
    ## fill form
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username= form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("User created.")
        return redirect(url_for('login'))



    return render_template('register.html', title='Register', form=form)