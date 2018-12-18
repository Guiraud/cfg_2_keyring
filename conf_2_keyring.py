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
	for clé,valeur in config.items(section):
		keyring.set_password(section,clé,valeur.strip('\"'))
		i= i+1
print (str(i)+" lignes traitées")

