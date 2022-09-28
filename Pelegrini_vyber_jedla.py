import tkinter #knižka
canvas=tkinter.Canvas(width=710,height= 200) #velkost platna
canvas.pack() #platno

green=canvas.create_rectangle(10,10,180,180, fill='green',outline='green')#vyklreslenie zeleneho stvorca
read=canvas.create_rectangle(190,10,360,180, fill='red',outline='red')#vykreslenie cerveneho stvorca
blue=canvas.create_rectangle(370,10,530,180, fill='blue',outline='blue')#vykreslenie modreho stvorca
orange=canvas.create_rectangle(540,10,700,180, fill='orange',outline='orange')#vykreslenie oranzoveho stvorca

if Button-1 click on read:#ak sa kliklo na cervenu
    color=read #farba sa nastavila na cervenu
else:
    if Button-1 click on blue: #ak sa kliklo na modru
        color=blue #farba sa nastavila na modru
    else:
        if Button-1 click on green: #ak sa kliklo na zelenu
            color=green #farba sa nastavil an zelenu
        else:
            color=orange #farba sa nastavila na oranzovu
            
def jedlo(): #funkcia na jedlo
    subor=open('jedla.txt','w') #otvorenie suboru pre zapis jedla a cisla studenta
    subor.write(entry1+'/color') #zapise do suboru cislo studenta a jedlo ake si
    
entry1=tkinter.Entry() #štvorček na písanie
entry1.pack() #štvorček
button1=tkinter.Button(text='identifikačné číslo študenta') #spravi sa tlačidlo
button1.pack() #tlačitko
canvas.bind('<Button-1>',jedlo) #nastavenie klikania