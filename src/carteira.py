def alocar(perfil: int, pos: float = 15, pre: float = 15, caixa: float = 15,
           FII: float = 15, acoes: float = 15, ativosi: float = 15, bitcoin: float = 10):
    """
    Define os percentuais de alocação da carteira de acordo com o perfil do investidor.

    Perfis pré-definidos (0, 1 e 2) usam pesos fixos calibrados para um investidor
    com foco em cripto. O perfil 3 (Customizável) usa os percentuais informados
    manualmente via parâmetros.

    Args:
        perfil (int): Perfil do investidor. 0 = Conservador, 1 = Mediano,
            2 = Arrojado, 3 = Customizável.
        pos (float): Percentual em Pós Fixado (usado apenas no perfil Customizável).
        pre (float): Percentual em Pré Fixado (usado apenas no perfil Customizável).
        caixa (float): Percentual em Caixa (usado apenas no perfil Customizável).
        FII (float): Percentual em Fundos Imobiliários (usado apenas no perfil Customizável).
        acoes (float): Percentual em Ações (usado apenas no perfil Customizável).
        ativosi (float): Percentual em Ativos Internacionais (usado apenas no perfil Customizável).
        bitcoin (float): Percentual em Bitcoin (usado apenas no perfil Customizável).

    Returns:
        list[float]: Lista de percentuais de alocação, na ordem definida em
            `dados.categorias` (Pós Fixado, Pré Fixado, Caixa, FII, Ações,
            Ativos Internacionais, Bitcoin).

    Raises:
        ValueError: Se `perfil` não for 0, 1, 2 ou 3.
        ValueError: Se a soma dos percentuais de `taxas` não for exatamente 100.
    """
    
    # Validação do Perfil
    if perfil not in [0, 1, 2, 3]:
        raise ValueError(f"❌ Perfil inválido, selecione um número de 0 até 3.")

    # Alocação de acordo com os perfis
    if perfil == 0:  # Conservador (cripto)
        taxas = [50, 25, 10, 5, 5, 0, 5]
    elif perfil == 1:  # Mediano (cripto)
        taxas = [20, 15, 5, 5, 25, 5, 25]
    elif perfil == 2:  # Arrojado (cripto)
        taxas = [15, 0, 0, 0, 25, 10, 50]
    else:  # Customizável
        taxas = [pos, pre, caixa, FII, acoes, ativosi, bitcoin]

    # Validação das Taxas
    if sum(taxas) != 100 or sum(taxas) > 100 or sum(taxas) < 0:
        raise ValueError(f"❌ Alocação inválida: soma = {sum(taxas)}% (deve ser 100%)")
    
    return taxas