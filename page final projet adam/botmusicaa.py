import pyautogui,time
#il faut installer le package pyautogui avant de lancer le bot
jojo=['j','v','v','b','n','b','v','f','v','b','j','l' ,'(','f','v','b','v','f',';',',','j']
sil=[')','f','v','v','f','v','b','b','b','j','b','v','b','v','p','v','j','j','b','v','b','b','p','f',',',',','j','b','j','b','v','si+',';','v','si+',';','v','v','f','v','b','j','v']
moz=['u','u','u','r','y','t','e','t','y','r','y','t','e','y','t','r']
tch=['o','o','t','7','7','0','0','y','i','o','o','t','7','7','0','0','y','i','o','o','t','7','7','0','0','y','i','o','o','t','7','7','0','0','y','i''o','o','t','7','7','0','0','y','i','o','o','t','7','7','0','0','y','i']
bonus=['do','do']
def press(touche):

    
    pyautogui.keyDown(touche)
    pyautogui.keyUp(touche)
    
    
    
def click(x,y):
    
    pyautogui.click(x,y)
    
    pass
def note_vers_touche(note):
    dico={
    "do-":'w',
    "doré-":'s',
    "ré-":'x',
    "rémi-":'d',
    "mi-":'c',
    "fa-":'a',
    "fasol-":'é',
    "sol-":'z',
    "solla-":'"',
    "la-":'e',
    "lasi-":"'",
    "si-":'r',
    "do":'t',
    "doré":'-',
    "ré":'y',
    "rémi" :'7',
    "mi":'u',
    "fa":'i',
    "fasol":'ç',
    "sol":'o',
    "solla":'0',
    "la":'p',
    "lasi":'=',
    "si":')',
    "do+":'^',
    "doré+":'f',
    "ré+":'v',
    "rémi+":'g',
    "mi+":'b',
    "fa+":'n',
    "fasol+":'j',
    "sol+":',',
    "solla+":'k',
    "la+":';',
    "lasi+":'l'
   }
    return dico[note]

def piano(note):
    touche = note_vers_touche(note)
    press(touche)
    
click(1097,512)


while len(jojo)!=0 :
    for i in range(11):
        if len(jojo)!=0:
            note = jojo.pop(0)
            press(note)
click(1704,754)

time.sleep(3)


while len(sil)!=0 :
    for i in range(11):
        if len(sil)!=0:
            note = sil.pop(0)
            press(note)
click(1704,754)



time.sleep(3)


while len(moz)!=0 :
    for i in range(11):
        if len(moz)!=0:
            note = moz.pop(0)
            press(note)
        
time.sleep(3)

while len(tch)!=0 :
    for i in range(11):
        if len(tch)!=0:
            note = tch.pop(0)
            press(note)

            
time.sleep(3)
while len(bonus)!=0 :
    for i in range(11):
        if len(bonus)!=0:
            note = bonus.pop(0)
            piano(note)
