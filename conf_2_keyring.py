# -*- coding: utf-8 -*-
"""
Fichier de conversion dans le trousseau Keyring d'un fichier config
"""
import configparser
import keyring
config = configparser.ConfigParser()
# put here de config file you want to parse
config.read('config.file')
i=0
for section in config.sections():
	for cle,valeur in config.items(section):
		keyring.set_password(section,cle,valeur.strip('\"'))
		i= i+1
print (str(i)+" lignes traitées")

