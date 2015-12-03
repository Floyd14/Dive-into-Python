import webbrowser
import os

absolute_path = "./HTML - Loc/index.html"

webbrowser.open('file://' + os.path.realpath(absolute_path))

# webbrowser.open_new("http://www.python.org")
