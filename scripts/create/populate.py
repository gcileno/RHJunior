from scripts.create.objetos import DATA
from ej.models import EmpresaJunior,Funcao, Departamento, EmpresaJunior, Voluntario

def criar_objetos():

    ej_data = DATA["EJ"]
    ej, created = EmpresaJunior.objects.get_or_create(
        razao_social=ej_data["razao_social"],
        cnpj=ej_data["cnpj"],
        inscricao_estadual=ej_data["inscricao_estadual"],

        representante_legal=ej_data["representante_legal"],
        cpf_representante_legal=ej_data["cpf_representante_legal"],
        area_atuacao=ej_data["area_atuacao"],
        site=ej_data["site"],
        fundacao=ej_data["fundacao"]
    )
    if created:
        print(f"Empresa Júnior criada com sucesso.")
    else:
        print(f"Empresa Júnior '{ej.razao_social}' já existe.")

    for obj in DATA["FUNCOES"]:
        funcao, created = Funcao.objects.get_or_create(nome=obj)
        if created:
            print(f"Função '{obj}' criada com sucesso.")
        else:
            print(f"Função '{obj}' já existe.")
    
    for obj in DATA["DEPARTAMENTOS"]:
        departamento, created = Departamento.objects.get_or_create(nome=obj)
        if created:
            print(f"Departamento '{obj}' criado com sucesso.")
        else:
            print(f"Departamento '{obj}' já existe.")

    for vol_data in DATA["VOLUNTARIOS"]:
        from ej.models import Voluntario
        departamento = Departamento.objects.get(nome=vol_data["nome_departamento"])
        voluntario, created = Voluntario.objects.get_or_create(
            nome=vol_data["nome"],
            rg=vol_data["rg"],
            cpf=vol_data["cpf"],
            status_civil=vol_data["status_civil"],
            data_nascimento=vol_data["data_nascimento"],
            matricula=vol_data["matricula"],
            ies=vol_data["ies"],
            nome_departamento=departamento,
            data_entrada=vol_data["data_entrada"],
            periodo_entrada=vol_data["periodo_entrada"],
            status=vol_data["status"]
        )
        if created:
            print(f"Voluntário '{voluntario.nome}' criado com sucesso.")
        else:
            print(f"Voluntário '{voluntario.nome}' já existe.")

def criar_voluntarios():
    
        for vol_data in DATA["VOLUNTARIOS"]:
            from ej.models import Voluntario
            departamento = Departamento.objects.get(nome=vol_data["nome_departamento"])
            voluntario, created = Voluntario.objects.get_or_create(
                nome=vol_data["nome"],
                rg=vol_data["rg"],
                cpf=vol_data["cpf"],
                status_civil=vol_data["status_civil"],
                data_nascimento=vol_data["data_nascimento"],
                matricula=vol_data["matricula"],
                ies=vol_data["ies"],
                nome_departamento=departamento,
                data_entrada=vol_data["data_entrada"],
                periodo_entrada=vol_data["periodo_entrada"],
                status=vol_data["status"]
            )
            if created:
                print(f"Voluntário '{voluntario.nome}' criado com sucesso.")
            else:
                print(f"Voluntário '{voluntario.nome}' já existe.")