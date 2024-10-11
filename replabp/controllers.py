from flask import Blueprint, render_template, request
from models import users_lista

controller_blueprint = Blueprint('login', __name__)

@controller_blueprint.route('/')
def index():
    return render_template('index.html')

@controller_blueprint.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('index.html')

