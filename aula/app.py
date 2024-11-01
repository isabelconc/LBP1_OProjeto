from flask import Flask, redirect, request, session, url_for
from controllers.questionarioController import questionarioController

app = Flask(__name__)
app.secret_key = "chavinho" # a secret_key é necessária para fzr sessão

rotas_publicas = ["questoes.index", "questoes.verifica"] # indica quais rotas eu qro o middleware

@app.before_request
def verificaId():
    if request.endpoint in rotas_publicas: # .endpoint retorna qual função está sendo executada
        if "email" in session:
            return 
        return redirect(url_for("questoes.index")) # teste que antes era feito no controller

app.register_blueprint(questionarioController)


if __name__ == '__main__':
   app.run(debug=True)