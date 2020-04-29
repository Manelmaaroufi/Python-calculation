import numpy 

Eleve=int(input('eleves?'))

note= []
for i in range(Eleve):
    x=int(input('donnée un entier'))
    
    note.append(x)
    
x = numpy.mean(note) 
print(x)

v= numpy.median(note)
print(v)