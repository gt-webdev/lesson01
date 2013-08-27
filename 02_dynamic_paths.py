from bottle import route, run


@route('/')
def index():
  return 'hello world'


@route('/subjects/<sub_name>')
def subjects(sub_name):
  return "here's a page about " + sub_name


@route('/groups/<group_name>/permalink/<post_id>')
def show_post(group_name, post_id):
  if group_name == 'cs.gatech':
    if post_id == '42':
      return "This is the content of the 42nd post in cs.gatech"
  #if the group or post was incorrect, we show this error message
  return "I couldn't find the post you were looking for"


# wildcards conflicting with static route
@route('/wildcard/<text>')
def show_text(text):
  return text


@route('/wildcard/hammer')
def show_hammer():
  return "A Hammer, this is."

# spoiler: both routes work, bottle handles request by first checking for
# an exact match, before it allows wildcards to be selected

run(host='localhost', port=8080)
