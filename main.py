
OrdlisteFil = open("nsf2016/nsf2016.txt", "r")
Ordlisten = OrdlisteFil.readlines()
OrdlisteFil.close()


#fikser slik at listen før riktige æ,ø og å. Av en eller annen grunn blir disse rare når
# man henter ut filen, fjerner også et melomrom som er etter alle ordene
for i in range(len(Ordlisten)):
        Ordlisten[i] = Ordlisten[i][:-1]
        if "Ã¥" or "Ã¸" or "Ã¦" in Ordlisten[i]:
                Ordlisten[i] = (Ordlisten[i].replace("Ã¥", "å"))
                Ordlisten[i] = (Ordlisten[i].replace("Ã¸", "ø"))
                Ordlisten[i] = (Ordlisten[i].replace("Ã¦", "æ"))


antallBokstaver = int(input("Hvor mange bokstaver innehloder ordet ditt? "))
forlopigGjettetOrd = []
for i in range(antallBokstaver):
        forlopigGjettetOrd.append("_")
print(forlopigGjettetOrd)

alfabet = "abcdefghijklmnopqrstuvwxyzæøå"

def fjernOrd(gammelOrdliste):
        oppdatertOrdliste = []
        for i in range(len(gammelOrdliste)):

                if not len(gammelOrdliste[i]) == antallBokstaver:
                        gammelOrdliste[i] = ""
                else:
                        oppdatertOrdliste.append(gammelOrdliste[i])
        return oppdatertOrdliste

Ordlisten = fjernOrd(Ordlisten)

def finnBokstaverSomMaVaereIOrdene(ordene, gammelt, gjettetBokstaver):

        for k in range(len(gammelt)):
                plassering = []
                for i in range(len(alfabet)):
                        alfa = 0
                        if not alfabet[i] in (gjettetBokstaver and gammelt):
                                for j in range(len(ordene)):
                                        if alfabet[i] == ordene[j][k]:
                                                alfa += 1
                        if alfa == len(ordene):
                                gjettetBokstaver += alfabet[i]
                                plassering.append(k+1)
                                gammelt = oppdaterForlopigGjettetOrd(gammelt, plassering, alfabet[i])
        return gammelt
def finnMestVanligBokstav(ordene, gjettetBokstaver, forlopigGjettetOrd):
        storst = 0
        mestVanligBoksav = ""
        alfa = []
        for i in range(len(alfabet)):
                alfa.append(0)

        for j in range(len(ordene)):
                for i in range(len(alfabet)):
                        if alfabet[i] in ordene[j]:
                                alfa[i] += 1

        for i in range(len(alfabet)):
                if alfa[i] > storst:
                        if not alfabet[i] in (gjettetBokstaver and forlopigGjettetOrd):
                                storst = alfa[i]
                                mestVanligBoksav = alfabet[i]
        return mestVanligBoksav

def finnHvorBoksavER():
        hvorMange = int(input("Hvor mange? "))
        plassering = []
        for i in range(hvorMange):
                sted = int(input("Plassering" + str(i + 1) + " "))
                plassering.append(sted)
        return plassering

def oppdaterOrdListeFraBokstavplasering(plassering, gammelOrdliste, vanligBokstav, forlopigGjettetOrd):
        oppdatertOrdliste =[]
        for i in range(len(gammelOrdliste)):
                for j in range(len(forlopigGjettetOrd)):
                        if gammelOrdliste[i] != "":
                                if forlopigGjettetOrd[j] == "_":
                                        if gammelOrdliste[i][j] == vanligBokstav:
                                                gammelOrdliste[i] = ""
                                elif forlopigGjettetOrd[j] != gammelOrdliste[i][j]:
                                        gammelOrdliste[i] =""

        for i in range(len(gammelOrdliste)):
                if gammelOrdliste[i] != "":
                        oppdatertOrdliste.append(gammelOrdliste[i])

        return oppdatertOrdliste

def oppdaterForlopigGjettetOrd(gammelt, plassering, vanligBokstav):
        for i in range(len(gammelt)):
                if (i + 1) in plassering:
                        gammelt[i] = vanligBokstav
        return gammelt

def oppdaterOrdlistenAvBokstaverSomIkkeErDer(gammelOrdliste, vanligBokstav):
        oppdatertOrdliste =[]

        for i in range(len(gammelOrdliste)):
                if not vanligBokstav in gammelOrdliste[i]:
                        oppdatertOrdliste.append(gammelOrdliste[i])

        return oppdatertOrdliste

spill = True
gjettetBokstaver = ""
while spill:
        vanligBokstav = finnMestVanligBokstav(Ordlisten, gjettetBokstaver, forlopigGjettetOrd)
        gjettetBokstaver += vanligBokstav
        jaNei = input("Er \"" + str(vanligBokstav) + "\" i ordet? ")
        if jaNei == "ja":
                plasseringene = finnHvorBoksavER()
                forlopigGjettetOrd = oppdaterForlopigGjettetOrd(forlopigGjettetOrd, plasseringene, vanligBokstav)
                Ordlisten = oppdaterOrdListeFraBokstavplasering(plasseringene, Ordlisten, vanligBokstav, forlopigGjettetOrd)
                forlopigGjettetOrd = finnBokstaverSomMaVaereIOrdene(Ordlisten, forlopigGjettetOrd, gjettetBokstaver)
                print(forlopigGjettetOrd)

        elif jaNei =="nei":
                Ordlisten = oppdaterOrdlistenAvBokstaverSomIkkeErDer(Ordlisten, vanligBokstav)
                forlopigGjettetOrd = finnBokstaverSomMaVaereIOrdene(Ordlisten, forlopigGjettetOrd, gjettetBokstaver)
                print(forlopigGjettetOrd)
        if len(Ordlisten) < 20:
                print(Ordlisten)

        if len(Ordlisten) == 1:
                spill = False
                print("Ditt ord er: " + Ordlisten[0])
        if len(Ordlisten) == 0:
                spill = False
                print("Ditt ord finnes ikke i ordregisteret")








'''
alfabet = "abcdefghijklmnopqrstuvwxyzæøå"
antallBokstaver = int(input("Antall bokstaver i ordet? "))


def riktigOrd(jaNei, hvor):
        riktigOrd = []
        for i in range(antallBokstaver):
                if jaNei =="ja" and hvor == (i + 1):
                        riktigOrd.insert(i, mestVanligBokstav[-1])
                else:
                        riktigOrd.insert(i, "-")
        return riktigOrd

antallMulige = len(Ordlisten)
alfa = []
mestVanligBokstav = ""
antallriktigebokstaver = 0

for i in range(len(alfabet)):
        alfa.insert(i, [str(alfabet[i]), 0])

def resetAlfa():
        for i in range(len(alfabet)):
                alfa[i] = [alfabet[i], 0]
#Lager en arrey som inneholder alfabetet med en verdi

resetAlfa()

#fjerner ord uttenfor listen
for i in range(len(Ordlisten)):
        if len(Ordlisten[i]) != antallBokstaver:
                Ordlisten[i] = ""
                antallMulige -= 1

#velg mest vanlig bokstav
def denMestVanligBokstav():
        for i in range(len(Ordlisten)):
                if len(Ordlisten[i]) == antallBokstaver:
                        for j in range(len(Ordlisten[i])):
                                for k in range(len(alfabet)):
                                        if alfa[k][0] == Ordlisten[i][j]:
                                                alfa[k][1] += 1
        forlopigstorst = ""
        storstverdi = 0
        for i in range(len(alfabet)):
                if alfa[i][1] > storstverdi and not alfa[i][0] in mestVanligBokstav:
                        storstverdi = alfa[i][1]
                        forlopigstorst = alfa[i][0]
        return  forlopigstorst

mestVanligBokstav += denMestVanligBokstav()

def fjernOrd(a, jaNei, hvor):
        #Fjerner ordene som ineholder bokstavene
        for i in range(len(Ordlisten)):
                if not Ordlisten[i] == "":
                        if jaNei == "nei":
                                if mestVanligBokstav[-1] in Ordlisten[i]:
                                        Ordlisten[i] = ""
                                        a -=1
                                #else:
                                        #print(Ordlisten[i])

                        elif jaNei == "ja":
                                if not mestVanligBokstav[-1] == Ordlisten[i][(hvor-1)]:
                                        Ordlisten[i] = ""
                                        a -=1
                                #else:
                                        #print(Ordlisten[i])
        return a

#sjekk om bokstav er gjettet
loop = True
hvorMange = 0
hvor = 0
while loop:


        jaNei = input("Er \"" + mestVanligBokstav[-1] + "\" en boksatv i ordet? (ja/nei): ")
        if jaNei == "ja":
                #hvorMange = int(input("Hvor mange er det av denne bokstaven? "))
                #for i in range(hvorMange):
                hvor = int(input("Plassering: "))
        fjernOrd(antallMulige, jaNei, hvor)
        print(riktigOrd(jaNei, hvor))
        antallMulige = 0
        for i in range(len(Ordlisten)):
                if not Ordlisten[i] == "":
                        antallMulige +=1
        if antallMulige == 1:
                for i in range(len(Ordlisten)):
                        if not Ordlisten[i] == "":
                                print("Ditt ord er: " + Ordlisten[i])
                                loop = False
                break


        if jaNei == "ja":
                antallriktigebokstaver += 1

        if antallriktigebokstaver == antallBokstaver:
                print("En av disse ordene: ")
                for i in range(len(Ordlisten)):
                        if not Ordlisten[i] == "":
                                print(Ordlisten[i])
                break
        else:
                resetAlfa()
                mestVanligBokstav += denMestVanligBokstav()

'''
