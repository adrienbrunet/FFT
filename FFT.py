#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import log, ceil, pi
from cmath import exp


def main():
	''' Programme principal pour lancer la Fast Fourier Transform, cf http://fr.wikipedia.org/wiki/Transform%C3%A9e_de_Fourier_rapide. Utilisation de la méthode diviser pour regner. 
	Le polynôme sera demandé en console.'''
	#degre du polynome
	degre = input_degre() 
	#Coefficient
	liste_coeff = input_coeff(degre)
	#Debut du diviser pour régner et du fft
	FF = FFT(liste_coeff, degre)
	return FF

def FFT(liste_coeff, degre_fft):
	''' Application de l'algorithme de la fft avec la méthode diviser pour régner. '''
	if len(liste_coeff) == 1:
		liste_coeff_fft = [liste_coeff[0] for i in range(degre_fft)]
	else:
		liste_paire   = [liste_coeff[i] for i in range(0, len(liste_coeff), 2)]
		liste_impaire = [liste_coeff[i] for i in range(1, len(liste_coeff), 2)] 
		fft_paire   = FFT(liste_paire, degre_fft/2)
		fft_impaire = FFT(liste_impaire, degre_fft/2)
		racine_nieme_1 = exp(1j*2*pi/(degre_fft))
		racine = 1
		liste_coeff_fft = [0 for i in range(degre_fft)]
		for compteur in range( (degre_fft) / 2):
			x = racine * fft_impaire[compteur]
			liste_coeff_fft[compteur] = fft_paire[ compteur ] + x
			liste_coeff_fft[compteur + (degre_fft)/2] = fft_paire[ compteur ]  - x
			racine *= racine_nieme_1
	return liste_coeff_fft

def test_puissance_2(degre):
	''' Teste si le polynôme à l'entrée est bien de degré n-1, n une puissance de 2 '''
	if log(degre + 1, 2)-int(log(degre + 1, 2)) == 0.0:
		print 'le degré du polynôme (' + str(degre) + ') est bien une puissance de 2 moins 1'
		return True
	else:
		print 'le degré du polynôme (' + str(degre) + ') n\'est pas une puissance de 2 moins 1'
		return False


def input_degre():
	'''Prends en entrée le degré du polynome et vérifie ce que l'utilisateur rentre'''
	degre_temp = ""
	while 1:
		degre_temp = raw_input('Entrez le degre de votre polynome : ')
		try:
			degre_temp = int(degre_temp)
			if test_puissance_2(degre_temp):
				degre = degre_temp
				break
		except Exception, e:
			print 'Entrez un entier : une puissance de 2 moins 1'
	return degre

def input_coeff(degre):
	''' Rentrer les coefficients à la console. Verification des données entrées.  '''
	coeff=[]
	coeff_temp=""
	degre_coeff = 0
	while degre_coeff<=degre:
		coeff_temp = raw_input('Entrez le coefficient de x^' + str(degre_coeff) + ' : ' )
		try:
			coeff_temp = complex(coeff_temp)
			degre_coeff += 1
			coeff.append(coeff_temp)
		except Exception, e:
			print 'Entrez un coefficient'
		if coeff_temp == 0.0:
			if degre_coeff == degre + 1 :
				try:
					print 'Mauvais coefficient, le coefficient de plus haut degre ne peut pas être nul'
					degre_coeff = degre_coeff - 1
					coeff.pop()
				except Exception, e:
					pass
	return coeff

def mult(a,b ):
	'''Multiplier les deux polynomes'''
	degre = len(a) + len(b) -1 
	degre = 2**int(ceil(log(degre,2)))  
	fft_a = FFT(a,degre)
	fft_b = FFT(b,degre)
	#print fft_a
	#print fft_b
	result_1 = [ fft_a[i] * fft_b[i] for i in range(degre)]
	fft_result_1 = FFT(result_1,degre)
	resultat =  [ fft_result_1[i]/degre for i in range(1) + range(degre-1,0,-1)]
	return resultat


#G = main()
#H = mult(F,G)
#print H

#a =[1,1,1,1]
#b = [1,1,1,1]
#n=  2**int(ceil(log(7,2)))   
#print FFT(a,n)
#print FFT(b,n)
#print FFT(a,8)
#A = mult(a,b)
#print A

# print len(A)
# H2 = arrondi(H)
# print H2

