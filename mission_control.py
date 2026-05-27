import random

ciclos = 6
infos = 5

temperatura_critica = 35
temperatura_atencao = 33

comunicacao_critica = 30
comunicacao_atencao = 65

bateria_critica = 20    
bateria_atencao = 50

oxigenio_critico = 80
oxigenio_atencao = 90

estabilidade_critica = 40
estabilidade_atencao = 65

'''dados_missao = [[0] * infos for i in range(ciclos)]
for i in range (ciclos):
    for j in range(infos):
        dados_missao[i][j] = random.randint(0, 100)'''
        
dados_missao = [
    [28, 90, 95, 98, 95],
    [30, 85, 90, 95, 90],
    [31, 25, 85, 92, 88],
    [33, 40, 18, 90, 80],
    [37, 20, 15, 75, 35],
    [32, 70, 45, 88, 75]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistemas de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

ciclos_monitorados = ["início da missão", "estabilização dos sistemas", "queda parcial de comunicação", "alerta de energia", "risco operacional", "tentativa de recuperação"]

def analisar_temperatura(ciclo):
    if dados_missao[ciclo][0] >= temperatura_critica:
        return 2
    elif dados_missao[ciclo][0] < temperatura_critica and dados_missao[ciclo][0] >= temperatura_atencao:
        return 1
    else:
        return 0

def analisar_comunicacao(ciclo):
    if dados_missao[ciclo][1] <= comunicacao_critica:
        return 2
    elif dados_missao[ciclo][1] > comunicacao_critica and dados_missao[ciclo][1] <= comunicacao_atencao:
        return 1
    else:
        return 0

def analisar_bateria(ciclo):
    if dados_missao[ciclo][2] <= bateria_critica:
        return 2
    elif dados_missao[ciclo][2] > bateria_critica and dados_missao[ciclo][2] <= bateria_atencao:
        return 1
    else:
        return 0
    
def analisar_oxigenio(ciclo):
    if dados_missao[ciclo][3] <= oxigenio_critico:
        return 2
    elif dados_missao[ciclo][3] > oxigenio_critico and dados_missao[ciclo][3] <= oxigenio_atencao:
        return 1
    else:
        return 0

def analisar_estabilidade(ciclo):
    if dados_missao[ciclo][4] <= estabilidade_critica:
        return 2
    elif dados_missao[ciclo][4] >estabilidade_critica and dados_missao[ciclo][4] <= estabilidade_atencao:
        return 1
    else:
        return 0

def somar_pontos_risco_ciclo(ciclo):
    pontos_risco = sum([
        analisar_temperatura(ciclo),
        analisar_comunicacao(ciclo),
        analisar_bateria(ciclo),
        analisar_oxigenio(ciclo),
        analisar_estabilidade(ciclo)
    ])
    
    return pontos_risco

def classificar_ciclo(ciclo):

    pontos_risco = somar_pontos_risco_ciclo(ciclo)

    if 0 <= pontos_risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontos_risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def analisar_tendencia(ciclo):

    if ciclo == 0:
        return "Sem histórico"

    risco_atual = somar_pontos_risco_ciclo(ciclo)
    risco_anterior = somar_pontos_risco_ciclo(ciclo - 1)

    if risco_atual == risco_anterior:
        return "Estável"

    elif risco_atual > risco_anterior:
        return "Piora"

    else:
        return "Melhora"
    
def identificar_area_mais_afetada(ciclo):
    pontos_area = []
    pontos_area.append(analisar_temperatura(ciclo))
    pontos_area.append(analisar_comunicacao(ciclo))
    pontos_area.append(analisar_bateria(ciclo))
    pontos_area.append(analisar_oxigenio(ciclo))
    pontos_area.append(analisar_estabilidade(ciclo))
    
    maior_pontuacao = max(pontos_area)
    if maior_pontuacao == 0:
        return "Nenhuma área com riscos"

    indices_areas_mais_afetadas = [
        i for i, x in enumerate(pontos_area) if x == maior_pontuacao]
    
    areas = []

    for indice in indices_areas_mais_afetadas:
        areas.append(areas_monitoradas[indice])
        
    else: 
        if len(areas) == 1:
            return areas[0]
        else: 
            return ", ".join(areas[:-1]) + " e " + areas[-1]

def gerar_recomendacao(ciclo):
    recomendacoes = []
    
    if analisar_temperatura(ciclo) == 2:
        recomendacoes.append("verificar controle térmico")
    
    if analisar_comunicacao(ciclo) == 2:
        recomendacoes.append("restabelecer contato com a base")
    
    if analisar_bateria(ciclo) == 2:
        recomendacoes.append("ativar modo de economia de energia")
    
    if analisar_oxigenio(ciclo) == 2:
        recomendacoes.append("acionar protocolo de suporte à vida")
        
    if analisar_estabilidade(ciclo) == 2:
        recomendacoes.append("reduzir operações não essenciais")
    
    if not recomendacoes:
        return "Nenhuma ação necessária"
    else: 
        if len(recomendacoes) == 1:
            return recomendacoes[0]
        else: 
            return ", ".join(recomendacoes[:-1]) + " e " + recomendacoes[-1]
    
def gerar_relatorio_final(ciclo):
    return 0

for i in range(ciclos):
    print(f"============================================== CICLO {i+1}: {ciclos_monitorados[i].upper()} ==============================================")
    print("")
    print(f"- Status da missão: {classificar_ciclo(i)}")
    print(f"- Área(s) de maior risco: {identificar_area_mais_afetada(i)}")
    print(f"- Análise de tendência: {analisar_tendencia(i)}")
    print(f"- Recomendações: {gerar_recomendacao(i)}")
    print("")