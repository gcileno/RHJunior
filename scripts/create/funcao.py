from ej.models import Funcao

def create():
    funcoes = [
        'Desenvolvedor Back-end', 'Desenvolvedor Front-end',
        'Desenvolvedor Full-Stack', 
        'Auxiliar Direção e Gestão', 'Auxiliar de Recursos Humanos',
        'Auxiliar Financeiro', 'Auxiliar de Marketing',
        'Auxiliar de Desenvolvimento',
        'Diretor Marketing', 'Diretor Financeiro',
        'Diretor de Desenvolvimento', 'Diretor de RH',
        'Diretor Geral'
    ]

    for nome in funcoes:
        new_funcao, created = Funcao.objects.get_or_create(nome=nome)
        if created:
            print(f"Função '{nome}' cadastrada com sucesso!")
        else:
            print(f"Função '{nome}' já existe no banco de dados.")
