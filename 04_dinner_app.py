from bottle import route, run, error, redirect, abort
from random import choice

# simple list of things we can eat for dinner
dinner_items = ['pizza', 'burgers', 'pancakes']
pizza_counter = 0


@route('/')
def index():
  """The index page will pick a random dinner item and "suggest" it"""
  global pizza_counter
  dinner = choice(dinner_items)
  if dinner == 'pizza':
    pizza_counter += 1
    if pizza_counter > 5:
      abort(401, "I can't let you eat all that pizza")
  return dinner + ", that's what's for dinner!"


@route('/add/<new_item>')
def add_item(new_item):
  """accessing '/<new_item>' will create that item if it doesn't exist"""
  if new_item not in dinner_items:
    dinner_items.append(new_item)
    redirect('/')


@error(401)
def too_much_pizza(error):
  return "too much pizza!"

run(host='localhost', port=8080)
