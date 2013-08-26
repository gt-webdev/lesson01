from bottle import route, run

@route('/')
@route('/hello')
def index():
  return 'hello world'

@route('/bye')
@route('/goodbye')
def index():
  return 'goodbye world'

run(host='localhost', port=8080)
