import matplotlib.pyplot as plt
import dados

def alocar(
    perfil: int,
    pos: float = 15, pre: float = 15, caixa: float = 15,
    FII: float = 15, acoes: float = 15, ativosi: float = 15, bitcoin: float = 10):

    # Validação do Perfil
    if perfil not in [0, 1, 2, 3]:
        raise ValueError(f"❌ Perfil inválido, selecione um número de 0 até 3.")

    # Alocação de acordo com os perfis
    if perfil == 0:  # Conservador
        taxas = [50, 35, 10, 0, 4, 0, 1]
    elif perfil == 1:  # Mediano
        taxas = [30, 30, 0, 0, 20, 0, 20]
    elif perfil == 2:  # Arrojado
        taxas = [10, 10, 0, 10, 30, 0, 40]
    else:  # Customizável
        taxas = [pos, pre, caixa, FII, acoes, ativosi, bitcoin]

    # Validação das Taxas
    if sum(taxas) != 100 or sum(taxas) > 100 or sum(taxas) < 0:
        raise ValueError(f"❌ Alocação inválida: soma = {sum(taxas)}% (deve ser 100%)")
    
    return taxas


def calcularmedia(taxas):

    # Medias
    medias = []

    for j in range(len(dados.notas)):
        calculo = 0
        for i in range(len(taxas)):
            calculo += taxas[i] * dados.notas[j][i]
        media = round(calculo / sum(taxas), 2)
        medias.append(media)
    
    return medias


def calcularalocacao(investimento: float, taxas):

    # Distribuição da Carteira e alocação do patrimonio
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


def analisar(medias):

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


def analise(perfil, medias, analizados):

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


def plotarcarteira(valores, categorias_filtradas, perfil, medias, analizados):

    plt.figure(figsize=(12, 6))

    plt.pie(
        valores,
        labels=[f"R$ {v:,.0f}" for v in valores],
        startangle=90,
        autopct='%1.1f%%'
    )

    plt.text(
        -3.25, 1,
        f"Perfil: {dados.perfis[perfil]}\n\n"
        f"Notas nos cenários:\n\n"
        f"Estável -> {medias[0]}\n"
        f"Base -> {medias[1]}\n"
        f"Pessimista -> {medias[2]}\n\n"
        f"Análise de Carteira:\n\n"
        f"{analizados[0]}\n"
        f"{analizados[1]}\n"
        f"{analizados[2]}",
        fontsize=10,
        va='top',
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.25)
    )

    plt.title("Alocação da Carteira de Investimentos")
    plt.legend(
        categorias_filtradas,
        title="Ativos",
        loc="center left",
        bbox_to_anchor=(1.2, 0.5)
    )

    plt.show()