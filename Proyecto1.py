def cargarArchivo():
    print("Aqui se cargará el archivo")

def procesarArchivo():
    print("Aqui se procesará el archivo")

def archivoSalida():
    print("Aqui se creará el archivo de salida")

def datosEstudiante():
    print("Osmar Noel Chacón Lemus")
    print("201900822")
    print("Introducción a la Programación y Computación 2 Sección E")
    print("Ingeniería en Ciencias y Sistemas")
    print("Quinto Semestre")
    print("##########################################################")

def generarGrafica():
    print("Aqui se va generar la gráfica")
    
print("> Bienvenido al programa, aparecerá una lista donde debe elegir la opción")
print("-------------------------------------------------------------------------")

op=0
while op!=6:
    print("Menú Principal:")
    print("\t1. Cargar archivo")
    print("\t2. Procesar archivo")
    print("\t3. Escribir archivo de salida")
    print("\t4. Mostrar datos del estudiante")
    print("\t5. Generar gráfica")
    print("\t6. Salida")
    op=int(input())
    if op==1:
        cargarArchivo()
    if op==2:
        procesarArchivo()
    if op==3:
        archivoSalida()
    if op==4:
        datosEstudiante()
    if op==5:
        generarGrafica()
print("Gracias por usar el programa")
    