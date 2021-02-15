from flask import Blueprint, render_template, redirect, session
from .helpers import login_required

main = Blueprint('main', __name__)


@main.route('/')
def home():
    if 'logged_in' in session:
        return redirect('/dashboard/')
    else:
        return render_template('home.html')


@main.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@main.route('/update_user/')
@login_required
def update_user():
    return render_template('update_user.html')
