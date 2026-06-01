nome_missao = "Mission Orion"
nome_equipe = "Equipe Apollo"
lista_pontos_missao = []

# ==== VALORES MÁXIMOS POR FAIXA ====

temperatura_critica_maxima = 35
temperatura_critica_minima = 18
temperatura_atencao = 33

comunicacao_critica = 30
comunicacao_atencao = 65

bateria_critica = 20    
bateria_atencao = 50

oxigenio_critico = 80
oxigenio_atencao = 90

estabilidade_critica = 40
estabilidade_atencao = 65
        
dados_missao = [
    [28.3, 90, 95, 98.2, 95],
    [30.7, 85, 90, 95.5, 90],
    [31.2, 25, 85, 92.4, 88],
    [33.4, 40, 18, 90.1, 80],
    [35.6, 20, 15, 75.6, 35],
    [32.0, 70, 45, 88.2, 75]
]

numero_ciclos = len(dados_missao)

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistemas de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

ciclos_monitorados = ["início da missão", "estabilização dos sistemas", "queda parcial de comunicação", "alerta de energia", "risco operacional", "tentativa de recuperação"]

# ==== FUNÇÕES DE ANÁLISE ====

def analisar_temperatura(ciclo):
    if dados_missao[ciclo][0] >= temperatura_critica_maxima or dados_missao[ciclo][0] <= temperatura_critica_minima:
        return 2
    elif dados_missao[ciclo][0] < temperatura_critica_maxima and dados_missao[ciclo][0] >= temperatura_atencao:
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
                
# ==== FUNÇÕES DE CÁLCULO ====

def somar_pontos_risco_ciclo(ciclo): # Soma dos pontos de risco de todas as áreas por ciclo
    pontos_risco = sum([
        analisar_temperatura(ciclo),
        analisar_comunicacao(ciclo),
        analisar_bateria(ciclo),
        analisar_oxigenio(ciclo),
        analisar_estabilidade(ciclo)
    ])
    
    return pontos_risco

def calc_media_area_missao(info):
    soma_info_missao = 0
    
    for i in range(numero_ciclos):
        soma_info_missao += dados_missao[i][info]
    return soma_info_missao / numero_ciclos

def calc_media_risco_missao():
    soma_risco_missao = 0
    
    for i in range(numero_ciclos):
        soma_risco_missao += somar_pontos_risco_ciclo(i)
    return soma_risco_missao / numero_ciclos

# ==== FUNÇÕES DE AUXILIARES ====

def pontuacao_para_status(pontos):

    match pontos:
        case 0:
            return "NORMAL"
        case 1:
            return "ATENÇÃO"
        case 2:
            return "CRÍTICO"

def listar_pontos_areas(ciclo): # Pontos de cada área por ciclo
    pontos_area = []
    pontos_area.append(analisar_temperatura(ciclo))
    pontos_area.append(analisar_comunicacao(ciclo))
    pontos_area.append(analisar_bateria(ciclo))
    pontos_area.append(analisar_oxigenio(ciclo))
    pontos_area.append(analisar_estabilidade(ciclo))
    
    return pontos_area

def classificar_ciclo(ciclo): # Retorna status da missão

    pontos_risco = somar_pontos_risco_ciclo(ciclo)

    if 0 <= pontos_risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontos_risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def classificar_missao(risco_medio):
    
    if risco_medio >= 6:
        return "MISSÃO EM ESTADO CRÍTICO"
    elif risco_medio >= 3 and risco_medio <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO ESTÁVEL"

def identificar_area_mais_afetada_ciclo(ciclo):

    pontos_area = listar_pontos_areas(ciclo) # Vetor com pontos de risco de todas as áreas por ciclo

    maior_pontuacao = max(pontos_area)

    if maior_pontuacao == 0:
        return "Nenhuma área com riscos"

    indices_areas_mais_afetadas = [i for i, x in enumerate(pontos_area) if x == maior_pontuacao] # Vetor com índices das áreas mais afetadas

    areas = []

    for indice in indices_areas_mais_afetadas:
        areas.append(areas_monitoradas[indice]) # Adiciona a área mais afetada através do seu índice no vetor de áreas monitoradas

    if len(areas) == 1:
        return areas[0]

    else:
        return ", ".join(areas[:-1]) + " e " + areas[-1] # Se houver empate nos pontos de risco, haverão mais de uma área "mais afetada"

def identificar_ciclo_mais_critico(): 
    
    lista_soma_pontos_ciclo = []
    for i in range(numero_ciclos):
        lista_soma_pontos_ciclo.append(somar_pontos_risco_ciclo(i))
    
    maior_risco_missao = max(lista_soma_pontos_ciclo)
    
    ciclos_criticos = []
    
    indices_ciclos_mais_criticos = [i for i, x in enumerate(lista_soma_pontos_ciclo) if x == maior_risco_missao]
    
    for indice in indices_ciclos_mais_criticos:
        ciclos_criticos.append(str(indice+1))
        
    if len(ciclos_criticos) == 1:
        return ciclos_criticos[0]

    else:
        return ", ".join(ciclos_criticos[:-1]) + " e " + ciclos_criticos[-1]

def numero_ciclos_criticos():
    quantidade_ciclos_criticos = 0

    for i in range(numero_ciclos):
        if classificar_ciclo(i) == "MISSÃO CRÍTICA":
            quantidade_ciclos_criticos += 1
    
    return quantidade_ciclos_criticos

def analisar_tendencia_ciclo(ciclo): # Retorna tendência entre um ciclo e o ciclo anterior

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

# ==== FUNÇÕES GENERATIVAS ====

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
            return ", ".join(recomendacoes[:-1]) + " e " + recomendacoes[-1] #Se houver mais de uma recomendação, retorna todas elas formatadas
    
def gerar_relatorio_final():
    
    # == VARIÁVEIS DE PONTOS DE RISCO TOTAL PARA CADA ÁREA ==
    
    soma_temperatura = 0
    soma_comunicacao = 0
    soma_energia = 0
    soma_oxigenio = 0
    soma_estabilidade = 0
    
    # =======================================================

    for i in range(numero_ciclos):
        pontos_area = listar_pontos_areas(i) # Vetor com pontos de risco de todas as áreas por ciclo

        soma_temperatura += pontos_area[0]
        soma_comunicacao += pontos_area[1]
        soma_energia += pontos_area[2]
        soma_oxigenio += pontos_area[3]
        soma_estabilidade += pontos_area[4]
        
 
        
    # == IDENTIFICAR TENDÊNCIA DA MISSÃO ==
    
    risco_inicial_missao = somar_pontos_risco_ciclo(0) # Retorna o risco do primeiro ciclo
    risco_final_missao = somar_pontos_risco_ciclo(numero_ciclos-1) # Retorna o risco do último ciclo

    if risco_final_missao == risco_inicial_missao:
        tendencia =  "Estável"

    elif risco_final_missao > risco_inicial_missao:
        tendencia = "Piora"

    else:
        tendencia = "Melhora"
    
    # == IDENTIFICAR ÁREA MAIS AFETADA NA MISSÃO ==
    
    pontuacoes = [
    soma_temperatura,
    soma_comunicacao,
    soma_energia,
    soma_oxigenio,
    soma_estabilidade
    ]
    
    maior_pontuacao = max(pontuacoes)

    indices_areas_mais_afetadas = [i for i, x in enumerate(pontuacoes) if x == maior_pontuacao]

    areas_mais_afetadas_missao = [areas_monitoradas[indice] for indice in indices_areas_mais_afetadas]
    
    print("============================================== RELATÓRIO FINAL ==============================================")
    
    print("")
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {numero_ciclos}")
    print("")
    
    if len(areas_mais_afetadas_missao) == 1:
        print(f"A área mais afetada da missão foi {areas_mais_afetadas_missao[0]} com {maior_pontuacao} pontos")

    else:
        texto_areas = (", ".join(areas_mais_afetadas_missao[:-1]) + " e " + areas_mais_afetadas_missao[-1])
        print(f"As áreas mais afetadas da missão foram: {texto_areas} com {maior_pontuacao} pontos")
        
    print("")
    print(f"- Tendência geral da missão: {tendencia}")
    print(f"- Risco do primeiro ciclo da missão: {risco_inicial_missao} pontos")
    print(f"- Risco do último ciclo da missão: {risco_final_missao} pontos")
    print("")
    
    print("-- Pontuação acumulada por área --")
    
    print("")
    print(f"- Temperatura interna: {soma_temperatura} pontos de risco na missão")
    print(f"- Comunicação com a base: {soma_comunicacao} pontos de risco na missão")
    print(f"- Sistemas de energia: {soma_energia} pontos de risco na missão")
    print(f"- Suporte de oxigênio: {soma_oxigenio} pontos de risco na missão")
    print(f"- Estabilidade operacional: {soma_estabilidade} pontos de risco na missão")
    print("")
    print(f"- Ciclo mais crítico: Ciclo {identificar_ciclo_mais_critico()}")
    
    lista_soma_pontos_ciclo = []
    for i in range(numero_ciclos):
        lista_soma_pontos_ciclo.append(somar_pontos_risco_ciclo(i))
    
    maior_risco_missao = max(lista_soma_pontos_ciclo)
    
    print(f"- Maior pontuação de risco: {maior_risco_missao}")
    print(f"- Risco médio da missão: {calc_media_risco_missao()}")
    print(f"- Quantidade de ciclos críticos: {numero_ciclos_criticos()}")
    print("")
    
    print("-- Média de dados de cada área --")
    print("")
    print(f"- Média de temperatura: {calc_media_area_missao(0):.2f} ºC")
    print(f"- Média de comunicação: {calc_media_area_missao(1):.2f}%")
    print(f"- Média de bateria: {calc_media_area_missao(2):.2f}%")
    print(f"- Média de oxigênio: {calc_media_area_missao(3):.2f}%")
    print(f"- Média de estabilidade: {calc_media_area_missao(4):.2f}%")
    
    
    print("")
    print(f"Classificação final da missão: {classificar_missao(calc_media_risco_missao())}")
    print("")
    
    print("CONCLUSÃO: ")
    print("A missão Mission Orion apresentou instabilidades ao longo dos ciclos monitorados, com seu momento mais crítico ocorrendo no Ciclo 5, ")
    print("que atingiu 10 pontos de risco. As áreas mais afetadas foram Comunicação com a Base e Sistemas de Energia, ambas com 5 pontos acumulados. ")
    print("Apesar da tendência geral de piora da missão, observou-se uma recuperação parcial no último ciclo, reduzindo o risco para 2 pontos. Com risco ")
    print("médio de 3,0 pontos e classificação final de MISSÃO EM ATENÇÃO, recomenda-se manter o monitoramento dos sistemas de comunicação e energia para ")
    print("prevenir novas ocorrências críticas.")
    print("==================================================================================================================================================")

# ==== REGISTRO DE CICLOS ====

print("=======================================================================================================================")
print("MISSION CONTROL AI")
print("=======================================================================================================================")
print("")
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {numero_ciclos}")
print("")

for i in range(numero_ciclos):
    lista_pontos_missao.append(somar_pontos_risco_ciclo(i))
    
    print(f"============================================== CICLO {i+1}: {ciclos_monitorados[i].upper()} ==============================================")
    print("")
        
    print(f"- Temperatura interna: {dados_missao[i][0]} °C | {pontuacao_para_status(analisar_temperatura(i))}")
    print(f"- Comunicação com a base: {dados_missao[i][1]} % | {pontuacao_para_status(analisar_comunicacao(i))}")
    print(f"- Sistemas de energia: {dados_missao[i][2]} % | {pontuacao_para_status(analisar_bateria(i))}")
    print(f"- Suporte de oxigênio: {dados_missao[i][3]} % | {pontuacao_para_status(analisar_oxigenio(i))}")
    print(f"- Estabilidade operacional: {dados_missao[i][4]} % | {pontuacao_para_status(analisar_estabilidade(i))}")
    
    print("")
    
    print(f"- Análise de tendência entre esse ciclo e o último: {analisar_tendencia_ciclo(i)}")
    print("")
    print(f"- Pontuação de risco do ciclo: {somar_pontos_risco_ciclo(i)}")
    print(f"- Classificação do ciclo: {classificar_ciclo(i)}")
    print(f"- Área(s) de maior risco: {identificar_area_mais_afetada_ciclo(i)}")
    print("")
    print(f"- Recomendações: {gerar_recomendacao(i)}")
    print("")

# ==== RELATÓRIO FINAL ====

gerar_relatorio_final()