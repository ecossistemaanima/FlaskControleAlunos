# adiciona o , render_template
from flask import Blueprint, render_template
from ..extensions import db
from ..models.uc import Uc

#Instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
#    return "Teste"
    #adiciona isso
#    db.create_all()
#   Adiciona o acesso a banco e a chamada ao render_template
    ucs_query = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_query)
