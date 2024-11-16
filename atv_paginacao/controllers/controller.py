from flask import Blueprint, jsonify, render_template, request

produtosController = Blueprint("produtos", __name__)

# lista JSON de produtos
products = [
    {"id": 1, "name": "Produto 1", "description": "Descrição do Produto 1"},
    {"id": 2, "name": "Produto 2", "description": "Descrição do Produto 2"},
    {"id": 3, "name": "Produto 3", "description": "Descrição do Produto 3"},
    {"id": 4, "name": "Produto 4", "description": "Descrição do Produto 4"},
    {"id": 5, "name": "Produto 5", "description": "Descrição do Produto 5"},
    {"id": 6, "name": "Produto 6", "description": "Descrição do Produto 6"},
]

@produtosController.route("/")
def index():
    # fazendo a paginação
    page = request.args.get("page", 1, type=int) # setando a página (page (aparece na url), valor (se não tiver (/), deve ser 1), tipo)
    per_page = 3 # fazendo display de 3 itens (produtos) por página
    start = (page - 1) * per_page # pegando o índice de pages e multiplicando por qtos itens serão exibidos
    end = start + per_page
    total_pages = (len(products) + per_page - 1) // per_page # calculando o total de pages necessárias para exibir todos os produtos
    paginated_products = products[start:end] # fatiamento python, obtendo só os produtos que quero na página 
    return render_template("index.html", products=paginated_products, page=page, total_pages=total_pages)

# @produtosController.route("/product/<int:product_id>")
    def get_product(product_id):
    # Buscar produto por ID
    # product = next((p for p in products if p["id"] == product_id), None)
    # if product:
        return jsonify(product)
    return jsonify({"error": "Produto não encontrado"}), 404


