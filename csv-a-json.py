
#!/usr/bin/python
#Convertir archivos .TXT o.CSV a .JSON
import csv, decimal, codecs, simplejson

print "\n ----- CSV o TXT a JSON -----"
archivoIn = raw_input("\nIngrese la ruta del archivo que contiene los datos: ")
archivoOut = raw_input("\nIngrese el nombre que tendra el archivo .json: ")

#Abrimos el archivo .txt o .csv
f = open(archivoIn)

#Creamos los diccionarios en una lista
lector = csv.DictReader(f, delimiter=",", quotechar='"') 

#Creacion del archivo .json
with codecs.open(archivoOut, "w", encoding="utf-8") as salida:
   
   #Recorremos la lista
   for l in lector:
      #Escribiendo los datos en el archivo
      salida.write(simplejson.dumps(l, ensure_ascii=False, use_decimal=True)+"\n")
   print "Archivo ", archivoOut, "creado exitosamente!"

f.close() #Cerramos el archivo
