### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
JS is not a pure OO programming language, whereas Python is. A function in JS is declared using the 'function' keyword, in Python, 'def' is used. Python uses indentation to define it's code blocks; JS uses curly braces. Python uses snake_case vs JS: lower camel case. None in Python vs null in JS. Tuple, like a list, but immutable exists as a built-in data structure in Python, but not JS.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  ??????

- What is a unit test?
A type of test used to determine whether individual units/components of code like functions perform as expected.

- What is an integration test?
Integration testing is a more complex type of software testing that is used to determine whether larger chunks/modules of software work together. 

- What is the role of web application framework, like Flask?
Designed to support the development of web applications including web services, and web APIs. Prevents you from having to manually handle every step of the process (receiving of HTTP requests, which port your server listens for requests on).

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
Path parameters are used to identify a specific resource/resources, whereas query params are used to sort/filter those resources. GET /cars/:id vs GET /cars?color=blue. Going to the cars page in general vs pulling blue cars specifically. 

- How do you collect data from a URL placeholder parameter using Flask?
request.args.get()

- How do you collect data from the query string using Flask?
request.query_string

- How do you collect data from the body of the request using Flask?
request.form

- What is a cookie and what kinds of things are they commonly used for?
Data stored on the client-side in the browser. Used to maintain a shopping cart, pages you viewed, etc.

- What is the session object in Flask?
A 'magic dictionary' that stores info specific to a user from one request to the next. They're 'signed', meaning the data can be stored on the client-side in such a way that it can't be tampered with unless the secret key is used. 

- What does Flask's `jsonify()` do?
Creates a response object with the given data serialized to JSON.
