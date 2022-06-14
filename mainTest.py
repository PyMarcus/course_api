from starlette.testclient import TestClient 
from main import app
from data.cursos import cursos


client = TestClient(app)


# teste para o método get em main
def testMainGetRootStatusCode() -> None:
    response = client.get('/')
    assert response.status_code == 200 


def testMainGetCourses() -> None:
    response = client.get('/cursos')
    assert response.json() == cursos()


def testMainGetCoursesId() -> None:
    response = client.get("/cursos/1")
    assert response.json() == cursos()['1']
    