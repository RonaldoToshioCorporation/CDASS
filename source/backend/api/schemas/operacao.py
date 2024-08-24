 
from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional, List
from model import Base
from model.operacao import Operacao
from schemas.tipo_operacao import TipoOperacaoViewSchema
from sqlalchemy import Numeric
 
class OperacaoSchema(BaseModel):
    """Define como um novo registro que será inserido """        
    placa_veiculo: str = "ABC1234"   
    codigo_tipo_operacao: int = 1
    observacao: str  = ""
    data_entrada: datetime  


class OperacaoViewSchema(BaseModel):
    """ Define como deverá retornado
    """
    codigo: int = 1
    data_entrada: datetime 
    data_saida: datetime 
    codigo_tipo_operacao: int = 1
    placa_veiculo: str = "ABC1234"
    tipo_operacao: TipoOperacaoViewSchema 
    total_permanencia: int = 0
    valor_total: float = 0 
    valor_base_calculo: float = 0 

class OperacaoBuscaPorVeiculoSchema(BaseModel):
    """ Define como será recebido os dados para a pesquisa """
    placa_veiculo: str = "ABC1234"

class OperacaoBuscaPorDataEntradaSchema(BaseModel):
    """ Define como será a pesquisa por data """
    data_entrada: date
    
class OperacaoEditSchema(BaseModel):
    """Define como será recebido os dados para a edição """
    codigo: int = 1
    codigo_tipo_operacao: int = 1
    observacao: str = ""


class OperacaoBuscaDelSchema(BaseModel):
    """ Define como a estrutura que representa a busca de delete.Que será
        feita apenas com o codigo da Operacao.

    """
    codigo: int = 1


class OperacaoSaidaVeiculoSchema(BaseModel):    
    """ Define como a estrutura que representa a baixa de saida do veiculo.Que será
         feita apenas com o codigo da Operacao.

    """    
    codigo: int = 1
    codigo_tipo_operacao: int = 1
    data_saida: str = "2023-01-01 22:00:00"    
    total_permanencia: int = 0
    valor_total: float = 0 
    valor_base_calculo: float = 0 
    observacao : str = ''



class ListaOperacaosSchema(BaseModel):
    """ Define como retorna a lista de Operacaos de operacao.
    """
    Operacaos: List[OperacaoViewSchema]


def apresenta_operacao(operacao: Operacao):
    """ Retorna uma representação de um Operacao seguindo o schema definido em
        OperacaoViewSchema.
    """    
    return {
        "codigo": operacao.codigo,
        "codigo_tipo_operacao": operacao.codigo_tipo_operacao,
        "placa_veiculo": operacao.placa_veiculo,
        "observacao": operacao.observacao,
        "data_entrada": operacao.data_entrada,
        "data_saida": operacao.data_saida,
        "total_permanencia": operacao.total_permanencia,
        "valor_total": operacao.valor_total,
        "valor_base_calculo": operacao.valor_base_calculo,
        "tipo_operacao": [  {"codigo": operacao.codigo_tipo_operacao ,
                             "sigla": operacao.tipo_operacao.sigla,
                             "descricao": operacao.tipo_operacao.descricao
                           }]
        
    }


def apresenta_lista_operacao(lista: List[Operacao]):
    """ Retorna uma representação da lista de operacoes seguindo o schema definido em
        OperacaoViewSchema.

    """
    result = []
    for item in lista:
       
        result.append({
            "codigo": item.codigo,
            "codigo_tipo_operacao": item.codigo_tipo_operacao,
            "placa_veiculo": item.placa_veiculo,
            "data_entrada": item.data_entrada,
            "data_saida": item.data_saida,
            "observacao": item.observacao,
            "total_permanencia": item.total_permanencia,
            "valor_total": item.valor_total,
            "valor_base_calculo": item.valor_base_calculo,
            "tipo_operacao": [{"codigo": item.codigo_tipo_operacao ,
                             "sigla": item.tipo_operacao.sigla,
                             "descricao": item.tipo_operacao.descricao
                           }]
        })

    return {"lista": result}    