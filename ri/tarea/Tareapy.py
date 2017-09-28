def LeerArchivos(FilePath):
	ListaSalida=[]
	with open("ArchivosEntrada/"+FilePath+".txt", 'r') as csvfile:
		func_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
		for row in func_reader:
			ListaSalida+=[row]
	return ListaSalida





#####################################
def LoopFuncionarios():
        ListaFuncionarios=LeerArchivos("Funcionarios")
        while True:
                pass

