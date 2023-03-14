"""test"""
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    """fonction index"""
    print('Request for index page received')
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    """favicon"""
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/hello', methods=['POST'])
def hello():
    """helloooooooo"""
    name = request.form.get('name')

    if name:
        print(f"Request for hello page received with name={name}")
        return render_template('hello.html', name=name)
    print('Request for hello page received with no name or blank name -- redirecting')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
