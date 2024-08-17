import datetime

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

def header_certificado(junior):
    HEADER = f"""
        <p><strong>{junior['razao_social']}</strong></p>
        <p><strong>{junior['cnpj']}</strong></p>
        <p><strong>{junior['area_atuacao']}</strong></p>
        """
    return HEADER



def text_certificado(parametros):
    # Formatação das datas
    data_inicio = datetime.datetime.strptime(parametros['data_in'], '%Y-%m-%d').strftime('%d de %B de %Y')
    data_fim = datetime.datetime.strptime(parametros['data_fim'], '%Y-%m-%d').strftime('%d de %B de %Y')

    # Pluralização das horas
    horas_plural = "horas" if int(parametros['horas']) > 1 else "hora"

    # Texto do certificado com formatação básica
    TEXT_CERTIFICADO = f"""
    <p><strong>Certificado</strong></p>
    <p>Este certificado é concedido a {parametros['nome']}, portador(a) da matrícula nº {parametros['matricula']}, em reconhecimento à sua participação como {parametros['funcao']} na Byte Seridó Júnior.</p>
    <p>O(A) voluntário(a) dedicou {parametros['horas']} {horas_plural} semanais (SEGUNDA A SEXTA) no período de {data_inicio} a {data_fim} na {parametros['ie']}, totalizando {parametros['tt_hrs']} horas.</p>
    <p>Caicó-RN, {datetime.date.today().strftime('%d de %B de %Y')}</p>
    """
    return TEXT_CERTIFICADO