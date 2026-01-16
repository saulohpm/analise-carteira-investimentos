from carteira import (alocar, calcularmedia, calcularalocacao, analisar, analise, plotarcarteira)

from cdb import calcularcdb, plotarcdb

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

    # ===============================
    # SIMULAÇÃO CDB
    # ===============================
    periodo = 12 * 5
    CDI = 14.32
    CDB = 100
    capital = 20000
    aportes = 1500

    MCDB, MCDI, caixa, Mliq, t = calcularcdb(periodo, CDI, CDB, capital, aportes)

    plotarcdb(MCDB, MCDI, caixa, Mliq, t)


if __name__ == "__main__":
    main()