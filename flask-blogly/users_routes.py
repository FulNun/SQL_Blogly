from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import db, User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def show_users():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)

@users_bp.route('/new', methods=['GET'])
def show_add_user_form():
    return render_template('users/new.html')

@users_bp.route('/new', methods=['POST'])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    if not first_name or not last_name:
        flash('First name and last name are required.', 'error')
        return redirect(url_for('users.show_add_user_form'))

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    flash('User added successfully!', 'success')
    return redirect(url_for('users.show_users'))

@users_bp.route('/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@users_bp.route('/<int:user_id>/edit', methods=['GET'])
def show_edit_user_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@users_bp.route('/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.commit()
    flash('User updated successfully!', 'success')
    return redirect(url_for('users.show_users'))

@users_bp.route('/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('users.show_users'))
