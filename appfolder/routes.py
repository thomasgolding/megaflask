from appfolder import demoapp

@demoapp.route('/')
@demoapp.route('/index')
def index():
    return "in indexfunction."