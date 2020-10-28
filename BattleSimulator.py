#GUSTAVO SIMOES, 95588

                 ####################################
                 #############TAD posicao############
                 ####################################

def cria_posicao(x,y): #R[POSICAO] = TUPLO COM 2 NUMEROS NATURAIS
 '''
 -----------cria_posicao------------------------
 -ARGUMENTOS: X,Y -> NUMEROS NATURAIS
 -DEVOLVE UM TUPLO CORRESPONDENTE A POSICAO
 -CASO OS ARGUMENTOS SEJAM INVALIDOS, DARA ERRO
 -----------------------------------------------
 '''
 if eh_posicao((x,y)):
  return (x,y)
 else:
  raise ValueError('cria_posicao: argumentos invalidos')
 
def cria_copia_posicao(p):
 '''
 -----------cria_copia_posicao-------
 -ARGUMENTOS: POSICAO (VALIDA)
 -DEVOLVE UMA COPIA DA POSICAO DADA
 ------------------------------------
 ''' 
 return cria_posicao(obter_pos_x(p), obter_pos_y(p))

def obter_pos_x(p):
 '''
 -----------obter_pos_x---------------------
 -ARGUMENTOS: POSICAO
 -DEVOLVE A COORDENADA DA POS NO EIXO DOS x
 -------------------------------------------
 '''  
 return p[0]

def obter_pos_y(p):
 '''
 -----------obter_pos_y---------------------
 -ARGUMENTOS: POSICAO
 -DEVOLVE A COORDENADA DA POS NO EIXO DOS Y
 -------------------------------------------
 '''   
 return p[1]

def eh_posicao(arg):
 '''
 -----------eh_posicao------------------------
 -ARGUMENTOS: QUALQUER
 -RETORNA SE O ARGUMENTO DADO E OU NAO POSICAO
 --------------------------------------------- 
 '''
 if not isinstance(arg, tuple): #verifica se e tuplo
  return False
 elif len(arg) != 2: #Nao pode ter 3 coordenadas
  return False
 elif type(obter_pos_x(arg)) != int or type(obter_pos_y(arg)) != int: #As coordenadas tem de ser inteiras
  return False
 elif obter_pos_x(arg) < 0 or obter_pos_y(arg) < 0: #As coordenadas nao podem ser negativas
  return False
 else:
  return True
 
def posicoes_iguais(p1, p2):
 '''
 -----------posicoes_iguais----------------------
 -ARGUMENTOS: DUAS POSICOES
 -RETORNA SE AS POSICOES DADAS SAO OU NAO IGUAIS
 ------------------------------------------------ 
 ''' 
 return cria_posicao(obter_pos_x(p1), obter_pos_y(p1)) == cria_posicao(obter_pos_x(p2), obter_pos_y(p2))

 
def posicao_para_str(p):
 '''
 -----------posicao_para_str---------------------
 -ARGUMENTOS: POSICAO 
 -RETORNA SE AS POSICOES DADAS SAO OU NAO IGUAIS
 ------------------------------------------------ 
 '''  
 return '(' + str(obter_pos_x(p)) + ', ' + str(obter_pos_y(p)) + ')' 

def obter_posicoes_adjacentes(p): 
 '''
 -----------obter_posicoes_adjacentes--------------
 -ARGUMENTOS: P
 -DEVOLVE UM TUPLO DE POSICOES CORRESPONDENTES AS 
 POSICOES ADJACENTES A POSICAO DADA
 --------------------------------------------------
 ''' 
 adj_filtrado = () 
 adj_todos = ((obter_pos_x(p), obter_pos_y(p)-1), (obter_pos_x(p)-1, obter_pos_y(p)), (obter_pos_x(p)+1, obter_pos_y(p)), (obter_pos_x(p), obter_pos_y(p)+1))
 for i in adj_todos: #Percorrer todas as possiveis posicoes adjacents 
  if eh_posicao(i): #Caso a posicao seja valida, soma-se a mesma ao tuplo final de posicaoes adjacentes
   adj_filtrado += (i,)
 return adj_filtrado

                 ####################################
                 ##########TAD unidade###############
                 ####################################

def cria_unidade(p, v, f, strg): #R[UNIDADE] = DICIONARIO COM 2 ENTRADAS, LISTA COM OS SEUS ATRIBUTOS (VIDA E FORCA) E TUPLO COM A SUA POSICAO
 '''
 -----------cria_unidade---------------------------
 -ARGUMENTOS: P,V,F (TUPLOS) STRG (STRING)
 -RECEBE OS ARGUMENTOS DADOS, VALIDANDO-OS E CASO
 SENDO VALIDOS, CONSTROI UMA UNIDADE
 --------------------------------------------------
 '''  
 dic = { strg: [v,f], '@': p }
 if not eh_unidade(dic): #Utiliza-se a funcao definida mais a frente para auxiliar a validacao da unidade
  raise ValueError('cria_unidade: argumentos invalidos') 
 else: 
  return dic #Se for unidade, devolve a unidade na representacao escolhida

def cria_copia_unidade(u):
 '''
 -----------cria_copia_unidade---------------------
 -ARGUMENTOS: U (UNIDADE)
 -RECEBE UMA UNIDADE E CRIA UMA COPIA DA MESMA
 --------------------------------------------------
 '''  
 return cria_unidade(obter_posicao(u), obter_vida(u), obter_forca(u), obter_exercito(u)) #Utiliza-se as funcoes definidas mais a frente para auxiliar a criacao da copia

def obter_posicao(u):
 '''
 -----------obter_posicao--------------------------
 -ARGUMENTOS: U (UNIDADE)
 -RECEBE UMA UNIDADE E DEVOLVE A SUA POSICAO
 --------------------------------------------------
 '''   
 return u['@']

def obter_exercito(u):
 '''
 -----------obter_exercito---------------------
 -ARGUMENTOS: U (UNIDADE)
 -RECEBE UMA UNIDADE E DEVOLVE O SEU EXERCITO
 ----------------------------------------------
 '''   
 for key in u.keys(): #Percorro todas as chaves da unidade, guardando a string que contem o nome do exercito
  if key != '@':    
   return key

def obter_forca(u):
 '''
 -----------obter_forca---------------------
 -ARGUMENTOS: U (UNIDADE)
 -RECEBE UMA UNIDADE E DEVOLVE A SUA FORCA
 -------------------------------------------
 '''   
 return u[obter_exercito(u)][1]

def obter_vida(u):
 '''
 -----------obter_vida---------------------
 -ARGUMENTOS: U (UNIDADE)
 -RECEBE UMA UNIDADE E DEVOLVE A SUA VIDA
 ------------------------------------------
 '''   
 return u[obter_exercito(u)][0]

def muda_posicao(u,p):
 '''
 -----------muda_posicao-----------------------
 -ARGUMENTOS: U (UNIDADE) P (POSICAO)
 -RECEBE UMA UNIDADE E UMA POSICAO, ALTERANDO
 A POSICAO EM QUE SE ENCONTRA, DEVOLVENDO A
 PROPRIA UNIDADE
 ----------------------------------------------
 '''    
 u['@'] = p
 return u

def remove_vida(u, v):
 '''
 -----------remove_vida-------------------------
 -ARGUMENTOS: U (UNIDADE) V (VIDA)
 -RECEBE UMA UNIDADE E VIDA, ALTERANDO DESTRUTI
 VAMENTE A MESMA, SUBTRAINDO A VIDA DADA A VIDA 
 ATUAL DA PROPRIA UNIDADE
 -----------------------------------------------
 '''   
 u[obter_exercito(u)][0] = obter_vida(u) - v
 return u

def eh_unidade(arg):
 '''
 -----------eh_unidade---------------------------
 -ARGUMENTOS: UNIVERSAL
 -RECEBE UM ARGUMENTO UNIVERSAL, RETORNA SE ESTE
 E UMA UNIDADE OU NAO (BOOLEANO)
 -------------------------------------------------
 '''    
 if type(arg) != dict: #Se nao for dicionario (nao cumpre a representacao definida pelo utilizador)
  return False
 elif len(arg) != 2: #Apenas pode ter a lista de atributos e a posicao
  return False
 elif not eh_posicao(obter_posicao(arg)): #A posicao tem de ser valida
  return False
 elif obter_vida(arg) <= 0 or type(obter_vida(arg)) != int: #A vida nao pode ser negativa, 0, ou um numero nao inteiro
  return False
 elif obter_forca(arg) <= 0 or type(obter_forca(arg)) != int: #Idem para a forca
  return False
 elif type(obter_exercito(arg)) != str: #O nome do exercito tem de ser um string nao vazio
  return False
 elif obter_exercito(arg) == '':
  return False
 else:
  return True
 
def unidades_iguais(u1, u2):
 '''
 -----------unidades_iguais----------------------
 -ARGUMENTOS: DUAS UNIDADES
 -AVALIA SE AS UNIDADES DADAS SAO OU NAO IGUAIS
 (BOOLEANO)
 ------------------------------------------------ 
 '''  
 return cria_copia_unidade(u1) == cria_copia_unidade(u2)
 
def unidade_para_char(u):
 '''
 -----------unidade_para_char--------------------
 -ARGUMENTOS: UNIDADE
 -RECEBE UMA UNIADDE E DEVOLVE A PRIMEIRA LETRA
 DO SEU EXERCITO EM MAIUSCULA
 ------------------------------------------------ 
 '''  
 nome = obter_exercito(u)
 for char in nome: #Percorro os caracteres pertencentes a string do exercito associado a unidade
  if (ord(char) >= 65 and ord(char) <= 90):  #Se for um caracter ASCII maisculo, devolver o caracter
   return str(chr(ord(char)))
  if (ord(char) >= 97 and ord(char) <= 122): #Se for um caracter ASCII minusculo, devolver o caracter maisculo (encontrado 32 indices atras)
   return str(chr(ord(char) - 32))

def unidade_para_str(u):
 '''
 -----------unidade_para_str----------------------
 -ARGUMENTOS: UNIDADE
 -RECEBE UMA UNIDADE E DEVOLVE A SUA REPRESENTACAO
 EXTERNA (NO FORMATO STRING)
 ------------------------------------------------ 
 '''   
 return unidade_para_char(u) + str([obter_vida(u), obter_forca(u)]) + '@' + str(obter_posicao(u))

def unidade_ataca(u1, u2):
 '''
 -----------unidade_para_str------------------------
 -ARGUMENTOS: UNIDADES
 -RECEBE DUAS UNIDADES, REALIZA UM ATAQUE, AVALIANDO
 SE A UNIDADE FOI ELIMINADA OU NAO (BOOLEANO)
 --------------------------------------------------- 
 '''   
 vida_un = obter_vida(u2)
 if obter_vida(remove_vida(u2, obter_forca(u1))) <= 0:
  del[u2]
  return True
 else:
  return False
 
def ordenar_unidades(t): 
 '''
 -----------ordenar_unidades---------------------
 -ARGUMENTOS: TUPLO DE UNIDADES
 -RECEBE UM TUPLO DE UNIDADES E DEVOLVE O MESMO
 TUPLO ORDENADO CONFORME A ORDEM DE LEITURA DO 
 LABIRINTO
 ------------------------------------------------ 
 '''   
 return tuple(sorted(t, key = lambda x: (obter_pos_y(obter_posicao(x)), obter_pos_x(obter_posicao(x))))) 
#Para simplificar o codigo, fiz recurso a funcao built in sorted e as funcoes de ordem superior de modo a fornecer um criterio pelo qual o mapa deve ser ordenado

                      ####################################
                      ##########TAD mapa##################
                      ####################################
 
def cria_mapa(d, w, e1, e2): #R[MAPA] = DICIONARIO COM 4 ENTRADAS, TUPLO COM AS SUAS DIMENSOES, TUPLO COM AS PAREDES INTERIORES, TUPLO CONTENDO AS UNIDADES DE UM EXERCITO, TUPLO CONTENDO AS UNIDADES DE OUTRO EXERCITO
 '''
 -----------cria_mapa----------------------------------
 -ARGUMENTOS: D,W,E1,E2, TUPLOS
 -RECEBE 4 TUPLOS, REPRESENTATIVOS DA DIMENSAO DO MAPA,
 DAS PAREDES PRESENTES DENTRO DO LABIRINTO, E UM TUPLO
 COM UNIDADES DE CADA EXERCITO
 RETORNA UM MAPA CASO OS ARGUMENTOS SEJAM VALIDOS
 ------------------------------------------------------ 
 '''    
 if type(d) != tuple or type(w) != tuple or type(e1) != tuple or type(e2) != tuple: #Se nenhum deles e tuplo
  raise ValueError('cria_mapa: argumentos invalidos')
 if len(d) == 0 or len(d) > 2: #se o tuplo com o mapa contem mais do que 1 tuplo de dimensoes
  raise ValueError('cria_mapa: argumentos invalidos')
 if d[0] < 3 or d[1] < 3: #se o mapa e pelo menos 3x3
  raise ValueError('cria_mapa: argumentos invalidos')
 if len(e1) < 1 or len(e2) < 1: #se os exercitos nao tem unidades
  raise ValueError('cria_mapa: argumentos invalidos')
 if w != ():
  for pos in w:
   if eh_posicao(pos) is False or obter_pos_x(pos) <= 0 or obter_pos_x(pos) >= d[0]-1 or obter_pos_y(pos) <= 0 or obter_pos_y(pos) >= d[1]-1: #se a minha posicao nao e valida, ou se encontra fora do mapa
    raise ValueError('cria_mapa: argumentos invalidos')
 for uni in e1: #idem para as unidades de e1 e e2
  if eh_unidade(uni) is False or eh_posicao(obter_posicao(uni)) is False or obter_pos_x(obter_posicao(uni)) <= 0 or obter_pos_x(obter_posicao(uni)) >= d[0]-1 or obter_pos_y(obter_posicao(uni)) <= 0 or obter_pos_y(obter_posicao(uni)) >= d[1]-1:
   raise ValueError('cria_mapa: argumentos invalidos') 
 for uni in e2:
  if eh_unidade(uni) is False or eh_posicao(obter_posicao(uni)) is False or obter_pos_x(obter_posicao(uni)) <= 0 or obter_pos_x(obter_posicao(uni)) >= d[0]-1 or obter_pos_y(obter_posicao(uni)) <= 0 or obter_pos_y(obter_posicao(uni)) >= d[1]-1:
   raise ValueError('cria_mapa: argumentos invalidos')   

 else:
  return {'d': d, 'w': w, obter_exercito(e1[0]): e1, obter_exercito(e2[0]): e2}
 
def cria_copia_mapa(m):
 '''
 -----------cria_copia_mapa----------------
 -ARGUMENTOS: M (MAPA)
 -RECEBE UM MAPA E CRIA UMA COPIA DO MESMO
 ------------------------------------------
 '''
 d = cria_copia_posicao(obter_tamanho(m)) #Optei por inicializar varios tuplos vazios e ir preenchendo com elementos
 w = ()
 e1 = ()
 e2 = ()
 for pos in obter_paredes(m):
  w += (cria_copia_posicao(pos),)
 for uni in obter_unidades_exercito(m, obter_nome_exercitos(m)[0]):
  e1 += (cria_copia_unidade(uni),)
 for uni in obter_unidades_exercito(m, obter_nome_exercitos(m)[1]):
  e2 += (cria_copia_unidade(uni),)   
 return cria_mapa(d,w,e1,e2)

def obter_tamanho(m):
 '''
 -----------obter_tamanho----------------
 -ARGUMENTOS: M (MAPA)
 -RECEBE UM MAPA E DEVOLVE O TUPLO QUE 
 CONTEM AS SUAS DIMENSOES
 ----------------------------------------
 ''' 
 return m['d']

def obter_nome_exercitos(m):
 '''
 -----------obter_nome_exercitos-------------
 -ARGUMENTOS: M (MAPA)
 -RECEBE UM MAPA E DEVOLVE UM TUPLO ORDENADO
 (POR ORDEM ALFABETICA) CONTENDO OS NOMES DOS
 EXERCITOS DAS UNIDADES
 --------------------------------------------
 '''  
 res = ()
 keys = m.keys()
 for key in keys:
  if key != 'd' and key != 'w':  #optei por iterar pelas chaves do dicionario, removendo-as se o seu nome nao correspondesse aos possiveis nomes do exercito
   res += (key,)
 return tuple(sorted(res))

def obter_paredes(m):
 '''
 -----------obter_paredes--------------------
 (FUNCAO ADICIONAL)
 -ARGUMENTOS: M (MAPA)
 -RECEBE UM MAPA E DEVOLVE UM TUPLO CONTENDO 
 AS POSICOES DAS PAREDES PRESENTES DENTRO DO
 MAPA
 --------------------------------------------
 '''   
 return m['w']


def obter_unidades_exercito(m, e):
 '''
 -----------obter_unidades_exercito-----------
 -ARGUMENTOS: M (MAPA), E (EXERCITO)
 -RECEBE UM MAPA E UM EXERCITO, DEVOLVENDO AS 
 UNIDADES DO EXERCITO DADO COMO ARGUMENTO, 
 ORDENADAS POR ORDEM DE LEITURA DO LABIRINTO
 ---------------------------------------------
 '''   
 return ordenar_unidades(m[e])

def obter_todas_unidades(m):
 '''
 -----------obter_todas_unidades--------------
 -ARGUMENTOS: M (MAPA)
 -RECEBE UM MAPA E  DEVOLVE TODAS AS UNIDADES 
 ORDENADAS POR ORDEM DE LEITURA DO LABIRINTO
 ---------------------------------------------
 '''    
 return ordenar_unidades(obter_unidades_exercito(m, obter_nome_exercitos(m)[0]) + obter_unidades_exercito(m, obter_nome_exercitos(m)[1])) 

def obter_unidade(m, p):
 '''
 -----------obter_unidade---------------------
 -ARGUMENTOS: M (MAPA), P (POSICAO)
 -RECEBE UM MAPA E UMA POSICAO, DEVOLVE A 
 UNIDADE PRESENTE NA POSICAO DADA
 ---------------------------------------------
 '''    
 for dic in obter_todas_unidades(m):
  if obter_posicao(dic) == p:
   return dic
   
def eliminar_unidade(m, u):
 '''
 -----------eliminar_unidade------------------
 -ARGUMENTOS: M (MAPA), U (UNIDADE)
 -RECEBE UM MAPA E UMA UNIDADE, ELIMINANDO
 A UNIDADE DADA COMO ARGUMENTO
 ---------------------------------------------
 '''  
 newtup = ()
 for un in m[obter_exercito(u)]: #decidi criar um tuplo novo, eliminando a unidade dada como argumento fazendo recurso a um ciclo
  if un != u:
   newtup += (un,)
 m[obter_exercito(u)] = newtup
 return m

def mover_unidade(m, u, p):
 '''
 -----------mover_unidade-----------------------
 -ARGUMENTOS: M (MAPA), U (UNIDADE), P (POSICAO)
 -RECEBE UM MAPA, UMA UNIDADE E UMA POSICAO, 
 MOVE A UNIDADE DADA PARA A POSICAO DADA
 -----------------------------------------------
 '''   
 obter_unidade(m,obter_posicao(u))['@'] = p
 return m     

def eh_posicao_unidade(m, p):
 '''
 -----------eh_posicao_unidade-------------------
 -ARGUMENTOS: M (MAPA), P (POSICAO)
 -RECEBE UM MAPA, E UMA POSICAO E AVALIA SE A 
 UNIDADE PRESENTE NA POSICAO DADA E VALIDA (BOOL)
 ------------------------------------------------
 '''    
 return eh_unidade((obter_unidade(m, p)))

def eh_posicao_corredor(m,p): 
 '''
 -----------eh_posicao_corredor-------------------
 -ARGUMENTOS: M (MAPA), P (POSICAO)
 -RECEBE UM MAPA, E UMA POSICAO E AVALIA SE A 
 POSICAO CORRESPONDE A UM CORREDOR (BOOL)
 ------------------------------------------------
 '''     
 if eh_posicao_parede(m, p):
  return False
 else:
  return p not in obter_paredes(m)

def eh_posicao_parede(m,p):
 '''
 -----------eh_posicao_parede-------------------
 -ARGUMENTOS: M (MAPA), P (POSICAO)
 -RECEBE UM MAPA, E UMA POSICAO E AVALIA SE A 
 POSICAO CORRESPONDE A UMA PAREDE (BOOL)
 ------------------------------------------------
 '''     
 if obter_pos_x(p) == 0 or obter_pos_x(p) == obter_tamanho(m)[0]-1:  #se x igual a 0 ou a x-1
  return True
 elif obter_pos_y(p) == 0 or obter_pos_y(p) == obter_tamanho(m)[1]-1:  #idem para y
  return True
 else:
  return False
 
def mapas_iguais(m1, m2):
 '''
 -----------mapas_iguais----------------------
 -ARGUMENTOS: DOIS MAPAS
 -AVALIA SE OS MAPAS DADOS SAO OU NAO IGUAIS
 (BOOLEANO)
 ------------------------------------------------ 
 '''   
 return cria_copia_mapa(m1) == cria_copia_mapa(m2)
   
def mapa_para_str(m):
 '''
 -----------mapa_para_str----------------------
 -ARGUMENTOS: MAPA
 -RECEBE UM MAPA E DEVOLVE A SUA REPRESENTACAO
 EXTERNA (NO FORMATO STRING)
 ------------------------------------------------ 
 '''    
 mapa_print = [] #decidi criar uma lista com o mapa a ser 
 mapa_final = '' 
 todas_posicoes = ()
 for uni in obter_todas_unidades(m): #comeco por obter todas as unidades presentes no mapa, iterando por cada uma e obtendo a sua posicao
  pos = obter_posicao(uni)
  todas_posicoes += (pos,)
 for y in range(obter_tamanho(m)[1]): #apos cada linha, adiciono um newline de forma a criar paragrafos no mapa
  mapa_linha = []
  for x in range(obter_tamanho(m)[0]):
   if (x,y) in todas_posicoes:  #itero pelas posicoes, verificando se e unidade, corredor, parede interna ou externa, atribuindo lhes o caracter para cada caso, somando no final ao mapa print
    if eh_unidade(obter_unidade(m, (x,y))): 
     mapa_linha += [unidade_para_char(obter_unidade(m, (x,y)))]      
   elif eh_posicao_corredor(m, (x,y)):
    mapa_linha += ['.'] 
   else:
     mapa_linha += ['#']
  mapa_print += mapa_linha
  mapa_print += ['\n']
 for it in mapa_print: #por fim, itero pela lista formada, criando assim a string final
  mapa_final += it
 return(mapa_final[:-1]) #retiro o ultimo newline

def obter_inimigos_adjacentes(m, u):
 '''
 -----------obter_inimigos_adjacentes----------------
 -ARGUMENTOS: MAPA (M), UNIDADE (U)
 -RECEBE UM MAPA E UMA UNDADE, DEVOLVENDO OS INIMIGOS 
 ADJACENTES A UNIDADE DADA (TUPLO)
 ----------------------------------------------------
 '''    
 tup_inimigos = ()
 for pos in obter_posicoes_adjacentes(obter_posicao(u)):
  if eh_unidade(obter_unidade(m ,pos)):
   if obter_exercito(u) != obter_exercito(obter_unidade(m,pos)):  
    tup_inimigos += (obter_unidade(m,pos),)
  
 return ordenar_unidades(tup_inimigos)
  
def obter_movimento(mapa, unit): 
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo  
    if obter_inimigos_adjacentes(mapa, unit):    
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)
        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    
    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)
   
def calcula_pontos(m, s):
 '''
 -----------calcula_pontos---------------------------
 -ARGUMENTOS: MAPA (M), STRING (S)
 -RECEBE UM MAPA E UMA STRING CORRESPONDENTE AO NOME
 DE UM DOS EXERCITOS, E DEVOLVE A SUA PONTUACAO (SOMA 
 TOTAL DOS PONTOS DE VIDA)
 ----------------------------------------------------
 '''   
 soma= 0
 for uni in obter_unidades_exercito(m, s):
  soma += obter_vida(uni)
 return soma

def simula_turno(m):
 '''
 -----------simula_turno-----------------------------------
 -ARGUMENTOS: M (MAPA)
 -RECEBE UM MAPA E SIMULA UM TURNO COMPLETO, REALIZANDO
 NAS DEVIDAS CONDICOES OS MOVIMENTOS E ATAQUES DAS UNIDADES
 ----------------------------------------------------------
 '''   
 todas_uni = obter_todas_unidades(m)
 for uni in todas_uni:
  if obter_vida(uni) > 0:
   mover_unidade(m, uni,obter_movimento(m,uni)) #realizo o movimento se a unidade nao estiver morta
   in_adj = obter_inimigos_adjacentes(m, uni)
   if in_adj != ():
    uni_n = unidade_ataca(uni, in_adj[0]) #se tiver inimigos adjacentes realiza um ataque, se a unidade for eliminada, e apagada do mapa
    if uni_n is True :
     eliminar_unidade(m, in_adj[0])
  else:
    eliminar_unidade(m, uni)
 return m   


def simula_batalha(strg, boole):
 '''
 -----------simula_batalha-----------------------------------------
 -ARGUMENTOS: STRING , BOOLE (BOOLEANO)
 -REQUER O FICHEIRO DE CONFIGURACAO (CONFIG.TXT)
 -RECEBE UM FICHEIRO DE OPERACAO E UM VALOR BOOLEANO CORRESPONDENTE
 AO MODO DE OPERACAO (TRUE = VERBOSO, FALSE = QUIET) E SIMULA
 UMA BATALHA COMPLETA, DEVOLVENDO OS MAPAS E O RESULTADO
 FINAL
 ------------------------------------------------------------------
 '''    
 cfg = open(strg)
 d = eval(cfg.readline())
 ex1 = eval(cfg.readline())
 ex2 = eval(cfg.readline())
 w = eval(cfg.readline())
 pos_e1 = eval(cfg.readline())
 pos_e2 = eval(cfg.readline()) #leitura de cada linha do ficheiro de modo a poder obter as informacoes necessarias 
 e1 = () #inicializacao de tuplos vazios que serao preenchidos com os exercitos
 e2= ()
 for pos in pos_e1:
  e1 += (cria_unidade(pos, ex1[1], ex1[2], ex1[0]),)
 for pos in pos_e2:
  e2 += (cria_unidade(pos, ex2[1], ex2[2], ex2[0]),) #preenchimento dos tuplos com as unidades dos exercitos, utilizando as informacoes do ficheiro de configuracao
 m = cria_mapa(d, w, e1, e2)
 nome_e1 = obter_nome_exercitos(m)[0]
 nome_e2 = obter_nome_exercitos(m)[1]
 def ciclo_prints(m, nome_e1, nome_e2):
  print(mapa_para_str(m))
  print('[ ' + nome_e1 + ':' + str(calcula_pontos(m, nome_e1)) + ' ' + nome_e2 + ':' + str(calcula_pontos(m, nome_e2)) + ' ]') #este ciclo corresponde a evolucao da batalha que sera visualizada pelo utilizador
  
 if boole is True: #modo verboso
  
   while calcula_pontos(m, nome_e1) != 0 and calcula_pontos(m, nome_e2) != 0:
    m_pre = cria_copia_mapa(m)
    ciclo_prints(m, nome_e1, nome_e2)
    simula_turno(m)
    if m_pre == m: #se os mapas forem iguais em dois turnos consecutivos
     return 'EMPATE'
    
   ciclo_prints(m, nome_e1, nome_e2)
   simula_turno(m)   
   
   if calcula_pontos(m, nome_e1) == 0: #se e1 morreu primeiro
    return nome_e2
   elif calcula_pontos(m, nome_e2) == 0: #caso contrario
    return nome_e1 
      
 else: #modo quiet
  ciclo_prints(m, nome_e1, nome_e2)
  
  while calcula_pontos(m, nome_e1) != 0 and calcula_pontos(m, nome_e2) != 0:
   m_pre = cria_copia_mapa(m)
   simula_turno(m)
   if m_pre == m:
    ciclo_prints(m, nome_e1, nome_e2)
    return 'EMPATE' #se os mapas forem iguais em dois turnos consecutivos 
  ciclo_prints(m, nome_e1, nome_e2)
  
  if calcula_pontos(m, nome_e1) == 0:
   return nome_e2
  elif calcula_pontos(m, nome_e2) == 0:
   return nome_e1
