# Definindo as categorias, perfis e cenarios
categorias = ['Pós Fixado','Pré Fixado','Caixa','Fundos Imobiliários','Ações','Ativos Internacionais','Bitcoin']
perfis = {0:'Conservador', 1:'Mediano', 2:'Arrojado', 3:'Customizável'}
cenarios = {0:'Cenário Estável', 1:'Cenário Base', 2:'Cenário Pessimista'}

# Notas dos Cenários
notas = [
    # Cenário Estável — Juros estáveis ou em leve queda, previsibilidade
    ['Bom', 'Médio', 'Médio', 'Médio', 'Médio', 'Médio', 'Ruim'],

    # Cenário Base — Juros já caíram o que tinham de cair, neutralidade
    ['Ruim', 'Bom', 'Péssimo', 'Médio', 'Bom', 'Médio', 'Muito Bom'],

    # Cenário Pessimista — Fim de ciclo, juros subindo, choque
    ['Muito Bom', 'Ruim', 'Bom', 'Ruim', 'Muito Ruim', 'Muito Ruim', 'Péssimo']
]

conversao_notas = {
    'Péssimo': 0,
    'Muito Ruim': 1,
    'Ruim': 2,
    'Médio': 3,
    'Bom': 4,
    'Muito Bom': 5
}

for i in range(len(notas)):
    for j in range(len(notas[i])):
        notas[i][j] = conversao_notas[notas[i][j]]