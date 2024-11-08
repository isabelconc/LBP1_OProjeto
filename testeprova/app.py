

@app.before_request
def require_login():
    allowed_routes = ['index', 'login']  
    if request.endpoint not in allowed_routes and 'tasks' not in session:
        flash('Por favor, faça login para acessar a página de agenda.', 'warning')
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
