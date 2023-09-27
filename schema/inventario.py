from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from model.inventario import Inventarios


class InventarioSchema(BaseModel):
    """ Define como um novo registro de auditoria de inventarios produtos faltantes no estoque
    """
    
    nome_produto : str = "Camisa Polo G"
    categoria : str = "Camisa"
    pratileira : str =  "120"
    posicao : str =  "12"
    quantidade : int = "5"
    id_auditor : str = "12345"
    

class InventarioBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com nome do produto.
    """
    nome_produto: str = "Digite nome produto"


class ListagemInventarioSchema(BaseModel):
    """ Define como uma listagem de produtos que teve auditoria.
    """
    inventario:List[InventarioSchema]


def apresenta_inventarios(inventarios: List[Inventarios]):
    """ Retorna uma representação de produtos auditados seguindo o schema definido em
        InventarioViewSchema.
    """
    result = []
    for inventario in inventarios:
        result.append({
            "nome_produto":inventario.nome_produto,
            "categoria":inventario.categoria,
            "pratileira":inventario.pratileira,
            "posicao":inventario.posicao,
            "quantidade": inventario.quantidade,
            "id_auditor":inventario.id_auditor,
            "data_inventario":inventario.data_insercao,
        })

    return {"inventarios": result}


class InventarioViewSchema(BaseModel):
    """ Define como um auditoria será retornado: descrição de produtos auditados).
    """
        
    id_inventario: int = 1    
    nome_produto : str = "Camisa Polo G"
    categoria : str = "Camisa"
    pratileira : str =  "120"
    posicao : str =  "12"
    quantidade : int = "5"
    id_auditor : str = "12345"
    data_insercao : str = "12/03/2023"


class InventarioDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome_produto: str

def apresenta_inventario(inventario: Inventarios):
    """ Retorna uma representação da auditoria seguindo o schema definido em
        InventarioViewSchema.
    """
    return {
        "id_inventario": inventario.id_inventario,
        "nome_produto":inventario.nome_produto,
        "categoria":inventario.categoria,
        "pratileira":inventario.pratileira,
        "posicao":inventario.posicao,
        "quantidade": inventario.quantidade,
        "id_auditor":inventario.id_auditor,     
        
    }