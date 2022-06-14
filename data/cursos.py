courses = {
        1: {
            'nome': 'Curso1',
            'aulas': 222,
            'horas': 30,
        },

        2: {
           'nome': 'Curso2',
            'aulas': 233,
            'horas': 40,
        },
}

def cursos() -> dict:
    # funcao que funciona como uma tabela de banco de dados
    return courses 
