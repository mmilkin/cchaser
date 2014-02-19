
# -*- coding: utf-8 -*-
"""
    An example of how to controls an RC Car with a raspberry pi
    :license: BSD, see LICENSE for more details.
"""
from flask.ext.login import login_required, current_user, login_user, logout_user
from flask import g, jsonify
from chaser.models import User
from controller import MotorInputError

from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from chaser import app, login_manager, motor_controller
from forms import LoginForm


@app.before_request
def load_users():
    if current_user and current_user.is_authenticated():
        g.user = current_user.get_id()
    else:
        g.user = None


@app.before_request
def load_global_user():
    g.user = current_user


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/state', methods=['GET'])
def state():
    result = {'state': motor_controller.state}
    return jsonify(result), 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        return redirect('/')
    return render_template(
        'login.html',
        title='Sign In',
        form=form,
    )


@app.route('/')
def control_app():
    return render_template(
        'control.html'
    )


@app.route('/control', methods=['POST'])
@login_required
def game_control():
    return _game_control()


def _game_control():
    key = request.form['key']
    app.logger.debug('game controller received key {0}'.format(key))
    try:
        motor_controller.motor(key)
    except MotorInputError:
        return jsonify({ "error": "Bad input {0}".format(key)}), 400
    return '', 200


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('control_app'))
