#Menù principale del programma: scrive all'interno di un file csv le coordinate

def printmenu():
    print("Benvenuto nel menù principale del programma")
    print("")
    print("Scegli una tra queste opzioni")
    print("  [0] Collaboratori e informazioni")
    print("  [1] Gestisci le coordinate del triangolo e 4° punto")
    print("  [2] Entra nel programma")
    print("")

def collab():
    print("Hanno collaborato al programma:")
    print("- Federico Scutariu")
    print("- Leonard Ifrim")
    print("- Eros Morozan")
    print("- Mattia Bresciani")
    print("- Gurvinder Karra")
    print("- Klejton Haxhiraj")
    print("- Paola Improta")
    print("- Dante Bertagnoli")
    print("")
    print("Si ringrazia l'aiuto della Prof.ssa Marchesini Cinzia")
import os
def gestfile():
    #f=open("coordinate.csv", "a") #apro il file in append così, in caso non esistesse, lo crea
    #f.close()
    
    try: #prova ad aprire il file in modalità lettura
        f=open("coordinate.csv", "r")
        riga = f.readline
        if riga!="":
            print("File esistente, sostituire i valori? S/N")
            scelta=input("    >>      ")
            if scelta == "N" or scelta == "n":
                printmenu()
                scelta=int(input("      >>      "))
            elif scelta =="s" or scelta =="S":
                f.close()
                os.remove("coordinate.csv")
                f=open("coordinate.csv", "a") #apro il file in append così, in caso non esistesse, lo crea
                for i in range(0, 4, 1):
                    print("Inserisci le coordinate x del ", i+1 ,"° punto")
                    coord1=float(input("   >>       "))
                    print("Inserisci le coordinate y del ", i+1 ,"° punto")
                    coord2=float(input("   >>       "))
                    finalcoord = str(coord1) + "," + str(coord2)+ "\n"
                    f.write(finalcoord)
                f.close() 
       

        
        f.close()
        return scelta 
    except FileNotFoundError as e: #se non esiste: (errore: FIleNotFoundError)
        f=open("coordinate.csv", "a") #apro il file in append così, in caso non esistesse, lo crea
        for i in range(0, 4, 1):
            print("Inserisci le coordinate x del ", i+1 ,"° punto")
            coord1=float(input("   >>       "))
            print("Inserisci le coordinate y del ", i+1 ,"° punto")
            coord2=float(input("   >>       "))
            finalcoord = str(coord1) + "," + str(coord2)+ "\n"
            f.write(finalcoord)
        f.close()    

    f.close()

printmenu()
scelta=int(input("      >>      "))

while(scelta!=0)and(scelta!=1)and(scelta!=2):
    print("")
    print("!ERRORE!")
    print(scelta, " non è un comando definito")
    print("")
    scelta=int(input("Reinserisci  >>      "))

if scelta==0:
    collab()

if scelta==1:
    gestfile()