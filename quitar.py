
"""








 <paciente>


        <datospersonales>
            <nombre>Daniel</nombre>
            <edad>14</edad>
        </datospersonales>
        <periodos>6</periodos>
        <m>15</m>
        <rejilla>
            <celda f="2" c="1" />
            <celda f="3" c="2" />
            <celda f="4" c="1" />
            <celda f="5" c="2" />
            <celda f="3" c="6" />
            <celda f="3" c="7" />
            <celda f="3" c="6" />
            <celda f="2" c="7" />
        </rejilla>


 </paciente>


































 #ruta = input('ingrese la dirección de su archivo XML: ')
        try:
            xmlfile=open('C:\Users\USER\Desktop\IPC2_Proyecto1_202107190\archivo de prueba\prueba.xml')
            if xmlfile.readable():
                xmldata= ET.fromstring(xmlfile.read())
                lstcel=xmldata.findall('datospersonales')
                for rejilla in lstcel:

                    print(f"...{rejilla.find('nombre').text}")
                    print("------------------------------------------")


                    #if rejilla.tag.lower() == 'c':
                
                     #   r = int(subelement.text)
                      #  #print(r)
            
                   # elif rejilla.tag.lower() == 'f':
                
                    #     c = int(subelement.text)
                     #    #print(c)

            
            
        except Exception as err:    
            print("Error: ", err)   
        finally:
            xmlfile.close()






-----------------------------------------------
tree=ET.parse('prueba.xml')
        root=tree.getroot()
        def nombres(nombre):
            return nombre.text
            
        def Edades(edad):
            return edad.text

        def rango(m):
            return m.text
        
        def celdas(celda):
            return celda.attrib
        print("----------------------------------------")
        nombress=list(map(nombres,root.iter('nombre: ')))
        edadess=list(map(Edades,root.iter('edad: ')))
        rangos=list(map(rango,root.iter('rango: ')))
        celdass=list(map(celdas,root.iter('celdas: ')))
        print(nombress)
        print(edadess)
        print(rangos)
        print(celdass)

------------------------------------------------------------------
try:

            ruta="prueba.xml"
           # ruta = input('ingrese la dirección de su archivo XML: ')
            tree = ET.parse(ruta)
            root = tree.getroot()
            
        except:
                
            print('|---------- ERROR: Datos no cargados-----------|')    

    elif n == '2':
        ruta="prueba.xml"
        tree=ET.parse(ruta)
        root = tree.getroot()
        for elemento in root:
            for datos in elemento.findall('.//paciente/datospersonales'):
                nombre=datos.text
                print(nombre)












"""