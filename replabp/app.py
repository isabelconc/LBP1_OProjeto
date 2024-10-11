from flask import Flask
from controllers import login_blueprint

app = Flask(__name__)
app.secret_key = 'secret_key'  # Necessário para sessões

# Registra o blueprint de login e cadastro
app.register_blueprint(login_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
