from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from datetime import datetime
from schema.error import *
from schema.inventario import *
from model import Session, inventario
from flask_cors import CORS

info = Info(title="API Inventario de Produtos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
inventario_tag = Tag(name="Inventario", description="Adição, visualização e remoção de produtos teve inventario")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')
  
@app.post('/inventarios', tags=[inventario_tag],
          responses={"200": InventarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})


def add_inventario(form: InventarioSchema):
    """Adiciona um novo inventario de produto realizado pelo auditor fiscal à base de dados

    Retorna detalhes do Inventario.
    """
    inventario = Inventarios(

            nome_produto = form.nome_produto,
            categoria = form.categoria,
            pratileira = form.pratileira,
            posicao = form.posicao,
            quantidade = form.quantidade,
            id_auditor =form.id_auditor,
        )
    try:

        session = Session()

        session.add(inventario)

        session.commit()
        return apresenta_inventario(inventario), 200

    except IntegrityError as e:

        error_msg = "Produto foi auditodo de mesmo nome já foi salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:

        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400


# Metodo GET
@app.get('/inventarios', tags=[inventario_tag],
         responses={"200": ListagemInventarioSchema, "404": ErrorSchema})


def get_inventario():
    """Faz a busca por uma descrição de produto a partir do id produto

    Retorna uma representação de produtos auditados.
    """


    session = Session()

    inventarios = session.query(Inventarios).all()

    if not inventario:

        return {"inventarios": []}, 200
    else:

        return apresenta_inventarios(inventarios), 200
