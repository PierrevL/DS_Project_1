# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import randint

words = ['baum', 'stuhl', 'tisch', 'lampe', 'nuss'] # Worte zum raten definieren
selectedWordNumber = randint(0, len(words) -1)      # randem int
selectedWord = ' '                                  # var anlegen für string
selectedWord = words[selectedWordNumber]            # gesuchtes wort als string
#print(f'selectedWord: , {selectedWord}')

wordToFind = []                                     #feld anlegen
wordToFind[:0] = selectedWord                       #string in feld konvertieren

selectedWordblind = []                              #feld für blind wort anlegen
i=0
while i < (len(selectedWord)):                      #blind Wort mit underlins in richtige läge als feld erstellen
  selectedWordblind.append('_')
  i = i + 1

attempt = 0                                         #zähler für versuch evorbereiten

def stestIsWordGuess():                             #funktion zum überprüfen pb das wort geraten wurde
  z = 0                                             #es wird geprüft ob beriets alle underlines ersetzt wurden
  wert = 0
  while z < (len(selectedWord)):
    if (selectedWordblind[z] == '_'):
      wert = 1
    z = z + 1
  return wert

stop = 1
while stop == 1:                                  # solange das Wort nicht geraten wurde
  print(f'Dein zu erratendes Wort: , {selectedWordblind}')
  attempt = attempt + 1
  chosenLetter = input("Welchen Buchstaben wählen Sie? ").lower()

  index = 0
  while index != -1:                              #kommt der Buchstabe im wort vor wird er ins blind Wort eingetragen
    index = selectedWord.find(chosenLetter, index, len(selectedWord))
    if (index != -1):
      selectedWordblind[index] = chosenLetter
      index = index + 1

  stop = stestIsWordGuess()

print(f'+++++++++++++++++++++++++++++++++++++++++++++')
print(f'+++++++++++++++++++++++++++++++++++++++++++++')
print(f'Prima Sie haben das Wort: , {selectedWord}')
print(f'                ERRATEN:')
print(f'Anzahl der Versuche: , {attempt}')
print(f'+++++++++++++++++++++++++++++++++++++++++++++')
print(f'+++++++++++++++++++++++++++++++++++++++++++++')



