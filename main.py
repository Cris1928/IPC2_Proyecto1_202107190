import webbrowser
import xml.etree.ElementTree as ET
from NodoCelda import Celda
from ListaCelda import ListaC
from NodoPaciente import pacienten
from ListarPasiente import passiente
from ListaNumeral import ListadoNumeral
from fpdf import FPDF
from xml.dom import minidom
import os
from colorama import Fore
def cargarXML(root):

    for elemento in root:
        for datos in elemento.findall('.//paciente/datospersonales'):
            nombre=datos.text
            print(nombre)
def XML(root):
    pass

def menu():
    global numeroxml
    numeroxml=1
    global nuevonumero
    nuevonumero=ListadoNumeral()
    while True:
        print(Fore.LIGHTYELLOW_EX+'*************************** Menú **************************')
        print("*                                                         *")
        print("* → 1. Cargar archivo XML.                                *")
        print("* → 2. Diagnosticar paciente.                             *")
        print("* → 3. Evaluar si posee alguna enfermedad-                *")
        print("* → 4. Generar reporte de diagnostico de los pacientes.   *")
        print('* → 5. Salir.                                             *')
        print("*                                                         *")
        print('***********************************************************')
        print()
        n = input(Fore.CYAN+'Digite la opción a realizar: ')
        print()
        if n == "1":
#C:\Users\USER\Desktop\Prueba1.xml
#C:\Users\USER\Desktop\IPC2_Proyecto1_202107190\prueba.xml
            pacientep=passiente()
            pacientep.limpiarList()
 
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
                            if dato.tag.lower() =="edad":
                                edadp=str(dato.text)

                    if datospersonales.tag.lower() =="periodos":
                        periodosp=str(datospersonales.text)
                    if datospersonales.tag.lower() =="m":
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
                    

            pacientep.print()
            print(" ")
            numeropaciente=input(Fore.CYAN+"ingrese el paciente que desea examinar: ")
            nuevonumero.limpiarList()

            busqueda1=pacientep.returnNombrePaciente(int(numeropaciente))
            npaciente=pacientep.buscarpaciente(str(busqueda1))
            periodos=int(npaciente.periodo)
            npaciente.celdas.evaluar(periodos)
            print(" ")
            print(" ")
            diagnostico=npaciente.celdas.enfermedad(periodos)
            if diagnostico == 0:
                print(Fore.BLUE+"\n Diagnostico: La enfermedad es leve")
            elif diagnostico == 1:
                print(Fore.LIGHTRED_EX+"\n Diagnostico: La enfermedad es mortal")
            elif diagnostico > 1:
                print(Fore.RED+"\nDiagnostico: La enfermedad es grave")
            else:
                pass
            print(" ")
            print(" ")
            generarPDF(periodos,busqueda1)

            nuevonumero.limpiarList()
        elif n=="3":
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
                            if dato.tag.lower() =="edad":
                                edadp=str(dato.text)

                    if datospersonales.tag.lower() =="periodos":
                        periodosp=str(datospersonales.text)
                    if datospersonales.tag.lower() =="m":
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
                    

            pacientep.print()
            print(" ")
            numeropaciente=input(Fore.CYAN+"ingrese el paciente que desea examinar: ")
            nuevonumero.limpiarList()

            busqueda1=pacientep.returnNombrePaciente(int(numeropaciente))
            npaciente=pacientep.buscarpaciente(str(busqueda1))
            periodos=10000
            npaciente.celdas.evaluar(periodos)
            print(" ")
            print(" ")
            diagnostico=npaciente.celdas.enfermedad(periodos)
            if diagnostico == 0:
                print(Fore.BLUE+"\n Diagnostico: La enfermedad es leve")
            elif diagnostico == 1:
                print(Fore.LIGHTRED_EX+"\n Diagnostico: La enfermedad es mortal")
            elif diagnostico > 1:
                print(Fore.RED+"\nDiagnostico: La enfermedad es grave")
            else:
                pass
            print(" ")
            print(" ")
            generarPDF(periodos,busqueda1)

            nuevonumero.limpiarList()
        elif n=="4":
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
                            if dato.tag.lower() =="edad":
                                edadp=str(dato.text)

                    if datospersonales.tag.lower() =="periodos":
                        periodosp=str(datospersonales.text)
                    if datospersonales.tag.lower() =="m":
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

            imprimir=int(pacientep.returnTamano())
            pacientes=minidom.Document()
            xml=pacientes.createElement("pacientes")
            pacientes.appendChild(xml)


            for num in range(1,imprimir+1):
                nuevonumero.limpiarList()

                busqueda1=pacientep.returnNombrePaciente(int(num))
                npaciente=pacientep.buscarpaciente(str(busqueda1))
                periodos=int(npaciente.periodo)
                npaciente.celdas.evaluarXML(periodos)
                patronenfermo=npaciente.celdas.RetornarPatron(periodos)
                diagnostico=npaciente.celdas.enfermedadXML(periodos)
          #      patronenfermo=npaciente.celdas.RetornarCeldaEnferma(periodos)
                if diagnostico == 0:
                    resultado="leve"
                elif diagnostico == 1:
                    resultado="mortal"
                elif diagnostico > 1:
                    resultado="grave"
                else:
                    pass     
                pacientexml=pacientes.createElement("paciente")
                xml.appendChild(pacientexml)
                datospersonalesxml=pacientes.createElement("datospersonales")
                pacientexml.appendChild(datospersonalesxml)

                datoxml=pacientes.createElement("nombre")
                datoxml.appendChild(pacientes.createTextNode("{}".format(npaciente.nombre)))
                datospersonalesxml.appendChild(datoxml)
            
                datoxml=pacientes.createElement("edad")
                datoxml.appendChild(pacientes.createTextNode("{}".format(npaciente.edad)))
                datospersonalesxml.appendChild(datoxml)

                periodosxml=pacientes.createElement("periodos")
                periodosxml.appendChild(pacientes.createTextNode("{}".format(npaciente.periodo)))
                pacientexml.appendChild(periodosxml)

                mxml=pacientes.createElement("m")
                mxml.appendChild(pacientes.createTextNode("{}".format(npaciente.m)))
                pacientexml.appendChild(mxml)

                resultadoxml=pacientes.createElement("m")
                resultadoxml.appendChild(pacientes.createTextNode("{}".format(resultado)))
                pacientexml.appendChild(resultadoxml)

                Nxml=pacientes.createElement("N")
                Nxml.appendChild(pacientes.createTextNode("{}".format(patronenfermo)))
                pacientexml.appendChild(Nxml)

                N1xml=pacientes.createElement("N1")
                N1xml.appendChild(pacientes.createTextNode("{}".format(diagnostico)))
                pacientexml.appendChild(N1xml)

                nuevonumero.limpiarList()

           

            xml_str=pacientes.toprettyxml(indent="\t")
            save_path_file="Reporte_{}.xml".format(numeroxml)
            with open(save_path_file,"w") as f:
                f.write(xml_str) 

            numeroxml=numeroxml+1
        elif n=="5":
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