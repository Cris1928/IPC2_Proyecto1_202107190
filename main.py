import xml.etree.ElementTree as ET
from NodoCelda import Celda
from ListaCelda import ListaC


def cargarXML(root):

    for elemento in root:
        for datos in elemento.findall('.//paciente/datospersonales'):
            nombre=datos.text
            print(nombre)



def menu():

    print('|****************** Menú ****************** |')
    print()
    print(" → 1. Cargar archivo XML.")
    print("→ 2. identificar nivel de enfermedad")

    print(' → 4. Salir.')
        
    print()
    n = input('Digite la opción a realizar: ')
    print()
    if n == "1":
        tree=ET.parse("./prueba.xml")
        root=tree.getroot()
    if n=="2":
        tipe1=1
        listac=ListaC()
        tree=ET.parse("./prueba.xml")
        root=tree.getroot()
        for paciente in root:
            for datospersonales in paciente:
                if datospersonales.tag.lower()=="datospersonales":
                    for dato in datospersonales:
                        if dato.tag.lower() =="nombre":
                            print("nombre: ",dato.text)
                        if dato.tag.lower() =="edad":
                            print("edad: ",dato.text)

                if datospersonales.tag.lower() =="periodos":
                    print("periodos: ",datospersonales.text)
                if datospersonales.tag.lower() =="m":
                    print("m: ",datospersonales.text)
                    i=0
                    j=0
                    m=int(datospersonales.text)+1
#                    for x in range(i, m):
 #                       #j=0
  #                      for y in  range(j, m):
   #                         listac.insertar(str(x),str(y),0)
    #                        #j=j+1
     #                  # i=i+i                 
            


                    #and j<= int(datospersonales.text):




                    
                if datospersonales.tag.lower() =="rejilla":
                    for rejilla in datospersonales:
                        fila=rejilla.attrib["f"]
                        column=rejilla.attrib["c"]
                        pass
                        
                        #print("fila: ",rejilla.attrib["f"])
                        #print("columna: ",rejilla.attrib["c"])
                       
                       # listac.pop(fila,column)

                        listac.insertar(fila,column,1)





        listac.pop("1","1")
        listac.mostrarCeldas()
     #   listac.buscar("1","1")
      #  listac.pop("1","1")
        #listac.mostrarCeldas()
        



       
menu()

