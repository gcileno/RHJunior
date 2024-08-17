from ej.models import Departamento

def create():
    departamentos = [
        'Marketing', 'Financeiro', 'Recursos Humanos', 'Desenvolvimento', 'Direção Geral'
    ]

    for nome in departamentos:
        new_funcao, created = Departamento.objects.get_or_create(nome=nome)
        if created:
            print(f"Novo departamento'{nome}")
        else:
            print(f"O Departamento: '{nome}' já existe no banco de dados.")