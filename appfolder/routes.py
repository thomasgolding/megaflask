from flask import render_template, redirect, flash, url_for
from appfolder import demoapp
from appfolder.forms import LoginForm

@demoapp.route('/')
@demoapp.route('/index')
def index():
    user = {'username': 'thomas'}
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign in", form=form)
