global1 = 34

def cambiar_global(x):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1 = x

    pass
cambiar_global(10)
#print(global1)

def anio_bisiesto(x):
  '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
  '''
#   if (x % 4==0) and (x %100 != 0) and (x%400==0):
#     return True
#   else:
#     return False
#   pass
  return (x % 4==0) and (x %100 != 0) and (x%400==0)

anio_bisiesto(2020)


def contar_valles(*args):

  r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
  '''
  count=0
  for i in range(len(args[0])):
    if args[0][i] == 0:
      count+=1
  return count 
  #pass
print(contar_valles([-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1]))
#print(a)


def saltando_rocas(rocas):
  
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    numsalto=0
    j=0
    for i in range(len(rocas)):
      if j<=len(rocas) and j+2 <len(rocas) and rocas[j+2]==0:
        j=j+2
        numsalto+=1
      elif j<=len(rocas) and j+1 <len(rocas) and rocas[j+1]==0:
        j=j+1
        numsalto+=1
      else:
        return numsalto
    pass

print(saltando_rocas([0,1,0,0,1,0,0]))

def pares_medias(lista):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    #lista=[0,0,1,3,0,1,5,0,5,2,0,0,5]
    a=set(lista)
    listaunica=list(a)
    dic={}
    for i in listaunica:
      b=lista.count(i)
      if b/2>=1:
          dic[i]=b//2
    return dic
print(pares_medias([0,0,1,3,0,1,5,0,5,2,0,0,5]))

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'

class ListaComa:
    
    #itemlist=[]
    
    def __init__(self, lista=[]):
        self.lista=lista
        
    def __str__(self):
        itemlist=""
        
        for i in self.lista:
            itemlist+=str(i)+","
            
        itemlist= itemlist[:len(itemlist)-1]
        return '{}'.format(itemlist)
    

objlistacoma = ListaComa([1,"b",2,"c"])
print(objlistacoma)



# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'
class Persona:
  def __init__(self,nombres=[],apellidos=[]):
    self.nombres=nombres
    self.apellidos=apellidos
#    self.lapellidos=remnumtitle(self.apellidos)
 
  def nombre_completo(self):
    for i,j in enumerate(self.nombres):
      if type(j)==str:
        self.nombres[i]=self.nombres[i].title()
      else:
        del self.nombres[i]        

    for i,j in enumerate(self.apellidos):
      if type(j)==str:
        self.apellidos[i]=self.apellidos[i].title()
      else:
        del self.apellidos[i]        

    nombrecompleto=''        
    
    self.apellidos=list(reversed(self.apellidos))
    for i in self.apellidos:
      nombrecompleto=i+' '+nombrecompleto

    self.nombres=list(reversed(self.nombres))
    for i in self.nombres:
      nombrecompleto=i+' '+nombrecompleto
    return nombrecompleto
       
nombre=Persona(['jair','mateo','Angie','Anabella','hilba',222], ['lara','ramirez','Morelos','rammo','ruiz',332])
print(nombre.nombre_completo())




# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.

