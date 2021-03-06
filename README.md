java-api-search
===============

This is a simple API search tool implemented in pure HTML and JavaScript
that lets you search for API elements (classes, interfaces, enums, and
annotations). All data is kept in a simple JSON file that you create for
the APIs you choose using the accompanying Python script. See the
[demo site](http://tools.mafr.de/java-api-search/) for an example of how
this looks.

Run the Python script create-json-db.py to download API elements for a number
of public Java libraries and create a JSON object from it. Example:

    $ ./create-api-index.py > htdocs/api-index.js

Publish the JSON object on a web server together with the HTML and JavaScript
content and load the index.html from your browser. The RETURN key takes you
to the first hit, TAB lets you select the other hits. All results open in a
new browser window.

For testing purposes you can serve the htdocs directory locally:

    $ cd htdocs
    $ python3 -m http.server

Point your browser to [http://localhost:8000/](http://localhost:8000/) and
give it a try.
