from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from ej.models import Voluntario, HistoricoMembro, EmpresasJuinior
from certificados.models import Certificados

from scripts.certificado import header_certificado, footer_certificado, text_certificado


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
        vol = certificados.historico_membro.voluntario

        context = {"certificados": certificados, "voluntario":vol}
        return render(request, self.template_name, context)

#@method_decorator(login_required(login_url='login'), name = 'dispatch')
class EmitirCertificadoView(LoginRequiredMixin,View):

    def get(self, request, certificado_id):
        
        ej = EmpresasJuinior.objects.get(id=1)

        certificado = get_object_or_404(Certificados, id=certificado_id)

        historico = certificado.historico_membro

        vol = Voluntario.objects.get(id=historico.voluntario.id)

                # Verifica se o usuário logado é o proprietário do certificado
        if certificado.historico_membro.voluntario.user != request.user:
            return HttpResponseForbidden("Você não tem permissão para acessar este certificado.")
        

        context = {
            'header':header_certificado(ej),
            'body':text_certificado(vol,historico,ej),
            'footer': footer_certificado(certificado.autenticacao, ej),
        }
        return render(request, 'emitir_certificado.html', context)
    