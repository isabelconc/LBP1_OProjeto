from flask import Flask, render_template, request, session
from controllers import controller_blueprint

app = Flask(__name__)
app.register_blueprint(controller_blueprint)
app.secret_key = 'secret_key'  

if __name__ == '__main__':
    app.run(debug=True)
