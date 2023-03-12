### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
- python is a language that deals more with the back end of an app where as javascript is more frontend ui interaction

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
- dict.get('c', 3) and dict.items()

- What is a unit test?
- a unit test is a segment of code that test another peice of code usually a function.

- What is an integration test?
- instead of test one peice of code you are testing multiple parts at once.

- What is the role of web application framework, like Flask?
- web frameworks help developers build and deploy web apps.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
- when a parameter is in the route it is usually used when it is the subject of a page
  and when it is a query param it is better used when it is extra info about a page

- How do you collect data from a URL placeholder parameter using Flask?
- @app.route('/route/<placeholder>')

- How do you collect data from the query string using Flask?
- query = request.args.get('q')

- How do you collect data from the body of the request using Flask?
- data = request.json

- What is a cookie and what kinds of things are they commonly used for?
- a cookie is a little bit of information saved to the site. an example is when online shopping the website knows whats in your shooping cart because the info is saved as a cookie

- What is the session object in Flask?
- The session object in Flask is a built-in data structure that allows you to store data across multiple requests.

- What does Flask's `jsonify()` do?
- it turns regular data types into json so it can be passed through requests
