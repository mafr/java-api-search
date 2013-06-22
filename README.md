java-api-search
===============

This is a simple API search tool implemented in pure HTML and JavaScript
that lets you search for API elements (classes, interfaces, enums, and
annotations). All data is kept in a simple JSON file that you create for
the APIs you choose using the accompanying Python script.

Run the Python script create-json-db.py to download API elements for a number
of public Java libraries and create a JSON object from it.

Publish the JSON object on a web server along the HTML and JavaScript
content and load the index.html from your browser.
