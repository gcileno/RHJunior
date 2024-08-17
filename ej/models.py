from django.db import models
from django.contrib.auth.models import User

STATUS_VOLUNTARIO = (
    ('ATIVO','Ativo'),
    ('DESLIGADO', 'Desativado')
)

class EmpresasJuinior(models.Model):
    razao_social = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18)  # Use CharField para CNPJ
    inscricao_estadual = models.CharField(max_length=20)
    
    representante_legal = models.CharField(max_length=100)
    cpf_representante_lega = models.CharField(max_length=11)
    
    area_atuacao = models.CharField(max_length=100)
    site = models.URLField(blank=True)  
    fundacao = models.DateField()
    info_contato = models.ForeignKey("Informacoes", blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):

        return f'{self.razao_social}'
    

class Funcao(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    
    voluntario_lider = models.ForeignKey(
        'Voluntario', 
        on_delete=models.SET_NULL,
        blank= True, 
        null=True, 
        related_name='lider_departamento')

    
    def __str__(self):
        return self.nome

class Informacoes(models.Model):
    rua = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return f"Informacoes #{self.pk}"
    #f'Id-{self.voluntario.informacoes_voluntario.id}'
    
class Voluntario(models.Model):
    
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    status_civil = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    informacoes_voluntario = models.ForeignKey(Informacoes, on_delete=models.CASCADE, null=True,blank=True)

    matricula = models.CharField(max_length=20, unique=True)
    ies = models.CharField(max_length=50, null=True, blank=True)
    
    nome_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    
    data_entrada = models.DateField(null=True, blank=True)
    data_saida = models.DateField(null=True, blank=True)
    
    periodo_entrada = models.CharField(max_length=50)
    periodo_saida = models.CharField(max_length=50, null=True, blank=True)

    status = models.CharField(max_length=9, choices= STATUS_VOLUNTARIO, default='CANDIDATO')

    def user_create(self):
        if self.user is None:
            self.user = User.objects.create(
                first_name=self.nome,
                username=self.matricula,
                password=self.matricula
            )
            self.user.set_password(self.matricula)
            self.user.save()
        else:
            self.user.first_name = self.nome
            self.user.username = self.matricula
            self.user.set_password(self.matricula)
            self.user.save()

            self.user = self.user

    def __str__(self):
        return f'{self.nome}'


class HistoricoMembro(models.Model):
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE, blank=True, null=True, related_name="historico")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, null=True, blank=True)
    data_Inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    observacao = models.TextField()

    def __str__(self):
        return f'{self.voluntario.matricula} {self.voluntario.nome} - {self.funcao.nome}'
    
class AnaliseDesempenho(models.Model):
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE, blank=True, null=True, related_name='analises')
    assiduidade = models.IntegerField()
    colaboracao = models.IntegerField()
    tarefas = models.IntegerField()
    cooperacao = models.IntegerField()
    realizacao_metas = models.IntegerField()

    data = models.DateField()
