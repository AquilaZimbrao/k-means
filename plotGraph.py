def plotGraph(centroids):

    color = ['bo','yo','go']
    idColor = -1
    import matplotlib.pyplot as plt

    for c in centroids:
        idColor += 1
        for f in c['flores']:
            plt.plot(f['x'], f['y'], color[idColor])
    plt.show()


    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    
    objectsCentroid = [
        'Centroid 1 ({x},{y})'.format(x=round(centroids[0]['x'],2), y=round(centroids[0]['y'],2)),
        'Centroid 2 ({x},{y})'.format(x=round(centroids[1]['x'],2), y=round(centroids[1]['y'],2)),
        'Centroid 3 ({x},{y})'.format(x=round(centroids[2]['x'],2), y=round(centroids[2]['y'],2)),
        ]

    objects = [
        'Setosa',
        'Versicolor',
        'Virginica'
    ]*3

    y_pos = np.arange(len(objects))
    performance = []
    for c in centroids:
        setosa = 0
        versicolor = 0
        virginica = 0

        for f in c['flores']:
            if f['especie'] == 'Iris-setosa':
                setosa += 1
            elif f['especie'] == 'Iris-versicolor':
                versicolor += 1
            elif f['especie'] == 'Iris-virginica':
                virginica += 1

        performance.append(setosa)
        performance.append(versicolor)
        performance.append(virginica)
        
    plt.bar(y_pos, performance, align='center', alpha=1)
    plt.xticks(y_pos, objects)
    plt.ylabel('Numero de Ocorrencias')
    plt.title('Flores K-Means')

    plt.show()