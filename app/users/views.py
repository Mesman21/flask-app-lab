from flask import request, redirect, url_for, render_template, session, flash, make_response
from . import users_bp

VALID_USERNAME = 'user1'
VALID_PASSWORD = 'password123'


# --- МАРШРУТИ ЛАБ 3 (Blueprint users) ---

@users_bp.route("/hi/<string:name>")
def greetings(name):
    # Змінено шаблон на hi.html
    age = request.args.get("age", "Unknown")
    return render_template("users/hi.html", name=name.upper(), age=age)


@users_bp.route("/admin")
def admin():
    return redirect(url_for('users.greetings', name='Administrator', age=45))


# --- МАРШРУТИ ЛАБ 4 (Login, Profile, Logout) ---

@users_bp.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('users.profile'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['username'] = username
            flash(f'Ласкаво просимо, {username}!', 'success')
            return redirect(url_for('users.profile'))
        else:
            flash('Неправильні дані. Спробуйте ще раз.', 'danger')
            return redirect(url_for('users.login'))

    return render_template('users/login.html')


@users_bp.route("/profile", methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        flash('Для доступу до профілю необхідно увійти.', 'warning')
        return redirect(url_for('users.login'))

    username = session['username']
    all_cookies = request.cookies.items()

    return render_template('users/profile.html', username=username, all_cookies=all_cookies)


@users_bp.route("/logout")
def logout():
    session.pop('username', None)
    flash('Ви успішно вийшли з системи.', 'info')
    return redirect(url_for('users.login'))


# --- МАРШРУТИ ЛАБ 4 (Кукі та Теми) ---

@users_bp.route("/cookies", methods=['POST'])
def handle_cookies():
    if 'username' not in session:
        flash('Необхідно увійти для керування кукі.', 'danger')
        return redirect(url_for('users.login'))

    action = request.form.get('action')

    if action == 'add':
        key = request.form.get('key')
        value = request.form.get('value')

        response = make_response(redirect(url_for('users.profile')))
        response.set_cookie(key, value, max_age=60 * 60 * 24 * 7)
        flash(f'Кукі "{key}" успішно додано.', 'success')
        return response

    elif action == 'delete_key':
        key = request.form.get('delete_key_name')
        response = make_response(redirect(url_for('users.profile')))
        response.delete_cookie(key)
        flash(f'Кукі "{key}" успішно видалено.', 'warning')
        return response

    elif action == 'delete_all':
        response = make_response(redirect(url_for('users.profile')))

        for key in request.cookies:
            response.delete_cookie(key)

        flash('Усі кукі успішно видалено.', 'warning')
        return response

    return redirect(url_for('users.profile'))


@users_bp.route("/theme/<string:theme_name>")
def select_theme(theme_name):
    if theme_name in ['light', 'dark']:
        response = make_response(redirect(url_for('users.profile')))
        response.set_cookie('theme', theme_name, max_age=60 * 60 * 24 * 365)
        flash(f'Тему змінено на {theme_name}.', 'info')
        return response

    flash('Невідома тема.', 'danger')
    return redirect(url_for('users.profile'))