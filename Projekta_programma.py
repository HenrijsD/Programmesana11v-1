
from math import *
def astonas_stundas():
    return 8-b


a=int(input("Sveiki, ludzu ievadiet savu vecumu - "))
b=int(input("ludzu ievadiet cik stundas Jus diennakti videji gulat - "))

if a<3: print("Dati nav pieejami")

if 3<=a<=5:
    print("Vecuma grupa no 3-5 gadi")
    
    if b<12:
        print("Jums butu jagul",12-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo neizguloties, cilvekam paaugstinas saslimsanas risks. \n Ja grutibas aizmigt iesakam: Pazeminat istabas temperaturu, neest pirms gulet iesanas, samazinat zilas gaismas saskarsmi pirms gulet iesanas, \n iet gulet regularos laikos un ar daudz citiem panemieniem.")
    elif b>13: print("Jus gulat par daudz")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    

if 6<=a<=13:
    print("Vecuma grupa no 6-13 gadi")
    
    if b<10:
        print("Jums butu jagul",10-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo neizguloties, cilvekam paaugstinas saslimsanas risks. \n Ja grutibas aizmigt iesakam: Pazeminat istabas temperaturu, neest pirms gulet iesanas, samazinat zilas gaismas saskarsmi pirms gulet iesanas, \n iet gulet regularos laikos un ar daudz citiem panemieniem.")
    elif b>15: print("Jus gulat par daudz")
    else: print("Jus gulat nepieciesamo miega daudzumu")

if 14<=a<=17:
    print("Vecuma grupa no 14-17 gadi")
        
    if b<9:
        print("Jums butu jagul",9-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo neizguloties, cilvekam paaugstinas saslimsanas risks. \n Ja grutibas aizmigt iesakam: Pazeminat istabas temperaturu, neest pirms gulet iesanas, samazinat zilas gaismas saskarsmi pirms gulet iesanas, \n iet gulet regularos laikos un ar daudz citiem panemieniem.")
    elif b>12: print("Jus gulat par daudz")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    
if 18<=a<=25:
    print("Vecuma grupa no 18-25 gadi")
        
    if b<8:
        print("Jums butu jagul",astonas_stundas(),"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo neizguloties, cilvekam paaugstinas saslimsanas risks. \n Ja grutibas aizmigt iesakam: Pazeminat istabas temperaturu, neest pirms gulet iesanas, samazinat zilas gaismas saskarsmi pirms gulet iesanas, \n iet gulet regularos laikos un ar daudz citiem panemieniem.")
    elif b>12: print("Jus gulat par daudz")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    
if 26<=a<=64:
    print("Vecuma grupa no 26-64 gadi")
            
    if b<8:
        print("Jums butu jagul",astonas_stundas(),"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo neizguloties, cilvekam paaugstinas saslimsanas risks. \n Ja grutibas aizmigt iesakam: Pazeminat istabas temperaturu, neest pirms gulet iesanas, samazinat zilas gaismas saskarsmi pirms gulet iesanas, \n iet gulet regularos laikos un ar daudz citiem panemieniem.")
    elif b>11: print("Jus gulat par daudz")
    else: print("Jus gulat nepieciesamo miega daudzumu")

if 65<=a<=200:
    print("Vecuma grupa 65+ gadi")
                
    if b<7:
        print("Jums butu jagul",7-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo neizguloties, cilvekam paaugstinas saslimsanas risks. \n Ja grutibas aizmigt iesakam: Pazeminat istabas temperaturu, neest pirms gulet iesanas, samazinat zilas gaismas saskarsmi pirms gulet iesanas, \n iet gulet regularos laikos un ar daudz citiem panemieniem.")
    elif b>11: print("Jus gulat par daudz")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    
if 155<a:
    print("Dati nav piejami sim vecumam")