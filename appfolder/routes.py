from flask import render_template
from appfolder import demoapp

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
