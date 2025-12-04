def add_nacho(list, miset):
    for item in list:
        miset.add(item)
    return miset


animalesset = {'Leon', 'Gato', 'Perro'}
animalesset = add_nacho(['Cuervo', 'Jirafa', 'Corzo'], animalesset)
print(animalesset)
