import math
import csv
from random import randint
flores = []
xMin = 100000000
yMin = 100000000
xMax = -100000000
yMax = -100000000

def getCentroids(modo):
    centroids = []
    if modo == 1:
        centroids.append(dict(
            x=xMin,
            y=yMin,
            flores=[],
        ))

        centroids.append(dict(
            x=xMax-xMin,
            y=yMax-xMin,
            flores=[],
        ))

        centroids.append(dict(
            x=xMax,
            y=yMax,
            flores=[],
        ))
    elif modo == 2:
        centroids.append(dict(
            x=randint(0, 9),
            y=randint(0, 9),
            flores=[],
        ))

        centroids.append(dict(
            x=randint(0, 9),
            y=randint(0, 9),
            flores=[],
        ))

        centroids.append(dict(
            x=randint(0, 9),
            y=randint(0, 9),
            flores=[],
        ))
    elif modo == 3:
        f = flores[randint(0, len(flores))]
        centroids.append(dict(
            x=f['x'],
            y=f['y'],
            flores=[],
        ))

        f = flores[randint(0, len(flores))]
        centroids.append(dict(
            x=f['x'],
            y=f['y'],
            flores=[],
        ))

        f = flores[randint(0, len(flores))]
        centroids.append(dict(
            x=f['x'],
            y=f['y'],
            flores=[],
        ))

    return centroids

def calculoDist(xA, yA, xB, yB):
    return round(math.sqrt((xA-xB)**2) + ((yA-yB)**2),3)

def compare(x1, x2):
    return abs(x1-x2) <= 0.01

def lerFlores():
    ficheiro = open('dataset_iris.csv', 'r')
    reader = csv.reader(ficheiro)
    for key, linha in enumerate(reader):
        if (key>0 and len(linha)):
            xF = float(str(linha[0]).replace(',','.'))
            yF = float(str(linha[2]).replace(',','.'))

            global xMin
            global xMax
            global yMin 
            global yMax

            xMin = min(xMin, xF)
            xMax = max(xMax, xF)
            yMin = min(yMin, yF)
            yMax = max(yMax, yF)

            flores.append(dict(
                x=xF,
                y=yF,
                especie=linha[4],
                centroids=[0,0,0],
            ))

def calculaDistFlorCentroid():
    for key, c in enumerate(centroids):
        c['flores'] = []
        for f in flores:
            f['centroids'][key] = calculoDist(c['x'], c['y'], f['x'], f['y'])

def acharMelhorCentroid(): 
    for f in flores:
        melhorCentroid = min(f['centroids'])
        idCentroid = f['centroids'].index(melhorCentroid)

        centroids[idCentroid]['flores'].append(f)

def recalcularCentroid():
    m = 0
    for c in centroids:
        n = len(c['flores'])
        if n:
            x = 0
            y = 0
            for f in c['flores']:
                x += f['x']
                y += f['y']

            x = x/n
            y = y/n

            if (not compare(x, c['x']) or not compare(y, c['y'])):
                m = 1
            c['x'] = x
            c['y'] = y
    return m


for t in list(range(3)):
    flores = []
    lerFlores()
    centroids = getCentroids(t+1)
    mudou = 1
    numero = 1
    while(mudou):

        calculaDistFlorCentroid()
        acharMelhorCentroid()
        mudou = recalcularCentroid()
        numero +=1

    import plotGraph as plot
    plot.plotGraph(centroids)

