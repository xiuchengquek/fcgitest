__author__ = 'quek'

#!/usr/bin/env python
from cgi import FieldStorage
from flup.server.fcgi import WSGIServer



def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    form = FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=1)
    if 'name' in form:
        yield '<p>Hello %s</p>' % form['name'].value
        yield '<form name=\"name\" action=\"\" method=\"post\">\n' \
          '<p>Enter your name: <input type="text" name="name" value="">' \
          '<input type="submit" value="Submit"></p></form>\n'


if __name__ == '__main__':
    WSGIServer(app).run()