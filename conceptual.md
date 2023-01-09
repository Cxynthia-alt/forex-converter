### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  **python is object-oriented programming language that can be used for back-end development such as the server side of an application. Javascript is a scripting language that can be used to both front and back end. In front-end,we can use js to interact with users.**
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  ``my_dict.get('c', 0)``
- What is a unit test?
  **a test for a speific function with a piece of code in isolation from all the functions**
- What is an integration test?
  **a test to see if multiple functions work together**
- What is the role of web application framework, like Flask?
  **Web frameworks is a collection of libraries and modules that offers a way to create and run web applications. Flask, for example, is a back-end framework written in python. Guidelines for different files types working together**
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=hydrate'). How might you choose which one is a better fit
  for an application?
  **URL parameter: When you have a specific resource from the back-end. Returned everything from pretzel**
  **Using a query param: return everything that has the "hydrate" as their type**
  **query param: filter through and return multuple resources. Returned **
- How do you collect data from a URL placeholder parameter using Flask?
  **URL placeholder parameter example:**
  ```python
  @app.route("/products/<category>/<int:product_id>")
  def product_detail(category, product_id):
    return f"{category}  and {product_id}"
  ```
  **We can collect data by adding variables to functions as arguments and wrap up the variables with {}**
- How do you collect data from the query string using Flask?
  **Query string example through a GET request:**
  ```python
  @app.route("/shop/<toy>")
  def toy_detail(toy):
    color_1=request.args.get("color_1")
    #or
    color_2=request.args["color_2"]
  ```
  **We can use**
- How do you collect data from the body of the request using Flask?

  **When send a POST request, the body is an object.**
  **If it's through AJAX: request.json['key]**
  **It through a form: request.form['key']**
- What is a cookie and what kinds of things are they commonly used for?
  **A cookie is a key-value pair stored by browser. They are used to store the data from HTTP requests. Use to save info from the website that could be use for future/track user data**
- What is the session object in Flask?
  **It is a dictionary used to store data for current browser and cannot be modified/read by user.**
- What does Flask's `jsonify()` do?
  **It returns the data as JSON format as an HTTP response so it can be used in js file**
