import layout
import wx
import matplotlib.pyplot as plt

def funci():
	funcionário=dict()
	funcionário["nome"]= input('qual o nome ?')
	funcionário["idade"]= valint("digite um inteiro : ")

def valint(msg):
	numero = input(msg)
	while numero(num):
		numero=input("deu ERRO digite um número inteiro : ")
	return int(numero)


def num(n):
	if n in '0123456 789.,':
		return True
	else :
		return False

def apresenta(classe):
	app = wx.App()
	frame=classe(None)
	frame.Show()
	app.MainLoop()

def separa(dados):
	porcentagem=list()
	serviço=list()
	for x in dados:
		x["tots"]=list()
		for y in x['vetor']:
			y.split()
			y[0]=float(y[0])
			x["tots"].append(y[0])
			y[1]=float(y[1])
			y[0]=y[0]*(y[1]/100)
			serviço.append(float(y[0]))
		x["serviços"]=serviços[:]
		serviços.clear()
		x["totalserv"]=0 
		for y in x["vetor"]:
			x["totalserv"]+=y

	return dados



def funçãofoda(nomes):
	y=0
	grupo=list()
	vetfun=list()
	funcionario=dict()
	for x in range(len(nomes)):
		nomes[x] = nomes[x].replace(" \n",'')
	print (nomes)

	for x in range(len(nomes)):
		x=y
		if not nomes[x][0].isnumeric() :
			grupo.clear()
			funcionario.clear()
			funcionario["nome"]=nomes[x]
			if x+1 < len(nomes):
				x=x+1
				i=nomes[x]
			while i[0].isnumeric() :
				if x+1 < len(nomes):
					x+=1
					grupo.append(nomes[x-1])
					i=nomes[x]
				else:
					grupo.append(nomes[x])
					break
								
			funcionario["vetor"]=grupo[:]
			vetfun.append(funcionario.copy())
			y=x
		if x == len(nomes)-1:
			break
	return vetfun
def vet(vetN):
	y=0
	grupo=list()
	vetfun=list()
	funcionario=dict()
	for x in range(len(vetN)):
		x=y
		if not vetN[x][0].isnumeric() :
			grupo.clear()
			funcionario.clear()
			funcionario["nome"]=vetN[x]
			if x+1 < len(vetN):
				x=x+1
				i=vetN[x]
			while i[0].isnumeric() :
				if x+1 < len(vetN):
					x+=1
					grupo.append(vetN[x-1])
					i=vetN[x]
				else:
					grupo.append(vetN[x])
					break
							
		funcionario["vetor"]=grupo[:]
		vetfun.append(funcionario.copy())
		y=x
		if x == len(vetN)-1:
			break
	return vetfun

def vetfunn(vetfun):
	porcentagem=list()
	serviço=list()
	for x in vetfun:
		x['VS']=list()	
		x['porcentagem']=list()	
		x["tots"]=list()	
		x['money']=0	
		x['quantserv']=len(x['vetor'])	
		for o in x['vetor']:
			k=o.split()
			x['VS'].append(float(k[0]))
			x["tots"].append(float(k[0]))
			x['porcentagem'].append(float(k[1]))
		x["totalserv"]=0 
		for o in range(len(x["vetor"])): 
			x['money']+=x['VS'][o]*(x['porcentagem'][o])/100 
			x["totalserv"]+=x['VS'][o]-(x['VS'][o]*x['porcentagem'][o])/100
	return vetfun

def mostra(vetfun):
	for c in vetfun:
		print(f'O(a) {c["nome"]} produziu R${(c["totalserv"]+c["money"]):.2f}\nR${c["totalserv"]:.2f} para o salão \nR${c["money"]:.2f} para ele(a) \n{c["quantserv"]} serviços feitos')



def GrafBar(txt,vetfun,analise):
	plt.title(txt)
	for x in range(len(vetfun)):
		plt.bar(x,vetfun[x][analise],label=vetfun[x]["nome"])
	plt.legend()
	plt.show()