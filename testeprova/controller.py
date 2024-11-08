from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask import make_response
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessário para usar sessões

@app.route('/')
def index():
    if 'tasks' not in session:
        session['tasks'] = []
    return render_template('index.html', tasks=session['tasks'])

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    
    if not title or not description:
        flash('Título e descrição são obrigatórios!', 'error')
        return redirect(url_for('index'))

    task = {
        'title': title,
        'description': description,
        'due_date': due_date
    }
    session['tasks'].append(task)
    flash('Tarefa adicionada com sucesso!', 'success')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('tasks', None)
    flash('Sessão encerrada e tarefas removidas.', 'info')
    return redirect(url_for('index'))



@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    
    if not title or not description:
        flash('Título e descrição são obrigatórios!', 'error')
        return redirect(url_for('index'))

    task = {
        'title': title,
        'description': description,
        'due_date': due_date
    }
    session['tasks'].append(task)
    
    total_tasks = request.cookies.get('total_tasks', 0)
    total_tasks = int(total_tasks) + 1
    
    flash('Tarefa adicionada com sucesso!', 'success')
    
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('total_tasks', str(total_tasks))
    return resp

@app.route('/')
def index():
    if 'tasks' not in session:
        session['tasks'] = []
    total_tasks = request.cookies.get('total_tasks', 0)
    return render_template('index.html', tasks=session['tasks'], total_tasks=total_tasks)

