import os #Libreria del sistema
os.system("cls") #Limpia pantalla
from datetime import datetime #Libreria para la fecha

#           id    prod   stock precio
productos=["001","Aceite",50,4200,      #Listado de los productos
#           0      1     2   3
          "002","Arroz",100,1020,
#           4     5      6   7
          "003","Leche",40,950,
#           8     9     10  11
          "004","Azucar",200,1200]
#           12    13     14   15

#Llenar a mano con unas 30 ventas de diferentes dias, meses y años
folio=107 #para una nueva venta se debe incrementar el folio
#      boleta   fecha     id  cant total
ventas=[100,"10-03-2022","001",1,4200,
        101,"02-03-2020","004",10,12000,
        102,"15-04-2020","003",1,950,
        103,"20-02-2021","002",1,1020,
        104,"21-02-2021","003",2,1900,
        105,"12-03-2021","001",2,8400,
        106,"10-05-2022","002",2,2040,
        107,"11-05-2022","002",10,10200]

#Se debe actualizar el stock 
#Si el stock es 0 no puede vender productos
#Ojo no se puede vender mas de lo que hay en stock
#Menu de ventas (punto de venta)

#Variables
fecha=datetime.now().strftime("%d-%m-%Y") #Le da formato a la fecha
while True: #
        os.system("cls")
        print("PUNTO DE VENTA ",fecha) #Imprime la fecha con el formato ya dado
        print("-----------")
        print("1. Vender")
        print("2. Devolver producto")
        print("3. Ver productos") #Listar producto
        print("4. Listado general de ventas") #Detalle todas las ventas $
        print("5. Listado de ventas por fecha") #Detalle de ventas por fecha $
        print("6. Listado de ventas por mes") #Detalle de ventas por mes $
        print("7. Listado de ventas por año") #Detalle de ventas por año
        print("8. Salir")
        opcion=int(input("Ingrese una opcion[1-8]:")) #Hace que el usuario escoja una opcion
        try:
                if opcion == 1:
                        os.system("cls")
                        print("1. Vender")
                        print("-----------")
                        id=input("Ingrese el id del producto: ")
                        #Mostrar datos del producto
                        i=0
                        sw=0 #No existe el id
                        while i<=len(productos)-4:
                                if productos[i]==id:
                                        sw=1 #Si existe id
                                        print(productos[i+1]," stock ",productos[i+2]," $ ",productos[i+3])
                                        break
                                i=i+4
                        #Preguntar cuantos quiere
                        if sw==1:
                        #Encontrado, existe
                                if productos[i+2]>0:
                                        cantidad=int(input("Ingrese cantidad a comprar: "))
                                        if productos[i+2]>=cantidad:
                                                total=cantidad*productos[i+3]
                                                print("El total a pagar es $",total)

                                                resp=input("Desea comprar este producto s/n: ")
                                                if resp=="s":
                                                        folio=folio+1
                                                        ventas.extend([folio,fecha,str(id),cantidad,total])
                                                        productos[i+2]=productos[i+2]-cantidad
                                                else:
                                                        print("Ok, la compra se anula")
                                        else:
                                                print("Error, la cantidad supera al stock")
                        else:
                        #No existe
                                print("No exite")


                if opcion == 2:
                        os.system("cls")
                        print ("2.Devolver producto")
                        print("-----------")
                        folio=int(input("Ingrese el folio del producto: "))
                        #mostrar datos del producto

                        i=0
                        sw=0 #No exite el id
                        while i<=len(ventas)-5:
                                if ventas[i]== folio:
                                        sw=1 #Si exite el id
                                        print("folio.",ventas[i]," fecha ",ventas[i+1],
                                        " id ",ventas[i+2]," cant. ",ventas[i+3]," $ ",ventas[i+4])
                                        break
                                i=i+5 #Preguntas cuantos quiere
                        if sw==1:
                                #Encontrado exite
                                #Validar que no sea mayor que lo comprado
                                cantidad=int(input("Ingrese cantidad a devolver: "))

                                resp=input("Desea reintegrar la cantidad al stock s/n: ")
                                if resp=="s":
                                        ip=0
                                        while ip<len(productos)-4:
                                                if productos[ip]==ventas[i+2]:
                                                        productos[ip+2]=productos[ip+2]+cantidad
                                                        ventas[i+3]=ventas[i+3]-cantidad
                                                        #Actualizar el total de la boleta...

                                                        print("Datos actualizados...")
                                                        break
                                                ip=ip+1
                                        else:
                                                print("Ok, la devolucion se anula...")
                        else:
                                #No existe
                                print("Error, folio no existe...")



                if opcion == 3:
                        os.system("cls")
                        print("3. Ver producto")
                        print("-----------")

                        i=0
                        print("Id  Productos  Cantidad  Precio")
                        while i<=len(productos)-4:
                                print(productos[i]," ",productos[i+1]," ",productos[i+2]," ",productos[i+3])
                                i=i+4                
                if opcion == 4:
                        os.system("cls")
                        print("4. Listado de ventas por fecha")
                        print("-----------")
                        total=0
                        i=0
                        print("folio fecha  productos cantidad total")
                        while i<=len(ventas)-5:
                                print(ventas[i]," ",ventas[i+2]," ",ventas[i+3]," ",ventas[i+4])
                                total=total+ventas[i+4]
                                i=i+5
                                print("El total de ventas es $",total,"\n")

                if opcion == 5:
                        os.system("cls")
                        print("5.Listado de ventas por mes")
                        print("-----------")
                        total=0
                        miFecha=input("Ingrese fecha dd-mm-yyyy: ")
                        print("\n")
                        i=0
                        print("Folio feha      producto cantidad total")
                        while i<=len(ventas)-5:
                                if ventas[i+1]==miFecha:
                                        print(ventas[i]," ",ventas[i+1]," ",ventas[i+2]," ",ventas[i+3], " ",ventas[i+4])
                                        total=total+ventas[i+4]
                                i=i+5
                        print("El total de ventas es $",total,"\n")

                if opcion == 6:
                        os.system("cls")
                        print("6. Listado de ventas mensuales")
                        print("-----------")
                        total=0
                        mes=input("Ingrese mes de mm-yyyy: ")
                        print("\n")
                        i=0
                        print("folio fecha     producto cantidad total")
                        while i<=len(ventas)-5:
                                fechaVenta=ventas[i+1]
                                if fechaVenta[3:10]==mes:
                                        print(ventas[i]," ",ventas[i+1]," ",ventas[i+2]," ",ventas[i+3], " ",ventas[i+4])
                                        total=total+ventas[i+4]
                                i=i+5
                        print("El total de ventas del anio es $",total,"\n")

                if opcion == 7:
                        os.system("cls")
                        print("6. Listado de ventas anuales")
                        print("-----------")
                        total=0
                        anio=input("Ingrese eñ año yyyy: ")
                        print("\n")
                        i=0
                        print("folio fecha     producto cantidad total")
                        while i<=len(ventas)-5:
                                fechaVenta=ventas[i+1]
                                if fechaVenta[6:10]==anio:
                                        print(ventas[i]," ",ventas[i+1]," ",ventas[i+2]," ",ventas[i+3], " ",ventas[i+4])
                                        total=total+ventas[i+4]
                                i=i+5
                        print("El total de ventas es $",total,"\n")

                if opcion == 8:
                        os.system("cls")
                        print("Salir")
                        break
                if opcion<1 or opcion>8:
                        print("Error ingrese una opcion valida")
        except:
                 print("Error, debe ingresar un valor entre 1-8")
        input("Presione Enter para continuar")       #Frena la ejecucion del ciclo                                 
print("Fin del Menu")
