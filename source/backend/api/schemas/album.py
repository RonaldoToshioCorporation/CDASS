from pydantic import BaseModel
from typing import Optional, List
from model import Base
from model.album import Album
from sqlalchemy import Numeric
 
class AlbumSchema(BaseModel):
    """Define como um novo registro que será inserido """        
    id: int  = 1    
    title: str  = ""
    artist:str = ""
    price: float = 0 

class AlbumViewSchema(BaseModel):
    """ Define como deverá retornado
    """
    id: int = 1
    title: str = 'Blaze of Glory'
    artist: str = 'Jon Bon Jovi'
    price: float = 80.50    


class AlbumEditSchema(BaseModel):
    """Define como será recebido os dados para a edição """
    id: int = 0
    title: str = ''
    artist: str = ''
    price: float = 0


class ListaAlbunsSchema(BaseModel):
    """ Define como retorna a lista de Albuns.
    """
    Albuns: List[AlbumViewSchema]


class AlbumBuscaDelSchema(BaseModel):
    """ Define como a estrutura que representa a busca de delete.Que será
        feita apenas com o id do album.

    """
    id: int = 1


def apresenta_album(album: Album):
    """ Retorna uma representação de um Album seguindo o schema definido em
        AlbumViewSchema.
    """    
    return {
        "id": album.id,
        "title": album.title,
        "artist": album.artist,
        "price": album.price        
    }


def apresenta_lista_Albuns(albuns: List[Album]):
    """ Retorna uma representação da lista de albuns seguindo o schema definido em
        OperacaoViewSchema.

    """
    result = []
    for album in albuns:
       
        result.append({
            "id": album.id,
            "title": album.title,
            "artist": album.artist,
            "price": album.price
        })

    return {"albuns": result}    