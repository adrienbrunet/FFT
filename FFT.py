#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import cmath
from Tkinter import *


def test_puissance_2(degre):
	''' Teste si le polynôme à l'entrée est bien de degré n, n une puissance de 2 '''
	if math.log(degre, 2)-int(math.log(degre, 2)) == 0.0:
		print 'le degré du polynôme (' + str(degre) + ') est bien une puissance de 2'
		return True
	else:
		print 'le degré du polynôme (' + str(degre) + ') n\'est pas une puissance de 2'
		# # Cree une fenetre
		# wdw = Tk()
		# label = Label( wdw, text = 'Ecrire le polynôme de degré en puissance de 2 dont on veut la FFT' )
		# label.pack( side = TOP )
		# # Cree un bouton de parent 'wdw'
		# bq = Button( wdw, text = 'Quitter', command = wdw.destroy )
		# bq.pack()
		# #break
		# # # Lance la boucle d'attente d'événements
		# wdw.mainloop()
		return False


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

def diviser_liste(liste_coeff):
	''' Divise la liste des coefficients en deux parties, une contenant les chiffres pairs, une autre les chiffres impairs'''
	if len(liste_coeff)==1:
		pass


	if len(liste_coeff) %2 ==0:
		liste_paire_temp = [''] * (len(liste_coeff)/2)
		liste_impaire_temp = [''] * (len(liste_coeff)/2)
		for i in range(0, len(liste_coeff)/2 ):
			liste_paire_temp[i] = liste_coeff[2*i]
			liste_impaire_temp[i] = liste_coeff[2*i+1]
	if len(liste_coeff) %2 ==1:
		liste_paire_temp = [''] * ((len(liste_coeff)+1)/2)
		liste_impaire_temp = [''] * ((len(liste_coeff)-1)/2)
		for i in range(0, (len(liste_coeff)-1)/2 ):
			liste_paire_temp[i] = liste_coeff[2*i]
			liste_impaire_temp[i] = liste_coeff[2*i+1]
		liste_paire_temp[(len(liste_coeff)+1) / 2 - 1] = liste_coeff[len(liste_coeff) - 1]


	print liste_paire_temp, liste_impaire_temp
	return liste_paire_temp, liste_impaire_temp


def FFT(liste_coeff, degre_fft):
	''' Application de l'algorithme de la fft avec la méthode diviser pour régner. '''
	if degre_fft == 0:
		liste_coeff_fft = ['']*2
		liste_coeff_fft[0] = liste_coeff[0]
	if degre_fft>1:
		liste_paire, liste_impaire = diviser_liste(liste_coeff)
		fft_paire = FFT(liste_paire, degre_fft/2)
		fft_impaire = FFT(liste_impaire, degre_fft/2)
		racine_nieme_1 = racine_de_1(degre_fft)
		for compteur in range(0, degre_fft):
			liste_coeff_fft = [''] * (degre_fft)
			liste_coeff_fft[compteur] = fft_paire[compteur %degre_fft/2] + racine_nieme_1[compteur] * fft_impaire[compteur %degre_fft/2]
	return liste_coeff_fft	
		

def input_degre():
	'''Prends en entrée le degré du polynome et vérifie ce que l'utilisateur rentre'''
	degre_temp=""
	while 1:
		degre_temp = raw_input('Entrez le degre de votre polynome : ')
		try:
			degre_temp = int(degre_temp)
			if test_puissance_2(degre_temp):
				degre = degre_temp
				break
		except Exception, e:
			print 'Entrez un entier puissance de 2'
	return degre

def input_coeff(degre):
	coeff=[]
	coeff_temp=""
	degre_coeff = 0
	while degre_coeff<=degre:
		coeff_temp = raw_input('Entrez le coefficient de x^' + str(degre_coeff) + ' : ' )
		try:
			coeff_temp = float(coeff_temp)
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

def racine_de_1(degre):
	''' Calcule les racine n-ième de l'unité, défini comme suit http://fr.wikipedia.org/wiki/Racine_de_l%27unit%C3%A9 '''
	liste_racine = []
	for k in range(0, 2*degre):
		liste_racine.append(cmath.exp(2*k*1j*cmath.pi/2*degre))
	return liste_racine 

# F = main()
# print F