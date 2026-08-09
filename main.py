from src.carteira import alocar, calcularmedia, calcularalocacao, analisar, analise, plotarcarteira

def main():

    # ===============================
    # CONFIGURAÇÕES GERAIS
    # ===============================
    perfil = 1
    investimento = 10000

    # ===============================
    # ANÁLISE DA CARTEIRA
    # ===============================
    alocacao = alocar(perfil)
    nota_carteira = calcularmedia(alocacao)
    analizados = analisar(nota_carteira)

    analise(perfil, nota_carteira, analizados)

    valores, categorias_filtradas = calcularalocacao(investimento, alocacao)
    plotarcarteira(valores, categorias_filtradas, perfil, nota_carteira, analizados)


if __name__ == "__main__":
    main()