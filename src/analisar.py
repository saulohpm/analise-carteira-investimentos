from . import dados

def nota(medias):
    """
    Traduz as médias numéricas de cada cenário em uma classificação textual.

    Args:
        medias (list[float]): Médias ponderadas (0 a 5) de adequação da carteira
            para cada cenário, na ordem definida em `dados.cenarios`.

    Returns:
        list[str]: Frases descrevendo a adequação da carteira em cada cenário
            (ex: "Carteira Frágil no Cenário Estável"), na mesma ordem de `medias`.
    """

    analizados = []

    for k in range(len(medias)):
        if medias[k] < 2:
            analizado = f"Carteira Frágil no {dados.cenarios[k]}"
        elif medias[k] < 3:
            analizado = f"Carteira Neutra no {dados.cenarios[k]}"
        elif medias[k] < 4:
            analizado = f"Carteira Resiliente no {dados.cenarios[k]}"
        else:
            analizado = f"Carteira muito adequada para o {dados.cenarios[k]}"

        analizados.append(analizado)

    return analizados


def sensibilidade(perfil, medias, analizados):
    """
    Imprime no console um resumo da análise da carteira.

    Exibe o perfil escolhido, a nota da carteira em cada cenário, a classificação
    textual correspondente e um aviso sobre a natureza das notas (adequação, não
    retorno financeiro).

    Args:
        perfil (int): Perfil do investidor (0 a 3), usado para buscar o nome em
            `dados.perfis`.
        medias (list[float]): Médias ponderadas (0 a 5) de adequação da carteira
            para cada cenário.
        analizados (list[str]): Classificações textuais retornadas por `analisar`.

    Returns:
        None
    """

    print(f"\nO perfil escolhido foi: {dados.perfis[perfil]}\n")

    for i in range(len(medias)):
        print(f"Carteira nota {medias[i]} de 5, no {dados.cenarios[i]}!")

    print("")
    for a in analizados:
        print(a)

    print(
        "\nOBS: Estas notas não representam retorno financeiro, "
        "mas adequação da carteira ao cenário macroeconômico"
    )