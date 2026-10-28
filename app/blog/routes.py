from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, template_folder='templates')

entradas_db = {
    1: {"titulo": "Nuevos productos destacados para esta temporada"},
    2: {"titulo": "Guía de compra: Cómo elegir el mejor artículo para ti"},
    3: {"titulo": "Descuentos especiales y ofertas de fin de semana"}
}

@blog_bp.route('/entrada/<int:id>')
def mostrar_entrada(id):
    entrada = entradas_db.get(id)
    
    if entrada:
        return render_template('blog/entrada.html', entrada=entrada)
    else:
        return "<h1>Entrada no encontrada</h1>", 404