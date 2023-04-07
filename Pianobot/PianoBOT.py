import pyautogui,time
import tkinter as tk
from tkinter import Entry, Button

#il faut installer le package pyautogui,tkinter et time avant de lancer le bot
moz=['do','do','do','ré','fa','la','sol','fa','do','si','si','ré','la','la','la','fa']

def press(touche):

    
    pyautogui.keyDown(touche)
    pyautogui.keyUp(touche)
    
    
    
def click(x,y):
    
    pyautogui.click(x,y)
    
    pass
def note_vers_touche(note):
    dico={
    "do-":'a',
    "doré-":'z',
    "ré-":'e',
    "rémi-":'r',
    "mi-":'t',
    "fa-":'y',
    "fasol-":'u',
    "sol-":'i',
    "solla-":'o',
    "la-":'p',
    "lasi-":"q",
    "si-":'s',
    "do":'d',
    "doré":'f',
    "ré":'g',
    "rémi" :'h',
    "mi":'j',
    "fa":'k',
    "fasol":'l',
    "sol":'m',
    "solla":'w',
    "la":'x',
    "lasi":'c',
    "si":'v',
    "do+":'b',
    "doré+":'n',
    "ré+":',',
    "rémi+":';', "mi+":'!',
   }
    return dico[note]

def piano(note):
    touche = note_vers_touche(note)
    press(touche)
    


def test():
    click(400,212)
    # boucle qui lance la liste moz          
    while len(moz)!=0 :
        for i in range(15):
            if len(moz)!=0:
                note = moz.pop(0)
                piano(note)
                time.sleep(0.2)         



def jouer_les_note():
    # Récupérer la valeur entrée dans le widget Entry
    notes_str = note_entre.get()
    notes_str2 = note_entre2.get()
    notes_str3 = note_entre3.get()
    # Séparer les valeurs en utilisant la virgule comme séparateur
    notes = notes_str.split(",")
    notes2 = notes_str2.split(",")
    notes3 = notes_str3.split(",")
    # Ajouter les notes à la liste
    click(400,212)
    def jouer(notes):
        for note in notes:
        # Enlever les espaces éventuels autour des notes
            note = note.strip()
            piano(note)
            time.sleep(0.5)
    jouer(notes)
    time.sleep(3)
    jouer(notes2)
    time.sleep(3)
    jouer(notes3)      

#création de l'interface grafique
root = tk.Tk()
root.title("Piano BOT")
root.iconphoto(False, tk.PhotoImage(file="icon.png"))


note_label1 = tk.Label(root, text="music 1 entre les note:")
note_entre = Entry(root)
note_label1.pack()
note_entre.pack()

note_label2 = tk.Label(root, text="music 2 entre les note:")
note_entre2 = Entry(root)
note_label2.pack()
note_entre2.pack()

note_label3 = tk.Label(root, text="music 3 entre les note:")
note_entre3 = Entry(root)
note_label3.pack()
note_entre3.pack()

jouer_button = Button(root, text="Jouer", command=jouer_les_note)
jouer_button.pack()

exemple_button = Button(root, text="Exemple", command=test)
exemple_button.pack()

root.mainloop()

