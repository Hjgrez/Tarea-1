import csv
import random
import time
import json


def abrir_csv(nombre):
    nombrecsv = open(nombre)
    basenombre = csv.reader(nombrecsv)
    basenombre= list(basenombre)
    return basenombre


def estadistica(nombre,amigos,arch):
    inicio=time.clock()
    basecheck = abrir_csv(nombre)
    baseamigos = abrir_csv(amigos)
    basecheck.pop(0)
    basecheck.sort(key=lambda x: x[0])
    cant_ids=0
    cant_ubic=0
    ult_id=None
    ult_ubic= None
    for index in range(len(basecheck)):
        if basecheck[index][0]==ult_id:
            continue
        elif basecheck[index][0]!=ult_id:
            ult_id=basecheck[index][0]
            cant_ids+=1
    basecheck.sort(key=lambda x: x[-1])
    for index in range(len(basecheck)):
            if basecheck[index][-1]==ult_ubic:
                continue
            elif basecheck[index][-1]!=ult_ubic:
                ult_ubic=basecheck[index][-1]
                cant_ubic+=1
    tiempo=time.clock()-inicio
    mensaje = ""
    mensaje += ("La cantidad de ubicaciones es: "+ str(cant_ubic)+"\n")
    mensaje += ("La cantidad de usuarios es: "+ str(cant_ids) + "\n")
    mensaje += ("La cantidad de checkins es: " +str(len(basecheck))+ "\n")
    mensaje += ("El prom de checkins por persona es: " + str(float((len(basecheck)/cant_ids))) + "\n")
    mensaje += ("El prom de checkins por lugar es: " + str(float(len(basecheck)/cant_ubic)) + "\n")
    mensaje += ("El prom de amigos por usuario es: " + str(float(len(baseamigos)/(cant_ids))) + "\n")
    print("El computador tardo: {0}:{1} segs".format(int(tiempo//60),int(tiempo%60)))
    print(mensaje)
    estad = open(arch,"w")
    estad.write(mensaje)
    estad.close()
    
    return None


def azar(nombase,nombre):
    base = abrir_csv(nombase)
    archivo = open(nombre,"w")
    lis_azar = []
    base.pop(0)

    for i in range(500):
        indice= random.randint(0,len(base))
        item = base.pop(indice)
        item = item[1:3]
        item = [float(x) for x in item]
        lis_azar.append(item)
    lis_json=json.dumps(lis_azar)
    datos_json="var datos = " + lis_json
    archivo.write(datos_json)
    archivo.close()
    return None

estadistica("../datos/foursquare_checkins.csv","../datos/foursquare_friendship.csv","../datos/estadisticas3.txt")
lis_azar= azar("../datos/foursquare_checkins.csv","../datos/muestra2.json")

