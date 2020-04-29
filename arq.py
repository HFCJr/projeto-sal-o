from datetime import date

def escarq (nome,name):
	with open(nome,"a+") as file: 
		file.write(f"{name} \n")
	return

def lerarq(nome):
	with open(nome,"r+") as file: 
		fila=file.readlines()
		for x in range(len(fila)):
			fila[x] = fila[x].replace(" \n",'')
	return fila
def excluirn(nome,NAME):
	linhas=lerarq(nome)
	for x in linhas:
		if NAME in x :
			x.replace("\n","")
			linhas.remove(x)

	with open(nome,"w+") as file: 
		for x in linhas:
			file.write(f'{x}')

def sala(vet,tot):
	total=0
	with open(f'banco/{date.today()}.txt',"w+") as file :
		for c in vet:
			total+=c["totalserv"]
			file.write(f'O(a) Funcionário(a) {c["nome"]} produziu R${(c["totalserv"]+c["money"]):.2f}\nR${c["totalserv"]:.2f} para o salão \nR${c["money"]:.2f} para ele(a) \n{c["quantserv"]} serviços feitos\n')

		file.write(f'O salão produziu {total:.2f} no total gerando {total-tot:.2f} de lucro.')
	

