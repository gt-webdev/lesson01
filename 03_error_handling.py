from bottle import route, run, error, abort


@route('/')
def index():
  return 'this page works'


@route('/waldo')
def whereishe():
  abort(404)


@route('/mchammer')
def can_u_touch_this():
  abort(401)  # U are unauthorized to touch this


@error(401)
def cannot_be_touched(error):
  return "U can't touch this!"


@error(404)
def four0four(error):
  return "these are not the droids you are looking for"


run(host='localhost', port=8080)
