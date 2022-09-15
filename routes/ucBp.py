# Importando o Blueprint
from flask import Blueprint
#adiciona isso
from ..extensions import db
from ..models.uc import Uc

#Instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
#    return "Teste"
    #adiciona isso
    db.create_all()