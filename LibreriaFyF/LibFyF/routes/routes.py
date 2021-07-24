from flask import Blueprint, render_template

global_scope = Blueprint("views", __name__)#con esto voy a definir rutas que vamos a abrir del navegador

#nav={} preguntar que variables irían dentro del nav

@global_scope.route('/inicio', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

#fijate si van todas las rutas aca