#!/usr/bin/python

"""Solution to Net-Force Cryptography challenge 302: Substitution....
   --by Pranshu Bajpai"""

def subs(x):
      return {
          "o": "l",
	  "g": "e",
	  "r": "u",
	  "t": "z",
	  "z": "t",
	  "d": "f",
	  "l":"o",
	  "u":"r",
	  "a":"c",
	  "e":"g",
	  "d":"f",
	  "c":"a",
          "f":"d",
          "y":"w"
          }[x]

CIPHERTEXT = "ogrk hg tl`n srbszizrzig aiphgu mg ycahzylluf vllu fg ahcoogneg pceinc is ngzdluag"

PLAINTEXT = ""

for LETTER in CIPHERTEXT:
    if LETTER=='o' or LETTER=='g' or LETTER=='r' or LETTER=='t' or LETTER=='z' or LETTER=='d' or LETTER=="l" or LETTER=="u" or LETTER=="a" or LETTER=="e" or LETTER=="d" or LETTER=='c' or LETTER=='f' or LETTER=='y':
       PLAINTEXT = PLAINTEXT + subs(LETTER)
    else:
       PLAINTEXT = PLAINTEXT + LETTER

print PLAINTEXT
		