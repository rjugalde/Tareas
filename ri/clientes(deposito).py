#definicion de las clases
class Cuenta:
    numeroCuenta = ""
    saldo = 0
    tipo = "AC"
    referenciaCliente = ""
    referenciaSucursal = ""

    def Depositar(self,p):
        self.saldo = self.saldo + p

    def ImprimirSaldo(self):
        print("El saldo de la cuenta es ",self.saldo)
    
class Persona:
    identificacion = ""
    nombre = ""
    direccion = ""
    telefono = ""
    def Imprima(self):
        print("Identificacion: ",self.identificacion)
        print("Nombre: ",self.nombre)
        print("dir.: ",self.direccion)
        print("tel.: ",self.telefono)

#programa
clientes = []   #lista de clientes
cuentas = []    #lista de cuentas

opcion = " "
while opcion.upper() != "S" :   #se sale hasta que "S"
    print("")
    print("Seleccione una opcion:")
    print("   1.  Ingresar clientes")
    print("   2.  Imprimir clientes")
    print("   3.  Crear cuenta")
    print("   4.  Hacer deposito")
    print("   5.  Imprimir saldo")
    print("   6.  Imprimir lista de cuentas")
    print("   S.  Salir")
    print("")
    opcion = input("   Digite la opcion y presione ENTER -->")
    print("")
    if opcion == "1" :
        p = Persona()
        p.identificacion = input("Digite la identificacion :")
        p.nombre = input("Digite el nombre :")
        p.direccion = input("Digite el direccion :")
        p.telefono = input("Digite el telefono :")
        clientes.append(p)
    elif opcion == "2" :
        print("Lista de clientes :")
        print("-------------------")
        for i in range(len(clientes)):
            clientes[i].Imprima()
    elif opcion == "3" :
        c = Cuenta()
        c.numeroCuenta = input("Digite el numero de cuenta :")
        c.referenciaCliente = input("Digite el cliente dueño :")
        cuentas.append(c)
    elif opcion == "4" :
        #buscar la cuenta y despues si existe, depositar
        cuentaBuscada = input("Ingrese la cuenta para deposito :")
        encontro = -1# no existe
        encontrocliente=-1    #tarea#tarea#tarea#tarea#tarea
##        print(cuentas)
        for i in range(len(cuentas)):
##            print(cuentas[i].numeroCuenta)
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i 
                for j in range(len(clientes)):  #tarea#tarea#tarea#tarea#tarea
                    if clientes[j].identificacion==cuentas[i].referenciaCliente: #tarea#tarea#tarea#tarea
                        encontrocliente=j    #tarea#tarea#tarea
        if encontrocliente != -1 :  #tarea#tarea#tarea
            monto = int(input("Digite el monto del deposito :"))
            
            cuentas[encontro].Depositar(monto)
        else :
            print("La cuenta digitada no existe o no tiene un cliente asociado !!!")
##            print("")
    elif opcion == "5" :
        #buscar la cuenta y despues si existe, depositar
        cuentaBuscada = input("Ingrese la cuenta para deposito :")
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].numeroCuenta == cuentaBuscada :
                encontro = i
        if encontro != -1 :
            cuentas[encontro].ImprimirSaldo()
        else :
            print("La cuenta digitada no existe !!!")
    elif opcion =="6" :
        clienteBuscado = input("Digite la identificacion del cliente :")
        encontro = -1       # no existe
        for i in range(len(cuentas)):
            if cuentas[i].referenciaCliente == clienteBuscado :
                encontro = i
                print("cuenta :",cuentas[i].numeroCuenta)
        if encontro == -1 :
            print("El cliente no tiene cuentas !!!")
        
    else :
        print("Gracias por usar el programa !!!")
        print("Fin")
