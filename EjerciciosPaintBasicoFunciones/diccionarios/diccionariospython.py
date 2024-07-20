mi_diccionario = {"nombre":"juan", "edad":30, "ciudad":"Cucuta"}
#pidiendo datos de ciudad.
print(mi_diccionario['ciudad'])
print(mi_diccionario)
#agregando posicion de profesion
mi_diccionario['profesion']='ingeniero'
print(mi_diccionario)
#actualizando la edad
mi_diccionario['edad']=35
print(mi_diccionario)
#recorrido por tamaño de la lista
for clave in range(len(mi_diccionario.keys())):
  print("posicion index diccionario: " + str(clave))

#recorrido por tamaño de la lista
for i in range(len(mi_diccionario.items())):
  clave=list(mi_diccionario.keys())[i]
  mi_diccionario[clave]='sobre escribe'
print("La posicion que se actualiza: "+ str(clave))
print("se actualiza datos: "+str(mi_diccionario))

#recorrido por la clave del diccionario
for clave in mi_diccionario.keys():
  mi_diccionario['nombre']= "Diego"
  print("Nombre clave diccionario: " + str(clave))

#recorrido y asignacion por items
for clave, valor in mi_diccionario.items():
  mi_diccionario['edad']=40
  #print(mi_diccionario)
  print("el diccionario actualizado: "+ clave, valor)