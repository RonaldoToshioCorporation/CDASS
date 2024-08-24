from pydantic import BaseModel
from typing import Optional, List
from model import Base
from model.tipo_operacao import TipoOperacao


class TipoOperacaoSchema(BaseModel):
    """Define como um novo registro que será inserido """    
    sigla: str = "D"
    descricao: str = "Diaria"


class TipoOperacaoViewSchema(BaseModel):
    """ Define como deverá retornado
    """
    codigo: int = 1
    sigla: str = "M"
    descricao: str = "Mensal"


class TipoOperacaoEditSchema(BaseModel):
    """Define como será recebido os dados para a edição """
    codigo: int = 1
    sigla: str = 'E'    
    descricao: str = 'Eventual 2'


class TipoOperacaoBuscaDelSchema(BaseModel):
    """ Define como a estrutura que representa a busca de delete.Que será
        feita apenas com o codigo da TipoOperacao.

    """
    codigo: int = 1


class ListaTipoOperacaosSchema(BaseModel):
    """ Define como retorna a lista de TipoOperacaos de operacao.
    """
    TipoOperacaos: List[TipoOperacaoViewSchema]


def apresenta_tipo_operacao(tipo_operacao: TipoOperacao):
    """ Retorna uma representação de um TipoOperacao seguindo o schema definido em
        TipoOperacaoViewSchema.
    """
    return {
        "codigo": tipo_operacao.codigo,
        "sigla": tipo_operacao.sigla,
        "descricao": tipo_operacao.descricao
        # "modelos": [{"codigo": c.cod_modelo, "nome": c.nom_modelo} for c in TipoOperacao.modelos] 
    }


def apresenta_lista_tipo_operacao(lista: List[TipoOperacao]):
    """ Retorna uma representação da TipoOperacao de veiculo seguindo o schema definido em
        TipoOperacaoViewSchema.

    """
    result = []
    for item in lista:
       
        result.append({
            "codigo": item.codigo,
            "sigla": item.sigla,
            "descricao": item.descricao
        })

    return {"lista": result}    