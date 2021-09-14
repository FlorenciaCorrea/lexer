alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def a_sino(word): #
	s = 0
	for c in word:
		if s == 0 and c == 's':
			s = 1
		elif s == 1 and c == 'i':
			s = 2
		elif s == 2 and c == 'n':
			s = 3
		elif s == 3 and c == 'o':
			s = 4
		else:
			s = -1
			break
	return s == 4

def a_para(word): #
	s = 0
	for c in word:
		if s == 0 and c == 'p':
			s = 1
		elif s == 1 and c == 'a':
			s = 2
		elif s == 2 and c == 'r':
			s = 3
		elif s == 3 and c == 'a':
			s = 4
		else:
			s = -1
			break
	return s == 4

def a_si (word): #
	s = 0
	for c in word:
		if s == 0 and c == 's':
			s = 1
		elif s == 1 and c == 'i':
			s = 2
		else:
			s = -1
			break
	return s == 2

def a_cte (word): #
	s = 0
	for c in word:
		if s == 0 and c =='c':
			s = 1
		elif s == 1 and c == 't':
			s = 2
		elif s == 2 and c == 'e':
			s = 3
		else:
			s = -1
			break
	return s == 3

def a_desde (word):#
	s = 0
	for c in word:
		if s == 0 and c == 'd':
			s = 1
		elif s == 1 and c == 'e':
			s = 2
		elif s == 2 and c == 's':
			s = 3
		elif s == 3 and c == 'd':
			s = 4
		elif s == 4 and c == 'e':
			s = 5
		else:
			s = -1
			break
	return s == 5

def a_hasta (word):#
	s = 0
	for c in word:
		if s == 0 and c == 'h':
			s = 1
		elif s == 1 and c == 'a':
			s = 2
		elif s == 2 and c == 's':
			s = 3
		elif s == 3 and c == 't':
			s = 4
		elif s == 4 and c == 'a':
			s = 5
		else:
			s = -1
			break
	return s == 5

def a_entonces (word):#
	s = 0
	for c in word:
		if s == 0 and c == 'e':
			s = 1
		elif s == 1 and c == 'n':
			s = 2
		elif s == 2 and c == 't':
			s = 3
		elif s == 3 and c == 'o':
			s = 4
		elif s == 4 and c == 'n':
			s = 5
		elif s == 5 and c == 'c':
			s = 6
		elif s == 6 and c == 'e':
			s = 7
		elif s == 7 and c == 's':
			s = 8
		else:
			s = -1
			break
	return s == 8

def a_mostrar (word):#
	s = 0
	for c in word:
		if s == 0 and c == 'm':
			s = 1
		elif s == 1 and c == 'o':
			s = 2
		elif s == 2 and c == 's':
			s = 3
		elif s == 3 and c == 't':
			s = 4
		elif s == 4 and c == 'a':
			s = 5
		elif s == 5 and c == 'r':
			s = 6
		else:
			s = -1
			break
	return s == 6

def a_aceptar (word):#
	s = 0
	for c in word:
		if s == 0 and c == 'a':
			s = 1
		elif s == 1 and c == 'c':
			s = 2
		elif s == 2 and c == 'e':
			s = 3
		elif s == 3 and c == 'p':
			s = 4
		elif s == 4 and c == 't':
			s = 5
		elif s == 5 and c == 'a':
			s = 6
		elif s == 6 and c == 'r':
			s = 7
		else:
			s = -1
			break
	return s == 7

def a_num (word):
	s = 0  
	for c in word:
		if s == 0 and (c in numeros):
			s = 1
		elif s == 1 and (c in numeros):
			s = 1
		elif s == 1 and (c in alfabeto):
			s = -1
			break
		else:
			s = -1
			break		
	return s == 1

def a_id (word):
	s = 0
	for c in word:
		if s == 0 and (c in alfabeto):
			s = 1
		elif s == 1 and (c in alfabeto):
			s = 1
		else:
			s = -1
			break
	return s == 1


def a_paropen (word):
	s = 0
	for c in word:
		if s == 0 and c == '(':
			s = 1
		else :
			s = -1
			break
	return s == 1

def a_parclose (word):
	s = 0
	for c in word:
		if s == 0 and c == ')':
			s = 1
		else:
			s = -1
			break
	return s == 1

def a_llaveop (word):
	s = 0
	for c in word :
		if s == 0 and c == '{':
			s = 1
		else:
			s = -1
			break
	return s == 1

def a_llaveclose (word):
	s = 0
	for c in word :
		if s == 0 and c == '}':
			s = 1
		else:
			s = -1
			break
	return s == 1

def a_coma(word):
	s = 0
	for c in word:
		if s == 0 and c == ',':
			s = 1
		else:
			s = -1
			break
	return s == 1

def a_puntocoma (word):
	s = 0
	for c in word :
		if s == 0 and c == ';':
			s = 1
		else:
			s = -1
			break
	return s == 1

def a_operadores(word):
	s = 0
	operadores = ['+','*']
	for c in word:
		if s == 0 and (c in operadores):
			s = 1
		else:
			s = -1
			break
	return s == 1

def a_comparacion(word):
	s = 0
	for c in word :
		if s == 0 and c == '=':
			s = 1
		else:
			s = -1
			break
	return s == 1


def a_invalido(word):
	s = 0
	for c in word:
		if s == 0 and c in alfabeto:
			s = 1
		elif s == 1 and c in alfabeto:
			s = 1
		elif s == 1 and c in numeros:
			s = 2
		elif s == 0 and c in numeros:
			s = 3
		elif s == 3 and c in numeros:
			s = 3
		elif s ==3 and c in alfabeto:
			s = 2
		elif s == 2 and (c in alfabeto):
			s = 2
		elif s == 2 and (c in numeros):
			s = 2
		else:
			s = -1
			break
	return s == 2

ttokens = [('SINO', a_sino),
('PARA',a_para),
('SI', a_si),
('CTE', a_cte),
('DESDE',a_desde),
('HASTA', a_hasta),
('ENTONCES',a_entonces),
('MOSTRAR',a_mostrar),
('ACEPTAR',a_aceptar),
('NUM', a_num),
('Id', a_id),
('ParOpen', a_paropen),
('ParClose', a_parclose),
('LlaveOpen', a_llaveop),
('LlaveClose', a_llaveclose),
('Coma', a_coma),
('PuntoComa', a_puntocoma),
('OPMAT', a_operadores),
('COMPARACION', a_comparacion),
('Token no valido', a_invalido)]

def aceptados(word):
	candidatos = []
	for (token, automata) in ttokens:
		if automata(word):
			candidatos.append(token)
	if len(candidatos)>0:
			return (True, candidatos[0])
	else:
		return False

def lex(src):
	tokens = []
	state = 0
	i = 0
	c = ""
	word = ""
	start = 0
	src = src+" "	
	while i < len(src):
		c = src[i]
		word = src[start:i+1]
		if state == 0:
			if c.isspace():
				i+=1
				state = 0
				start = i
			else:
				start = i			
				i+=1
				state = 1
					
		elif state == 1:
			if aceptados(word) and not c.isspace():
				i+=1
				state = 1
			else:
				i-=1
				state = 2
		elif state == 2:
			if not aceptados(word) or a_invalido(word):
				return ("Token no valido", word)
				break
			aux = aceptados(word)
			agregar_token = aux[1]
			tokens.append((agregar_token, word))
			i+=1
			state = 0
			start = i		
	return tokens	

