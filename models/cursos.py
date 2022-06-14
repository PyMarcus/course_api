from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    """
    Classe que cria o modelo de dados a ser utilizados
    É aparente na documentação e também no banco de dados
    Descreve o curso com os parametros id, titulo ,aulas , horas.
    Sendo id não opicional
    """
    id: Optional[int] = None
    titulo: str 
    aulas: int
    hours: float
