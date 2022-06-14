from fastapi import FastAPI
from typing import Any
from data.cursos import cursos
from fastapi import HTTPException
from fastapi import status
from models.cursos import Curso
import json
from fastapi.responses import JSONResponse
from fastapi import Path  # para path parameters : parâmetro que virá no endpoint
from fastapi import Query  # para query parameters parametro via endpoint com ? e &
from fastapi import Header  # para header parameteres: parametro enviado no cabecalho, normalmente, ligado a autenticacao e autorizacao
from typing import Optional



app = FastAPI()


# get methods
@app.get('/')
async def root() -> Any:
    return {'teste': 1}


@app.get('/cursos')
async def getCursos() -> dict:
    return cursos()


@app.get('/cursos/{id_curso}')
async def getCursos(id_curso: int or str = Path(default=None, title="ID do curso", description="Deve estar entre 1 e 2",gt=0, lt=3)) -> dict:  # gt > maior q lt < menor que
    try:
        curso = cursos()[id_curso]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso nao encontrado')
    return curso


# post methods
@app.post('/cursos', status_code=status.HTTP_201_CREATED)  # deve-se informar o status,pois, o fast api retorna 200 para sucesso
async def postCurso(curso: Curso) -> None:
    next_id = len(cursos()) + 1
    if curso.id not in cursos():
        cursos()[next_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail=f"Curso de id: {curso.id} ja existe")


# put methods
@app.put('/cursos/{id_curso}')
async def putCurso(curso: Curso, id_curso: int):
    try:
        if id_curso in cursos().keys():
            cursos()[id_curso] = curso 
            del curso.id  # para nao aparecer id null
        else:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"O curso informado, id: {id_curso}, nao existe")
    except Exception:
        raise HTTPException(status_code=422, detail="Há campos requeridos que nao foram enviados")
    else:
        return curso
     


# delete methods
@app.delete('/cursos/{id_curso}')
async def deleteCurso(id_curso: int):
    from fastapi import Response
    try:
        if id_curso in cursos().keys():
            del cursos()[id_curso]
        else:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"O curso informado, id: {id_curso}, nao existe")
    except Exception:
        ...
    else:
        return Response(status_code=204)


# teste de query parameters: ?a=1&b=2 etc
@app.get("/soma")
async def calculator(
    a: int = Query(default=None, description="informe um numero maior que 0", gt=0),
    b: int = Query(default=None, description="informe um numero maior que 0", gt=0), 
    c: Optional[int] = None
    ) -> int:
    """
    realiza a soma
    parameters: a , b, c (int)
    return: result (int)
    """
    if c:
        return {"Solution ": a + b + c}
    else:
        return {"Solution ": a + b}


@app.get("/login")
async def login(xuser = Header(default=None, ), token = Header(default=None, )) -> dict[str, str]: # normalmente, os parametros de header sao precedidos por x
    if xuser is None or token is None:
        raise HTTPException(status_code=401, detail=f"Não autorizado")
    return {"user":xuser, "token":token}
 


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, debug=True, reload=True)