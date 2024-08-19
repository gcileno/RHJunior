import datetime

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

    horas = 20
    horas_plural = "horas" if horas > 1 else "hora"
    total_hrs = 20 * ((data_fim - data_inicio).days // 7)

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