from list import liste
import random

# Fonction qui choisit un nombre premier different d'un autre
def nbPremierDiff(src) :
  dest = liste[r.randrange(len(liste))]
  while src == dest:
    dest = liste[r.randrange(len(liste))]
  return dest
# Algorithme d'Euclide pour le pgcd 
def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b
# Conversion message equivalent ascii
def convert_ascii(message) :
  i = 0
  message_ascii = ""
  bigger = 0
  while i != len(message):
    c = ord(message[i])
    if c > bigger :
      bigger = c
    message_ascii = message_ascii + str(c)
    i = i + 1
  return [bigger, message_ascii]
# Algorithme d'Euclide etendu
def euclide_etendu(e, phi_n) :
  d = 1 
  temp = (e*d)%phi_n
  while(temp != 1):
    d = d+1
    temp = (e*d)%phi_n
  return d
# Chiffrement du message
def chiffrer(message_ascii, e, n):
  message_chiffre = str(pow(int(message_ascii), e)%n)
  return message_chiffre
######## Menu ########
choix = input('Salut a toi utilisateur, dis moi ce que je dois faire : \n1.Chiffrer\n2.Dechiffrer\nEntre une option du menu : ')
while choix != 1 and choix != 2 :
  choix = input('\nErreur, entrez soit 1 ou 2 : ')
######## Chiffrement ########
if choix==1:
  message = raw_input('\nOk, saisis le message que tu veux chiffrer : ')
  mm = convert_ascii(message)
  bigger = mm[0]
  message_ascii = mm[1]
  print "\n...\n"
  ####### Generation de p et q ########
  r = random.SystemRandom()
  p =liste[r.randrange(len(liste))]
  q = nbPremierDiff(p)
  n = p * q
  phi_n = (p-1)*(q-1)
  ######## Choix d'un exposant e et calcul de son inverse d ########
  e = r.choice(liste)
  d = euclide_etendu(e, phi_n)
  print "Cle publique :", e, "\nModulo :", n,"\nCle prive :", d
  # n et e = cle publique, d = cle prive
  print "\nEt voila le travail :\n", chiffrer(message_ascii, e, n)
######## Dechiffrement ########
else:
  message = raw_input('\nOk, saisis le message que tu veux dechiffrer : ')
  d = input('Super, maintenant la cle prive : ')
  n = input('Enfin le modulo : ')
  message = chiffrer(message, d, n)
  print "\nEt voila le travail :\n", message