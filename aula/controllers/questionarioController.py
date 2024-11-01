from flask import Blueprint, render_template, request, redirect, url_for, session

questionarioController = Blueprint("questoes", __name__) # "questoes" é o primeiro parâmetro do Blueprint (nome do Blueprint), __name__ é o segundo (nome)

@questionarioController.route('/')
def index():
    return render_template('index.html')

@questionarioController.route('/verifica', methods = ["POST"])
def verifica():
    nome = request.form.get("nome") # request.form["nome"] tb funciona
    email = request.form.get("email")
    if email.split("@")[1] == "aluno.ifsp.edu.br": # split pega a parte depois do @, [1] indica o índice da parte depois do @
        session["email"] = email # variável onde o request.form["email"] está
        session["nome"] = nome 
        return redirect(url_for("questoes.questionario")) # depois do nome do Blueprint, segue o nome da FUNÇÃO (não da rota)
    return "Email inválido. Por favor, entre com seu email institucional."

@questionarioController.route('/questionario')
def questionario():
    return render_template("questionario.html")

@questionarioController.route('/logout')
def logout():
   session.pop("email", None) # troca "email" por "nada"
   session.pop("nome", None)
   return redirect(url_for("questoes.index"))