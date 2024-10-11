# controllers.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import check_login, register_user

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
def index():
    # Verifica se o usuário está logado
    if 'user' in session:
        flash(f'Bem-vindo de volta, {session["user"]}!', 'success')
    return render_template('index.html')

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_login(username, password):
            session['user'] = username
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('login.index'))
        else:
            flash('Usuário ou senha inválidos', 'danger')

    return render_template('login.html')

@login_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if register_user(username, password):
            flash('Cadastro realizado com sucesso! Faça login para continuar.', 'success')
            return redirect(url_for('login.login'))
        else:
            flash('Usuário já existe!', 'danger')

    return render_template('register.html')

@login_blueprint.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('login.index'))
