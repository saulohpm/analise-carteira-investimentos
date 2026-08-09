from . import dados

def media(taxas):
    """
    Calcula a média ponderada de adequação da carteira para cada cenário macroeconômico.

    Para cada cenário em `dados.notas`, pondera a nota de cada classe de ativo
    pelo percentual alocado (`taxas`) e normaliza pela soma das taxas.

    Args:
        taxas (list[float]): Percentuais de alocação por classe de ativo, na
            ordem definida em `dados.categorias`.

    Returns:
        list[float]: Média ponderada (0 a 5) de adequação da carteira para
            cada cenário, na ordem definida em `dados.cenarios`.
    """

    medias = []

    for j in range(len(dados.notas)):
        calculo = 0
        for i in range(len(taxas)):
            calculo += taxas[i] * dados.notas[j][i]
        media = round(calculo / sum(taxas), 2)
        medias.append(media)

    return medias


def alocacao(investimento: float, taxas):
    """
    Converte os percentuais de alocação em valores monetários por classe de ativo.

    Ativos com alocação igual a zero são descartados do resultado (não aparecem
    nem no gráfico nem na legenda). Imprime no console o valor alocado em cada
    classe de ativo com alocação positiva.

    Args:
        investimento (float): Valor total do patrimônio a ser alocado, em reais.
        taxas (list[float]): Percentuais de alocação por classe de ativo, na
            ordem definida em `dados.categorias`.

    Returns:
        tuple[list[float], list[str]]: Tupla contendo:
            - valores: valores em reais alocados em cada classe de ativo (apenas
              as com alocação > 0).
            - categorias_filtradas: nomes das classes de ativo correspondentes,
              na mesma ordem de `valores`.
    """

    valores = []
    categorias_filtradas = []

    for i in range(len(dados.categorias)):
        percentual = taxas[i] / 100
        alocacao = investimento * percentual

        if alocacao > 0:
            print(f"{dados.categorias[i]} → R$ {alocacao:,.2f}")
            categorias_filtradas.append(dados.categorias[i])
            valores.append(alocacao)

    return valores, categorias_filtradas