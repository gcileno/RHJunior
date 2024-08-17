from django.shortcuts import render
from django.views.generic import View

from certificados.models import Certificados


TEXT_CERTIFICADO = """
    Portador(a) da matrícula nº VOL_MATR, participou como FUNC_NOME da Empresa Júnior de Sistemas de Informação,
    Byte Seridó Júnior, realizando HORAS semanais (SEGUNDA A SEXTA). No período de DATA_IN a DATA_FIM na IE.
    """


class CertificarViews(View):
    template_name = "validar.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
    
    def post(self, request):
        certificados = Certificados.objects.get(autenticacao = request.POST.get("chave"))
        #filtrar certificados via data fim preenchida
        context = {"certificados": certificados}
        return render(request, self.template_name, context)