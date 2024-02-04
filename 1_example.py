'''
Ejemplo: Cree un programa que muestre todos los string de
largo 3 que se pueden formar a partir de las letras "a", "b" y
"c".
'''
def permutaciones(s) :
    if(len(s) == 3):
        print(s)
        return
    for c in ['a', 'b', 'c']:
        permutaciones(s + c)

permutaciones ("")