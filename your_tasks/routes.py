from flask import Blueprint, render_template, redirect, session


main = Blueprint('main', __name__)


@main.route('/')
def home():
    if 'logged_in' in session:
        return redirect('/dashboard/')
    else:
        return render_template('home.html')


@main.route('/dashboard/')
def dashboard():
    if 'logged_in' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')


@main.route('/update_user/')
def update_user():
    if 'logged_in' in session:
        return render_template('update_user.html')
    else:
        return redirect('/')


@main.route('/reset/')
def reset():
    if 'logged_in' in session:
        return redirect('/dashboard/')
    else:
        return render_template('reset.html')
