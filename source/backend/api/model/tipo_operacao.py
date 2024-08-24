from sqlalchemy import Column, String, Integer
from model import Base
from sqlalchemy.orm import relationship

class TipoOperacao(Base):
    __tablename__ = 'tipo_operacao'
    codigo = Column("id_operacao_tip", Integer, primary_key=True)
    sigla = Column("sig_operacao_tip",String(1), unique=True)
    descricao = Column("ds_operacao_tip",String(100))

    ## criar o vinculo com os modelos do veiculo
    operacoes = relationship("Operacao", back_populates="tipo_operacao")
    
    
    def __init__(self, sigla: str, descricao: str):
        """
        Cria uma marca de veiculo

        Argumentos:
            sigla: sigla do tipo de operacao E-EVENTUAL / D-DIARIO / M-MENSAL
        """
        self.sigla = sigla
        self.descricao = descricao

