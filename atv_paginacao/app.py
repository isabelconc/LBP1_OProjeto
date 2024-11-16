from flask import Flask
from controllers.controller import produtosController

app = Flask(__name__)
app.register_blueprint(produtosController)

if __name__ == '__main__':
    app.run(debug=True)