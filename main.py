import xml.etree.ElementTree as ET
from NodoCelda import Celda
from ListaCelda import ListaC
from NodoPaciente import pacienten
from ListarPasiente import passiente



#C:\Users\USER\Desktop\Prueba1.xml

def cargarXML(root):

    for elemento in root:
        for datos in elemento.findall('.//paciente/datospersonales'):
            nombre=datos.text
            print(nombre)

parar=False


def menu():
    while True:

        print('|****************** Menú ****************** |')
        print()
        print(" → 1. Cargar archivo XML.")
        print(" → 2. Diagnosticar paciente")
        print(' → 3. Salir.')
            
        print()
        n = input('Digite la opción a realizar: ')
        print()
        if n == "1":
        #  tree=ET.parse("./prueba.xml")
        # root=tree.getroot()



    # if n=="2":
            tipe1=1
            listac=ListaC()
            
            ruta = input('ingrese la dirección de su archivo XML: ')
            
        if n=="2":
           # pacientep.limpiarList()
            tree=ET.parse(ruta)
            root=tree.getroot()
            pacientep=passiente()
            for paciente in root:
                for datospersonales in paciente:
                    if datospersonales.tag.lower()=="datospersonales":
                        for dato in datospersonales:
                            if dato.tag.lower() =="nombre":
                                namep=str(dato.text)
                            # print("nombre: ",dato.text)
                            if dato.tag.lower() =="edad":
                                edadp=str(dato.text)
                            # print("edad: ",dato.text)

                    if datospersonales.tag.lower() =="periodos":
                        periodosp=str(datospersonales.text)
                    # print("periodos: ",datospersonales.text)
                    if datospersonales.tag.lower() =="m":
                        #print("m: ",datospersonales.text)
                        m=int(datospersonales.text)+1
                        mp=str(datospersonales.text)
                        neww=pacienten(namep,edadp,periodosp,mp)
                        pacientep.append(neww)
                        npaciente=pacientep.buscarpaciente(namep)

                    if datospersonales.tag.lower() =="rejilla":
                        for rejilla in datospersonales:

                            fila=int(rejilla.attrib["f"])
                            column=int(rejilla.attrib["c"])
                            nuevasceldas=Celda(fila,column,1)
                            npaciente.celdas.append(nuevasceldas)
                        i=1
                        for x in range(i, m):
                            j=1
                            for y in  range(j, m):
                                npaciente.celdas.buscar(int(x),int(y))
                        #  pass
                            
                #           print("fila: ",rejilla.attrib["f"])
                #          print("columna: ",rejilla.attrib["c"])
                        
                        # listac.pop(fila,column)

                        #----  listac.insertar(fila,column,1)
            
        

            pacientep.print()
            numeropaciente=input("ingrese el paciente que desea examinar: ")
            
            #npaciente.celdas.buscar("3","0")


           # npaciente=pacientep.buscarpaciente("Criscros")
            #npaciente.celdas.mostrarCeldas()
            f=0
            busqueda1=pacientep.returnNombrePaciente(int(numeropaciente))
            npaciente=pacientep.buscarpaciente(str(busqueda1))
            periodos=int(npaciente.periodo)
            npaciente.celdas.evaluar(periodos)
        
           # print("")
          #  print("-----------------------------")
         
         
         #   npaciente.celdas.mostrarCeldas()



            #npaciente.celdas.generarpdf()
            #npaciente.celdas.graficar()





        if n=="3":
            return False




    
menu()