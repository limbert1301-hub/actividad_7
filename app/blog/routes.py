from flask import Blueprint

# Creamos el Blueprint para el blog
blog_bp = Blueprint('blog', __name__)

# Simulación de una base de datos de entradas
entradas_db = {
    1: {"titulo": "Nuevos productos destacados para esta temporada"},
    2: {"titulo": "Guía de compra: Cómo elegir el mejor artículo para ti"},
    3: {"titulo": "Descuentos especiales y ofertas de fin de semana"}
}

@blog_bp.route('/entrada/<int:id>')
def mostrar_entrada(id):
    # Buscamos la entrada según el id recibido en la URL
    entrada = entradas_db.get(id)
    
    if entrada:
        return f"<h1>{entrada['titulo']}</h1>"
    else:
        return "<h1>Entrada no encontrada</h1>", 404