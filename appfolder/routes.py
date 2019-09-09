from demoapp import app

@app.route('/')
@app.route('/index')
def index():
    return "in indexfunction."