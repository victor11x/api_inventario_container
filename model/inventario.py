from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime,date
from typing import Union

from model import Base

class Inventarios(Base):
    __tablename__ = 'inventario'

    id_inventario = Column("pk_inventario", Integer, primary_key=True)
    nome_produto = Column(String(140))
    categoria = Column(String(140)) 
    pratileira = Column(String(4))
    posicao = Column(String(20))
    quantidade = Column(Integer)
    id_auditor = Column(String(20))
    data_insercao = Column(DateTime, default=datetime.now())
    
    
def __init__(self, nome_produto:str, categoria:str, pratileira: str, posicao: str,quantidade:int, id_auditor:str,data_insercao:Union[DateTime, None] = None):
        """
        Produtos faltantes no estoque 

        Arguments:
  
        """
        self.nome_produto = nome_produto
        self.categoria = categoria
        self.pratileira = pratileira
        self.posicao = posicao
        self.quantidade = quantidade
        self.id_auditor = id_auditor
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
        