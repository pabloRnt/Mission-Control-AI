import random

pontos_risco = 0

ciclos = 6
infos = 5

temperatura_critica = 35
temperatura_atencao = 33

comunicacao_critica = 30
comunicacao_atencao = 65

bateria_critica = 20    
bateria_atencao = 50

oxigenio_critica = 80
oxigenio_atencao = 90

estabilidade_critica = 40
estabilidade_atencao = 65

dados_missao = [[0] * infos for i in range(ciclos)]
for i in range (ciclos):
    for j in range(infos):
        dados_missao[i][j] = random.randint(0,40)

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistemas de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

def analisar_temperatura(ciclo):
    if dados_missao[ciclo][0] >= 35:
        return pontos_risco + 2
    elif dados_missao[ciclo][0] < temperatura_critica and dados_missao[ciclo][0] >= temperatura_atencao:
        return pontos_risco + 1
    else:
        return pontos_risco

def analisar_comunicacao(ciclo):
    if dados_missao[ciclo][1] >= 35:
        return pontos_risco + 2
    elif dados_missao[ciclo][1] > comunicacao_critica and dados_missao[ciclo][1] <= comunicacao_atencao:
        return pontos_risco + 1
    else:
        return pontos_risco

def analisar_bateria(ciclo):
    if dados_missao[ciclo][2] >= 35:
        return pontos_risco + 2
    elif dados_missao[ciclo][2] > bateria_critica and dados_missao[ciclo][2] <= bateria_atencao:
        return pontos_risco + 1
    else:
        return pontos_risco
    
def analisar_oxigenio(ciclo):
    if dados_missao[ciclo][3] >= 35:
        return pontos_risco + 2
    elif dados_missao[ciclo][3] > oxigenio_critica and dados_missao[ciclo][3] <= comunicacao_atencao:
        return pontos_risco + 1
    else:
        return pontos_risco

def analisar_estabilidade(ciclo):
    if dados_missao[ciclo][4] >= 35:
        return pontos_risco + 2
    elif dados_missao[ciclo][4] >estabilidade_critica and dados_missao[ciclo][4] <= estabilidade_atencao:
        return pontos_risco + 1
    else:
        return pontos_risco

def classificar_ciclo(ciclo):
    pontos_risco = sum([
        analisar_temperatura(ciclo),
        analisar_comunicacao(ciclo),
        analisar_bateria(ciclo),
        analisar_oxigenio(ciclo),
        analisar_estabilidade(ciclo)
    ])

    if pontos_risco >= 0 and pontos_risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontos_risco >= 3 and pontos_risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    elif pontos_risco >= 6 and pontos_risco <= 10:
        return "MISSÃO CRÍTICA"

def analisar_tendencia(ciclo):
    return 0

def identificar_area_mais_afetada(ciclo):
    pontos_area = []
    pontos_area.append(analisar_temperatura(ciclo))
    pontos_area.append(analisar_comunicacao(ciclo))
    pontos_area.append(analisar_bateria(ciclo))
    pontos_area.append(analisar_oxigenio(ciclo))
    pontos_area.append(analisar_estabilidade(ciclo))
    
    maior_pontuacao = max(pontos_area)
    indices_areas_mais_afetadas = [i for i, x in enumerate(pontos_area) if x == maior_pontuacao]
    
    areas = ""

    for indice in indices_areas_mais_afetadas:
        areas += areas_monitoradas[indice] + ", "
    return areas

def gerar_recomendacao(ciclo):
    return 0

def gerar_relatorio_final(ciclo):
    return 0

for i in range(ciclos):
    print(f"============= CICLO {i+1} =============")
    print(f"Status da missão: {classificar_ciclo(i)}")
    print(f"Área(s) de maior risco: {identificar_area_mais_afetada(i)}")
    print("")