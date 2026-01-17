from carteira import (alocar, calcularmedia, calcularalocacao, analisar, analise, plotarcarteira)

def main():
    # ===============================
    # CONFIGURAÇÕES GERAIS
    # ===============================
    perfil = 1
    investimento = 10000

    # ===============================
    # ANÁLISE DA CARTEIRA
    # ===============================
    taxas = alocar(perfil)
    medias = calcularmedia(taxas)
    analizados = analisar(medias)

    analise(perfil, medias, analizados)

    valores, categorias_filtradas = calcularalocacao(investimento, taxas)
    plotarcarteira(valores, categorias_filtradas, perfil, medias, analizados)


if __name__ == "__main__":
    main()
