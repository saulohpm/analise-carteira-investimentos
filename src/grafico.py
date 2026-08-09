import matplotlib.pyplot as plt
from . import dados

def plotar_carteira(valores, categorias_filtradas, perfil, medias, analizados, tamanho = (16, 8)):
    """
    Gera um gráfico de pizza representando a composição da carteira.

    O gráfico exibe a distribuição percentual dos valores alocados, com uma
    caixa de texto lateral resumindo o perfil escolhido, as notas de adequação
    em cada cenário e a classificação textual correspondente.

    Args:
        valores (list[float]): Valores em reais alocados em cada classe de ativo
            (apenas as com alocação > 0), conforme retornado por `calcularalocacao`.
        categorias_filtradas (list[str]): Nomes das classes de ativo correspondentes
            a `valores`.
        perfil (int): Perfil do investidor (0 a 3), usado para buscar o nome em
            `dados.perfis`.
        medias (list[float]): Médias ponderadas (0 a 5) de adequação da carteira
            para cada cenário (Estável, Base, Pessimista).
        analizados (list[str]): Classificações textuais de cada cenário, conforme
            retornado por `analisar`.
        tamanho (tuple[int, int]): Dimensões da figura (largura, altura) em polegadas.
            Padrão: (16, 8).

    Returns:
        None
    """

    plt.figure(figsize=tamanho)

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