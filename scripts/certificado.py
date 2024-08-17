import datetime

from ej.models import EmpresasJuinior

parametros = {
    "nome": 'nome',
    "matricula": 'mat',
    "funcao": 'fun',
    "horas": 'hrs',
    "data_in": 'in',
    "data_fim": 'fim',
    "id": 'ie',
    "tt_hrs": 'hr'
}

def header_certificado(ej):
    HEADER = f"""
        <p><strong>Nome: {ej.razao_social}</strong></p>
        <p><strong>CNPJ: {ej.cnpj}</strong></p>
        <p><strong>Area de atuação: {ej.area_atuacao}</strong></p>
        """
    return HEADER



def text_certificado(voluntario, historico, ej):
    # Formatação das datas
    data_inicio = historico.data_Inicio
    data_fim = historico.data_fim

    if data_fim is None:
        data_fim = datetime.date.today()

    horas = 20
    horas_plural = "horas" if horas > 1 else "hora"
    total_hrs = 20 * ((data_fim - data_inicio).days // 7)

    # Texto do certificado com formatação básica
    TEXT_CERTIFICADO = f"""
    <p><strong>Certificado</strong></p>
    <p>Este certificado é concedido a {voluntario.nome}, portador(a) da matrícula nº {voluntario.matricula}, em reconhecimento à sua participação como {historico.funcao} na Byte Seridó Júnior.</p>
    <p>O(A) voluntário(a) dedicou {horas} {horas_plural} semanais (SEGUNDA A SEXTA) no período de {data_inicio} a {data_fim} na {ej.razao_social}, totalizando {total_hrs} horas.</p>
    <p>Caicó-RN, {datetime.date.today().strftime('%d de %B de %Y')}</p>
    """
    return TEXT_CERTIFICADO

def footer_certificado(chave,ej):

    FOOTER = f"""

        <p><strong>{ej.representante_legal}</strong></p>
        <p>Diretor(a) Presidente</p>
        <p>Chave de autenticação: {chave}</p>
        <p>Acesse: byteseridojr/certificados/buscar/ </p>
        <p>Digite a cheve no campo buscar para validação. </p>
        """
    return FOOTER