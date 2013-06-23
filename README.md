java-api-search
===============

This is a simple API search tool implemented in pure HTML and JavaScript
that lets you search for API elements (classes, interfaces, enums, and
annotations). All data is kept in a simple JSON file that you create for
the APIs you choose using the accompanying Python script. 

Run the Python script create-json-db.py to download API elements for a number
of public Java libraries and create a JSON object from it. Example:

  $ ./create-api-index.py > htdocs/api-index.js

Publish the JSON object on a web server together with the HTML and JavaScript
content and load the index.html from your browser.

For testing purposes you can serve the htdocs directory locally:

  $ cd htdocs
  $ python3 -m http.server

Point your browser to http://localhost:8000/ and give it a try.
