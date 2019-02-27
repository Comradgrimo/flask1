# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, send_file, abort, send_from_directory,g
app = Flask(__name__)
app.debug = True

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', type="image/x-icon")

@app.route('/')
def hello():
    return render_template("hello.html")

@app.route('/graph')
def graph(path='./graph'):
    return render_template("graph.html", entries=list(os.scandir(path))).encode('UTF-8')

@app.route("/download/<path:path>")
def download(path):
    return send_file(path)

# @app.route('/january')
# def january(path='./html/2019/january'):
#     return render_template("january.html", entries=list(os.scandir(path))).encode('UTF-8')

@app.route('/<month>')
def year(month):
    month1 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
             'november', 'december']
    if month in month1:
        return render_template("january.html", entries=list(os.scandir("./html/2019/"+ month)), name_month = month)
    else:
        return render_template('404.html')

@app.errorhandler(404)
def error500(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='192.168.15.164', port='5010')

#192.168.0.13
