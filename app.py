# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, send_file, abort, send_from_directory
app = Flask(__name__)
app.debug = True

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', type="image/x-icon")

@app.route('/')
@app.route('/<path:path>')
def dir_viewer(path='./html'):

    return render_template("hello.html", entries=os.scandir(path)).encode('UTF-8')

@app.route("/download/<path:path>")
def download(path):
    return send_file(path)
if __name__ == '__main__':
    app.run(host='192.168.15.164', port='5010')

#192.168.15.164