import datetime
from ej.models import Voluntario, HistoricoMembro

def header_certificado(ej):
    HEADER = f"""
        <p has-text-primary-00><strong> {ej.razao_social}</strong></p>
        <p has-text-primary-00><strong> {ej.cnpj}</strong></p>
        <p has-text-primary-00><strong> {ej.area_atuacao}</strong></p>
        """
    return HEADER



def text_certificado(voluntario, historico, ej):
    # Formatação das datas
    data_inicio = historico.data_Inicio
    data_fim = historico.data_fim

    if data_fim is None:
        data_fim = datetime.date.today()

    horas = 10
    horas_plural = "horas" if horas > 1 else "hora"
    total_hrs = horas * ((data_fim - data_inicio).days // 7)

    # Texto do certificado com formatação básica
    TEXT_CERTIFICADO = f"""
    <p class="title is-5"><strong>Certificado</strong></p>
    <p class="subtitle is-6">Este certificado é concedido a {voluntario.nome}, portador(a) da matrícula nº {voluntario.matricula}, em reconhecimento à sua participação como {historico.funcao} na Byte Seridó Júnior.</p>
    <p class="subtitle is-6">O(A) voluntário(a) dedicou {horas} {horas_plural} semanais (SEGUNDA A SEXTA) no período de {data_inicio} a {data_fim} na {ej.razao_social}, totalizando {total_hrs} horas.</p>
    <p class="subtitle is-6">Caicó-RN, {datetime.date.today().strftime('%d de %B de %Y')}</p>
    """
    return TEXT_CERTIFICADO

def footer_certificado(chave, ej):
    FOOTER = f"""
        <div class="content has-text-centered">
            <p class="title is-5"><strong>{ej.representante_legal}</strong></p>
            <p class="subtitle is-6">Diretor(a) Presidente</p>
            <p class="subtitle is-6">Chave de autenticação: <strong>{chave}</strong></p>
            <p class="subtitle is-6">Acesse: <a href="https://byteseridojr/certificados/buscar/" target="_blank">byteseridojr/certificados/buscar/</a></p>
            <p class="subtitle is-6">Digite a chave no campo buscar para validação.</p>
        </div>
    """
    return FOOTER



class CertificadoHTML:
    def __init__(self, ej, voluntario, historico, chave):
        self.ej = ej
        self.voluntario = voluntario
        self.historico = historico
        self.chave = chave

    def horas(self):
        
        if self.historico.funcao:
            if 'diretor' in self.historico.funcao.nome.lower():
                return 15
            return 10
        return 0
    
    def formatar_datas(self):
        data_inicio = self.historico.data_Inicio
        data_fim = self.historico.data_fim or datetime.date.today()
        return data_inicio, data_fim

    def gerar_certificado(self):
        header = self.header_certificado()
        texto = self.text_certificado()
        footer = self.footer_certificado()
        return f"{header}\n{texto}\n{footer}"

    def header_certificado(self):
        HEADER = f"""
                <div class="hero is-primary">
                    <div class="hero-body">
                        <p class="title">
                        {self.ej.razao_social}
                        </p>
                        <p class="subtitle">
                        CNPJ: {self.ej.cnpj} | Área de atuação: {self.ej.area_atuacao}
                        </p>
                    </div>
                </div>
        """
        return HEADER

    def text_certificado(self):
        data_inicio, data_fim = self.formatar_datas()
        total_hrs = self.horas() * ((data_fim - data_inicio).days // 7)

        # Texto do certificado com formatação básica
        TEXT_CERTIFICADO = f"""
        <div class="box has-background-linear-gradient-info-light">
            
                <h1 class="title is-3 has-text-centered">Certificado de Participação</h1>
            
            <section class="section">
                <p class="subtitle is-6">Certificamos <strong>{self.voluntario.nome}</strong>, portador(a) da matrícula nº {self.voluntario.matricula}, em reconhecimento à sua participação como <strong>{self.historico.funcao}</strong>.</p>
                <p class="subtitle is-6">O(A) voluntário(a) dedicou <strong>{self.horas()} horas semanais</strong> (SEGUNDA A SEXTA) no período de {data_inicio} a {data_fim} na {self.ej.razao_social}, totalizando <strong>{total_hrs} horas</strong>.</p>
            </section>
            
                    <div class="box has-background-white has-text-black has-text-centered">
                        <p><strong>{self.ej.representante_legal}</strong></p>
                        <p>Diretor(a) Presidente</p>
                    </div>
                <p class="has-text-centered">Caicó-RN, {datetime.date.today().strftime('%d de %B de %Y')}</p>
            
        </div>
        """
        return TEXT_CERTIFICADO

    def footer_certificado(self):
        FOOTER = f"""
            <div class="box has-background-primary">
                <div class="box has-background-white has-text-black has-text-centered">
                    <p>Chave de autenticação:</p>
                    <p class="subtitle is-6">{self.chave}</p>
                </div>
                <p class="subtitle is-6">Para validação, acesse: <a href="https://byteseridojr/certificados/buscar/" target="_blank">byteseridojr/certificados/buscar/</a></p>
            </div>
        """
        return FOOTER
