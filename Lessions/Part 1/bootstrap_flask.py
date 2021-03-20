from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/user/<name>')
def bstest(name):
    return render_template('bs_templates/user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('bs_templates/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('bs_templates/500.html'), 500


@app.route('/intserverr')
def intserverr():
    a = 5 / 0
    return 'it wont be printed'


@app.route('/')
def index():
    return render_template('bs_templates/somelink.html', info=url_for('bstest', name='John', _external=True))


if __name__ == '__main__':
    app.run()
