from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError
from model import Session, Album
from logger import logger
from schemas import *
from flask_cors import CORS


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger,\
                             Redoc ou RapiDoc")
album_Tag = Tag(
    name="Album", description="Adição, edição, exclusão e consultas de albuns")

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite\
       a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# ***************************************************  Metodos do Album ***************************************
# Novo registro na tabela album


@app.post('/album', tags=[album_Tag],
          responses={"201": AlbumViewSchema,
                     "404": ErrorSchema,
                     "500": ErrorSchema})
def add_album(form: AlbumSchema):
    album = Album(
        id=form.id,
        title=form.title,
        artist=form.artist,
        price=form.price
    )

    logger.debug(f"Adicionando o album {album.title}")

    try:
        # criando conexão com a base
        session = Session()
        # adicionando
        session.add(album)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado o album com {album.title}")

        return apresenta_album(album), 200

    except IntegrityError as e:
        # como a duplicidade de id é a provável razão do IntegrityError
        error_msg = f"O id do album {album.id} já foi salvo anteriormente na base :/{e}"
        logger.warning(
            f"Erro ao adicionar o album com ID ={album.id}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(
            f"Erro ao adicionar um novo album - error {e}, {error_msg}")
        return {"message": error_msg}, 400

# Edicao registro na tabela tipo_operacao do veiculo


@app.put('/album', tags=[album_Tag],
        responses={
            "204": None,
            "404": ErrorSchema,
            "500": ErrorSchema
        })
def editar_album(form: AlbumEditSchema):
    """Editar uma album """
    id = form.id
    title = form.title
    artitst = form.artist
    price = form.price
    logger.info(f"Editando o album #{id} e title {title}")
    try:
        # criando conexão com a base
        session = Session()

        count = session.query(Album)\
                       .filter(Album.id == id)\
                       .update({
                                "title": title,
                                "artist": artitst,
                                "price": price,
                        })

        session.commit()
        if count:
            # retorna sem representação com apenas o codigo http 204
            logger.debug(f"Editado o album #{id}")
            return '', 204
        else:
            error_msg = f"O album com o #{id} não foi encontrado na base"
            logger.warning(f"Erro ao editar o album com o #{id} , {error_msg}")
            return ' ', 404
    except Exception as e:
            # caso um erro fora do previsto
            error_msg = f"Este titulo de album {title} já existe com outro codigo! :/{e.__str__}"
            logger.warning(
                f"Erro ao editar o album com o #'{id}', {error_msg}")
            return {"message": error_msg}, 400

# Remoção de um registro de album


@app.delete('/album', tags=[album_Tag],
            responses={
                "204": None,
                "400": ErrorSchema,
                "404": ErrorSchema,
                "500": ErrorSchema
            }
        )
def del_album(form: AlbumBuscaDelSchema):
    id = form.id
    logger.debug(f"Excluindo o album #{id}")


    try:
        # criando conexão com a base
        session = Session()

        # fazendo a remoção
        count = session.query(Album).filter(
            Album.id == id).delete()

        session.commit()

        if count:
            # retorna sem representação com apenas o codigo http 204
            logger.debug(f"Excluido o album com o id #{id} com sucesso!")
            return '', 204

        else:
            # se o   não foi encontrado retorno o codigo http 404
            error_msg = "O album não foi encontrado na base"

            logger.warning(
                f"Erro ao excluir o album com o id #'{id}', {error_msg}")

            return '', 404

    except Exception as e:

        # caso um erro fora do previsto
        error_msg = f"Não foi possível excluir o album:/{e}"

        logger.warning(
            f"Erro ao excluir o album com o id #'{id}', {error_msg}")

        return {"message": error_msg}, 500

# Consulta de todos os albuns
@app.get('/albuns', tags=[album_Tag],
         responses={"200": ListaAlbunsSchema,
                    "404": ErrorSchema,
                    "500": ErrorSchema})
def get_albuns():
    """Consulta os albuns 

    Retorna uma listagem de representações de albuns
    """
    logger.debug(f"Consultando os albuns   ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        lista = session.query(Album).all()

        if not lista:
            error_msg = 'Não foi encontrado registros'
            # se não há tipo_operacaos cadastrados
            return {"lista":[]}, 200
        else:
            logger.debug(f"%d tipo_operacoes encontrados" %
                         len(lista))
            # retorna a representação de tipo_operacaos
            return apresenta_lista_Albuns(lista), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar os albuns :/{str(e)}"
        logger.warning(
            f"Erro ao consultar albuns, {error_msg}")
        return {"message": error_msg}, 500


# Consulta album especifico 
@app.get('/album', tags=[album_Tag],
         responses={"200": AlbumBuscaEditSchema,
                    "404": ErrorSchema,
                    "500": ErrorSchema})
def get_album_id(query: AlbumBuscaEditSchema):

    id = query.id;

    logger.debug( f"Consultando um album por id = #{id} ")

    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        album = session.query(Album).filter(Album.id == id).first();
        
        
        # se não há marcas cadastrados
        if (not album):

            error_msg ="Não foi encontrado o album!"
            logger.warning(f"Erro ao buscar o album id, {id}")
            return {"message": error_msg}, 404            

        else:            
            # retorna a representação de modelos            
            return apresenta_album(album), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar o album :/{str(e)}"
        logger.warning(
            f"Erro ao consultar o album, {error_msg}")
        return {"message": error_msg}, 500
 