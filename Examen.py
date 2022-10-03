import json
import sys

Coj=set()
ar=[]
tupla=set()
dirrec={}
lista=[]
lista_Materia=[]
def Materias():
    try:
        MA = open("Kardex.txt", "r")
        matr = []
        lis = []
        for x in MA:
            lis = x.split("|")
            matr.append(lis[0])
            matr.append(lis[1])
            matr.append(lis[2].replace("\n", ""))
            Coj.add(tuple(matr))
            matr.clear()
        # print(Coj)
        MA.close()
        return (Coj)
    except:
        print("No se encuentra el archivo dentro de la retua espesificada")
        sys.exit()

def Alumnos():
    try:
        archivo = open("Estudiantes.prn", "r")
        for x in archivo:
            ar.append(x[0:8])
            ar.append(x[8:].replace("\n", ""))
            tupla.add(tuple(ar))
            ar.clear()
        archivo.close()
        # print(tupla)
        return tupla
    except:
        print("No se encuentra el archivo dentro de la retua espesificada")
        sys.exit()

def llenado_json():
    for x in Alumnos():
        dirrec={}
        lista_Materia=[]
        nc,NomA=x
        for M in Materias():
            numeroControl,NombreMateria,Promedio=M
            if(numeroControl==nc):
              lista_Materia.append(NombreMateria)
        dirrec["Nombre"]=NomA
        dirrec["Materia"]=lista_Materia
        lista.append(dirrec)
    return lista
def llenado_jason2(*args):
    cont=0
    lista=[]
    for i in args:
        for x in Alumnos():
            dirrec = {}
            lista_Materia = []
            nc, NomA = x
            if nc==i:
                cont=1
                for M in Materias():
                    numeroControl, NombreMateria, Promedio = M
                    if (numeroControl == nc):
                        lista_Materia.append(NombreMateria)
                dirrec["Nombre"] = NomA
                dirrec["Materia"] = lista_Materia
                lista.append(dirrec)
    if cont!=0:
        return  json.dumps(lista)
    else:
        return json.dumps(llenado_json())
#print(llenado_json())
print(llenado_jason2("18420465"))
print(llenado_jason2("18420427"))
print(llenado_jason2("18420427","18420465","18420428"))
print(llenado_jason2())