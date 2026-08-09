from src import analisar, calcular, carteira, grafico

def main():

    # ===============================
    # CONFIGURAÇÕES GERAIS
    # ===============================
    perfil = 1
    investimento = 10000

    # ===============================
    # ANÁLISE DA CARTEIRA
    # ===============================
    alocacao = carteira.alocar(perfil)
    nota_carteira = calcular.media(alocacao)
    analizados = analisar.nota(nota_carteira)

    analisar.sensibilidade(perfil, nota_carteira, analizados)

    valores, categorias_filtradas = calcular.alocacao(investimento, alocacao)
    grafico.plotar_carteira(valores, categorias_filtradas, perfil, nota_carteira, analizados)


if __name__ == "__main__":
    main()