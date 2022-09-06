import webbrowser
import xml.etree.ElementTree as ET
from NodoCelda import Celda
from ListaCelda import ListaC
from NodoPaciente import pacienten
from ListarPasiente import passiente
from ListaNumeral import ListadoNumeral
from fpdf import FPDF
import os

#C:\Users\USER\Desktop\Prueba1.xml
#C:\Users\USER\Desktop\IPC2_Proyecto1_202107190\prueba.xml

def cargarXML(root):

    for elemento in root:
        for datos in elemento.findall('.//paciente/datospersonales'):
            nombre=datos.text
            print(nombre)
def XML(root):
    pass

def menu():
    global nuevonumero
    nuevonumero=ListadoNumeral()
    while True:
        print('|************************* Menú ************************* |')
        print(" ")
        print(" → 1. Cargar archivo XML.")
        print(" → 2. Diagnosticar paciente")
        print(" → 3. Generar reporte de diagnostico de los pacientes")
        print(' → 4. Salir.')
        print(" ")
        print('|******************************************************* |')
            
        print()
        n = input('Digite la opción a realizar: ')
        print()
        if n == "1":
#C:\Users\USER\Desktop\Prueba1.xml
#C:\Users\USER\Desktop\IPC2_Proyecto1_202107190\prueba.xml
            pacientep=passiente()
            pacientep.limpiarList()
        #  tree=ET.parse("./prueba.xml")
        # root=tree.getroot()
    # if n=="2":
            ruta = input('ingrese la dirección de su archivo XML: ')
        elif n=="2":
            nuevonumero=ListadoNumeral()
            tree=ET.parse(ruta)
            root=tree.getroot()
            pacientep.limpiarList()
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
        #------------------------------------------------------------------------------------------------------------------

            pacientep.print()
            numeropaciente=input("ingrese el paciente que desea examinar: ")
            
            #npaciente.celdas.buscar("3","0")


           # npaciente=pacientep.buscarpaciente("Criscros")
            #npaciente.celdas.mostrarCeldas()
            nuevonumero.limpiarList()

            busqueda1=pacientep.returnNombrePaciente(int(numeropaciente))
            npaciente=pacientep.buscarpaciente(str(busqueda1))
            periodos=int(npaciente.periodo)
            npaciente.celdas.evaluar(periodos)
            print(" ")
            print(" ")
            diagnostico=npaciente.celdas.enfermedad(periodos)
            if diagnostico == 0:
                print("\n Diagnostico: La enfermedad es leve")
            elif diagnostico == 1:
                print("\n Diagnostico: La enfermedad es mortal")
            elif diagnostico > 1:
                print("\n Diagnostico: La enfermedad es grave")
            else:
                pass
            print(" ")
            print(" ")
            generarPDF(periodos,busqueda1)
           # print("")
          #  print("-----------------------------"
         #   npaciente.celdas.mostrarCeldas()
            #npaciente.celdas.generarpdf()
            #npaciente.celdas.graficar()
            nuevonumero.limpiarList()
        elif n=="3":
            return False
        else:
            pass
def generarPDF(periodos,nombre):
    pdf=FPDF(orientation="P",unit="mm",format="A4")
    for i in range(0,(periodos+1)):
        pdf.add_page()
        pdf.image("graphviz{}".format(i)+".png",x=50,y=50,w=120,h=120)
    pdf.output("{}".format(nombre)+".pdf")
    for i in range(0,(periodos+1)):
        os.remove("graphviz{}".format(i)+".png")
        os.remove("graphviz{}".format(i)+".dot")    

menu()