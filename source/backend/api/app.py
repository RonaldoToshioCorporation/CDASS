from ctypes import cast
from datetime import date, datetime
import functools
import json
from pyclbr import Function
from sqlite3 import Date
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy import and_, func, null
from sqlalchemy.exc import IntegrityError

from model import Session, TipoOperacao, Operacao
from logger import logger
from schemas import *
from flask_cors import CORS
import pip._vendor.requests 




info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger,\
                             Redoc ou RapiDoc")

tipo_operacao_Tag = Tag(name="TipoOperacao", 
                        description="Adição, visualização,\
                                    edição e remoção de tipo_operacaos de veiculos à base")

operacao_Tag = Tag(name="Operacao", 
                        description="Adição, visualização,\
                                    edição e remoção de tipo_operacaos de veiculos à base")
 
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite\
       a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# ***************************************************  Metodos do tipo de operacao ***************************************
# Novo registro na tabela tipo_operacao do veiculo
@app.post('/tipo_operacao', tags=[tipo_operacao_Tag],
          responses={"201": TipoOperacaoViewSchema,
                     "404": ErrorSchema,
                     "500": ErrorSchema})
def add_tipo_operacao(form: TipoOperacaoSchema):
    """ Adicionar a tipo_operacao de operacao """
    tipo_operacao = TipoOperacao(      
      sigla = form.sigla,
      descricao = form.descricao
    )

    logger.debug(f"Adicionando o tipo_operacao de operacao com a sigla {tipo_operacao.sigla}\
                     descricao { tipo_operacao.descricao }")
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando  
        session.add(tipo_operacao)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado o tipo_operacao de operacao com a sigla {tipo_operacao.sigla}\
                      descricao{tipo_operacao.descricao}")
        return apresenta_tipo_operacao(tipo_operacao), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = f"O tipo de operacao com a sigla {tipo_operacao.sigla} já foi salvo anteriormente na base :/{e}"
        logger.warning(
            f"Erro ao adicionar a tipo_operacao do operacao com nome ={tipo_operacao.descricao}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar um novo tipo_operacao de operacao - error {e}, {error_msg}")
        return {"message": error_msg}, 400


# Edicao registro na tabela tipo_operacao do veiculo
@app.put('/tipo_operacao', tags=[tipo_operacao_Tag],
         responses={"204": None,
                    "404": ErrorSchema,
                    "500": ErrorSchema})
def upd_tipo_operacao(form: TipoOperacaoEditSchema):
    """Editar uma tipo_operacao de veiculojá cadastrado na base """
    codigo = form.codigo
    sigla = form.sigla
    descricao = form.descricao
    logger.info(f"Editando a tipo_operacao de operacao #{codigo} e sigla {sigla}")
    logger.debug(f"Editando a tipo_operacao de operacao #{codigo}")
    try:

        # criando conexão com a base
        session = Session()
 
        count = session.query(TipoOperacao).filter(
            TipoOperacao.codigo == codigo)\
                        .update({"descricao": descricao,
                                "sigla": sigla})
        session.commit()
        if count:
            # retorna sem representação com apenas o codigo http 204
            logger.debug(f"Editado a tipo_operacao com a sigla {sigla}")
            return '', 204
        else:
            error_msg = f"O tipo_operacao com a sigla {sigla} não foi encontrado na base"
            logger.warning(f"Erro ao editar o tipo_operacao com a sigla {sigla} , {error_msg}")
            return ' ', 404
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Esta sigla já existe com outro codigo! :/{e.__str__}"
        logger.warning(
            f"Erro ao editar o tipo_operacao com a sigla  #'{sigla}', {error_msg}")
        return {"message": error_msg}, 400


# Remoção de um registro de tipo_operacao de veiculo
@app.delete('/tipo_operacao', tags=[tipo_operacao_Tag],
            responses={"204": None,
                       "400": ErrorSchema,
                       "404": ErrorSchema,
                       "500": ErrorSchema})
def del_tipo_operacao(form: TipoOperacaoBuscaDelSchema):
    """Exclui uma tipo_operacao da base de dados através do atributo codigo

    Retorna uma mensagem de exclusão com sucesso.
    """
    codigo = form.codigo
    logger.debug(f"Excluindo a tipo_operacaoID #{codigo}")
    try:
        # criando conexão com a base
        session = Session()
        # validar se está sendo utilizado no operacao  
        operacao = session.query(Operacao)\
                             .filter(Operacao.codigo_tipo_operacao == codigo).first()
        print(operacao)

        if operacao:
            # se há   cadastrado
            error_msg = "O Tipo de Operacao está associado há um ou mais operações."
            logger.warning(f"Erro ao buscar a tipo_operacao de operacao , {error_msg}")
            return {"message": error_msg}, 400                

        # fazendo a remoção
        count = session.query(TipoOperacao).filter(
            TipoOperacao.codigo == codigo).delete()
        session.commit()

        if count:
            # retorna sem representação com apenas o codigo http 204
            logger.debug(f"Excluindo o tipo_operacao com o codigo #{codigo}")
            return '', 204
        else:
            # se o   não foi encontrado retorno o codigo http 404
            error_msg = "O tipo_operacao de operacao não foi encontrado na base"
            logger.warning(
                f"Erro ao excluir o tipo_operacao com o \
                 codigo #'{codigo}', {error_msg}")
            return '', 404
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível excluir tipo_operacao  :/{e}"
        logger.warning(
            f"Erro ao excluir a tipo_operacao com\
            o codigo #'{codigo}', {error_msg}")
        return {"message": error_msg}, 500


# Consulta de todos as tipo_operacaos
@app.get('/tipo_operacoes', tags=[tipo_operacao_Tag],
         responses={"200": ListaTipoOperacaosSchema,
                    "404": ErrorSchema,
                    "500": ErrorSchema})
def get_tipo_operacaos():
    """Consulta as tipo_operacoes 

    Retorna uma listagem de representações dos tipo_operacoes
    """
    logger.debug(f"Consultando as tipo_operacoes   ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        lista = session.query(TipoOperacao).all()

        if not lista:
            error_msg = 'Não foi encontrado registros'
            # se não há tipo_operacaos cadastrados
            return {"lista":[]}, 200
        else:
            logger.debug(f"%d tipo_operacoes encontrados" %
                         len(lista))
            # retorna a representação de tipo_operacaos
            return apresenta_lista_tipo_operacao(lista), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar os tipo_operacoes de listas :/{str(e)}"
        logger.warning(
            f"Erro ao consultar tipo_operacoes, {error_msg}")
        return {"message": error_msg}, 500


# Consulta por código de tipo_operacao
@app.get('/tipo_operacao_id', tags=[tipo_operacao_Tag],
         responses={"200": TipoOperacaoViewSchema, "404": ErrorSchema,
                    "500": ErrorSchema})
def get_tipo_operacao_id(query: TipoOperacaoBuscaDelSchema):
    """Consulta um tipo_operacao pelo codigo

    Retorna uma representação da tipo_operacao  
    """

    codigo = query.codigo

    logger.debug(
        f"Consultando a tipo_operacao por codigo = #{codigo} ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        tipo_operacao = session.query(TipoOperacao)\
                             .filter(TipoOperacao.codigo == codigo).first()

        if not tipo_operacao:
            # se não há   cadastrado
            error_msg = "Tipo Operacao não encontrado na base :/"
            logger.warning(f"Erro ao buscar a tipo_operacao de operacao , {error_msg}")
            return {"message": error_msg}, 404
        else:
            logger.debug(
                f"Tipo Operacao #{codigo} encontrado")
            # retorna a representação de  s
            return apresenta_tipo_operacao(tipo_operacao), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar a tipo_operacao:/{str(e)}"
        logger.warning(
            f"Erro ao consultar a tipo_operacao do operacao, {error_msg}")
        return {"message": error_msg}, 500



# ***************************************************  Metodos de operacao ***************************************
# Novo registro na tabela tipo_operacao do veiculo
@app.post('/operacao', tags=[operacao_Tag],
          responses={"201": OperacaoViewSchema,
                     "404": ErrorSchema,
                     "500": ErrorSchema})
def add_operacao(form: OperacaoSchema):
    """ Adicionar a operacao """
    operacao = Operacao(      
      codigo_tipo_operacao =  form.codigo_tipo_operacao,
      placa_veiculo = form.placa_veiculo,
      observacao = form.observacao,
      data_entrada = form.data_entrada
    )
    
    try:
          
        # criando conexão com a base
        session = Session()
        
        # adicionando  
        session.add(operacao)

        # efetivando o comando de adição de novo item na tabela
        session.commit()
        message = f"Adicionado operacao com o codigo tipo {operacao.codigo_tipo_operacao}\
                  e veículo {operacao.placa_veiculo}"
        logger.debug(message)
        logger.info(message)
        return apresenta_operacao(operacao), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = f"A operacao já foi salvo anteriormente na base :/"
        logger.warning(
            f"Erro ao adicionar a operacao")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar a operacao erro = {e}")
        return {"message": error_msg}, 500


# Consulta de todos as operacoes
@app.get('/operacoes', tags=[operacao_Tag],
         responses={"200": ListaOperacaosSchema, 
                    "404": ErrorSchema,
                    "500": ErrorSchema})
def get_operacoes():
    """Consulta as operacoes 

    Retorna uma listagem de representações das operacoes
    """
    logger.debug(f"Consultando as operacoes   ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        lista = session.query(Operacao).order_by(Operacao.data_entrada.asc()).all()
        print(lista)
        if not lista:
            
            # se não há operacaos cadastrados
            return {"lista": []}, 200
        else:
            logger.debug(f"%d operacoes encontrados" %
                         len(lista))
            # retorna a representação de tipo_operacaos
            return apresenta_lista_operacao(lista), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar as operacoes de listas :/{str(e)}"
        logger.warning(
            f"Erro ao consultar as operacoes, {error_msg}")
        return {"message": error_msg}, 500


# Consulta por código de operacao
@app.get('/operacao_id', tags=[operacao_Tag],
         responses={"200": OperacaoViewSchema, "404": ErrorSchema,
                    "500": ErrorSchema})
def get_operacao_id(query: OperacaoBuscaDelSchema):
    """Consulta uma operacao especifica pelo codigo

    Retorna uma representação da operacao  
    """

    codigo = query.codigo

    logger.debug(
        f"Consultando a operacao por codigo = #{codigo} ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        operacao = session.query(Operacao)\
                             .filter(Operacao.codigo == codigo).first()

        if not operacao:
            # se não há cadastrado
            error_msg = "Operacao não encontrado na base :/"
            logger.warning(f"Erro ao buscar a operacao error, {error_msg}")
            return {"message": error_msg}, 404
        else:
            logger.debug(
                f"A operacao com o código #{codigo} encontrado")
            # retorna a representação de  s
            return apresenta_operacao(operacao), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar a operacao:/{str(e)}"
        logger.warning(
            f"Erro ao consultar a operacao com erro {e}, {error_msg}")
        return {"message": error_msg}, 500


# Consulta por data de entrada 
@app.get('/operacao_data_entrada', tags=[operacao_Tag],
 responses={"200": ListaOperacaosSchema, "404": ErrorSchema,
                    "500": ErrorSchema})
def get_lista_por_data_entrada(query: OperacaoBuscaPorDataEntradaSchema):    
    """ Consulta as operacoes 
        Retorna uma listagem de representações das operacoes por data de entrada

    """
    data_entrada_param = query.data_entrada

    logger.debug(f"Consultando as operacoes   ")
    try:
        # criando conexão com a base
        session = Session()
        print(data_entrada_param)
        # fazendo a busca
        lista = session.query(Operacao)\
                       .filter(func.date(Operacao.data_entrada)  == data_entrada_param).all()
                       

        if not lista:
            error_msg = 'Não foi encontrado registros!'
            # se não há operacaos cadastrados
            return {"lista": []}, 200
        else:
            logger.debug(f"%d operacoes encontrados" %
                         len(lista))
            # retorna a representação de tipo_operacaos
            return apresenta_lista_operacao(lista), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar as operacoes de listas :/{str(e)}"
        logger.warning(
            f"Erro ao consultar as operacoes, {error_msg}")
        return {"message": error_msg}, 500



# Consulta por código de veiculo
@app.get('/operacao_veiculo_id', tags=[operacao_Tag],
         responses={"200": OperacaoViewSchema, "404": ErrorSchema,
                    "500": ErrorSchema})
def get_operacao_veiculo_id(query: OperacaoBuscaPorVeiculoSchema):
    """Consulta uma operacao especifica pelo codigo do veiculo

    Retorna uma lista de representações da operacao  
    """

    placa_veiculo = query.placa_veiculo

    logger.debug(
        f"Consultando a operacao por codigo veiculo = #{placa_veiculo} ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        operacao = session.query(Operacao)\
                             .filter(Operacao.placa_veiculo == placa_veiculo,\
                                     Operacao.data_saida == None).first()

        if not operacao:
            # se não há cadastrado
            error_msg = "Operacao não encontrado na base :/"
            logger.warning(f"Erro ao buscar a operacao error, {error_msg}")
            return {"message:" : error_msg}, 404
        else:
            logger.debug(
                f"A operacao com o código do veiculo #{placa_veiculo} encontrado")
            # retorna a representação de  s
            return apresenta_operacao(operacao), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar a operacao:/{str(e)}"
        logger.warning(
            f"Erro ao consultar a operacao com erro {e}, {error_msg}")
        return {"message": error_msg}, 500


# Edicao registro na tabela operacao do veiculo
@app.put('/operacao', tags=[operacao_Tag],
         responses={"204": None,
                    "400": ErrorSchema,
                    "404": ErrorSchema,
                    "500": ErrorSchema})
def upd_operacao(form: OperacaoEditSchema):
    """Editar a operacao cadastrado na base """
    codigo = form.codigo
    observacao = form.observacao
    codigo_tipo = form.codigo_tipo_operacao
    
    logger.debug(f"Editando a operacao de operacao #{codigo}")
    try:

        # criando conexão com a base
        session = Session()
               
        count = session.query(Operacao).filter(
            Operacao.codigo == codigo)\
                        .update({"observacao": observacao, "codigo_tipo_operacao": codigo_tipo})

        session.commit()

        if count:
            message = f"Editado com sucesso a operacao com o código {codigo}!"
            # retorna sem representação com apenas o codigo http 204
            logger.debug(message)
            return message, 204
        else:
            error_msg = f"A operacao com o código {codigo} não foi encontrado na base"
            logger.warning(
                f"Erro ao editar a operacao com o código {codigo} , {error_msg}")
            return error_msg, 404

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível editar a operacao :/{e.__str__}"
        logger.warning(
            f"Erro ao editar a operacao com o código  #'{codigo}', {error_msg}")
        return {"message": error_msg}, 500


# Remoção de um registro de operacao
@app.delete('/operacao', tags=[operacao_Tag],
            responses={"204": None, "404": ErrorSchema, "500": ErrorSchema})
def del_operacao(form: OperacaoBuscaDelSchema):
    """Exclui uma operacao da base de dados através do atributo codigo

    Retorna uma mensagem de exclusão com sucesso.
    """
    codigo = form.codigo
    logger.debug(f"Excluindo a operacaoID #{codigo}")
    try:
        # criando conexão com a base
        session = Session()
        
        # fazendo a remoção
        count = session.query(Operacao).filter(
                Operacao.codigo == codigo).delete()

        session.commit()

        if count:
            # retorna sem representação com apenas o codigo http 204
            message = f"Excluido a operacao com o codigo #{codigo}"
            logger.debug(message)
            return message, 204
        else:
            # se o   não foi encontrado retorno o codigo http 404
            error_msg = "A operacao não foi encontrada na base"

            logger.warning(
                f"Erro ao excluir a operacao com o codigo #'{codigo}', {error_msg}")

            return '', 404
            
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível excluir a operacao"

        logger.warning(
            f"Erro ao excluir a operacao com\
            o codigo #'{codigo}' - erro = {e},\
            {error_msg}")

        return {"message": error_msg}, 500
 

 
# Edicao registro na tabela operacao do veiculo
@app.put('/operacao_saida_veiculo', tags=[operacao_Tag],
         responses={"204": None,
                    "404": ErrorSchema,
                    "500": ErrorSchema})
def upd_baixa_operacao(form: OperacaoSaidaVeiculoSchema):
    """Edita a operacao cadastrado na base complementando os valores de saida do veiculo"""
    codigo = form.codigo
    data_saida = datetime.strptime(form.data_saida, "%Y-%m-%d %H:%M:%S")   
    codigo_tipo = form.codigo_tipo_operacao
    total_permanencia = form.total_permanencia
    valor_total = form.valor_total
    valor_base_calculo = form.valor_base_calculo

    observacao = form.observacao
    
    
    logger.debug(f"Editando a operacao de operacao #{codigo}")
    try:

        # criando conexão com a base
        session = Session()
        
        count = session.query(Operacao).filter(
            Operacao.codigo == codigo)\
                        .update({"observacao": observacao,
                                 "data_saida": data_saida,
                                 "codigo_tipo_operacao": codigo_tipo,
                                 "total_permanencia": total_permanencia,
                                 "valor_total": valor_total,
                                 "valor_base_calculo": valor_base_calculo })

        session.commit()

        if count:
            message = f"Editado com sucesso a operacao com o código {codigo}!"
            # retorna sem representação com apenas o codigo http 204
            logger.debug(message)
            return message, 204
        else:
            error_msg = f"A operacao com o código {codigo} não foi encontrado na base"
            logger.warning(
                f"Erro ao editar a operacao com o código {codigo} , {error_msg}")
            return error_msg, 404

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível editar a operacao :/{e.__str__}"
        logger.warning(
            f"Erro ao editar a operacao com o código  #'{codigo}', {error_msg}")
        return {"message": error_msg}, 500