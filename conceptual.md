### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Javascript uses semicolons to designate different lines, Python uses indentation

  Python is more explicit & strongly typed than Javascript. It will show more errors rahter than making assumptions about the code so it can move forward.

  Python is an object oriented programming language, while JS is a scripting language (though JS can be written to be more object oriented)

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  1. dict.get("c")
  2. dict.setdefault("c",default_value)

* What is a unit test?
  A unit test is the most basic level of testing. Simply if a function or component does what it is supposed to do

* What is an integration test?
  An integration test checks if the parts/units work together without unintended effects

* What is the role of web application framework, like Flask?
  A web application framework starts a server that listens for requests and helps determine how to respond to which requests

* You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  A route URL might be a more dedicated page, like a product page built to offer more details about the item in question
  A URL query param is usually the result of a search or sort/filter action.

* How do you collect data from a URL placeholder parameter using Flask?
  In the route, designate the placeholder with <>, ex <color>
  Then you can refer to it, ex color

* How do you collect data from the query string using Flask?
  from flask import request
  data = request.args["key"]

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?
  Cookies store information on the client (browser). They are commonly used for remembering preferences and whether you're logged in or not.

- What is the session object in Flask?
  the session object is Flask's way to handle cookies. It is client and server readable and it is signed so a user can't just change or read the cookie information. The session object is accessed/stored like a dictionary object with keys and values.

- What does Flask's `jsonify()` do?
  jsonify() turns responses into JSON to be sent

- What was the hardest part of this past week for you?
  It was hard to put everything together and keep things straight. Mixing Javascript and Python together as well as testing it was tough
  What was the most interesting?
  It was really interesting to learn Python & Flask as an alternative to Javascript
