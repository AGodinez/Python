#!/usr/bin/python
#Script para hacer ping en nuestra red local

from subprocess import Popen, PIPE

p = 0
print "\n  Script para hacer ping en nuestra red en un rango determinado\n"
i = input ("Inicio (ej: 1): ")
f = input ("Fin (ej: 255): ")
print " "
for ip in range(i,f):
	ipDir = '192.168.1.'+str(ip)
	subprocess = Popen(['/bin/ping', '-c 1 ', ipDir], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	if "bytes from " in stdout:
		print "La direccion IP %s ha respondido con un ECHO_REPLY!" %(stdout.split()[1])
		p += 1
		with open("IPs.txt", "a") as archivo:
			archivo.write(stdout.split()[1]+'\n')
if p == 0:
	print 'Ninguna IP del rango 192.168.1.'+str(i)+'-'+str(f)+" respondio con ECHO_REPLY"
