degre_temp=""

print type(degre_temp)

while 1:
	degre_temp = raw_input('Entrez le degre de votre polynome : ')
	try:
		degre_temp = int(degre_temp)

		break
	except Exception, e:
		print 'Entrez un entier'