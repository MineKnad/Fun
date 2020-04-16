
#06.05.2019 21:59 - Hallo, ich bin's, Konrad.
# Sieht schon ziemlich toll aus, es fehlen nur mehr ein paar Sachen
# Hauptsächlich eigentlich nur eine einzige Sache - Bauern dürfen sich 2 Felder bewegen, wenn Sie den ersten Zug machen.
# Hätte schon vorher einen changelog machen sollen.

#Alle funktionen:

#
# -alle Tests hier- nehmen 3 Argumente: position, ziel und farbe. Damit sagen sie, ob eine Figur von der position zum Ziel fahren darf.
#KönigTest()
#KöniginTest() - Setzt sich eigentlich aus TurmTest() und LäuferTest() zusammen
#BauerTest()
#LäuferTest()
#PferdTest()
#TurmTest()
#StandardProcedure() - in allen tests inkorporiert, testet auf generelle Sachen (out of borders, andere Figur schon da, Zug zur Startposition)

#MoveTest() - Damit wird der Zug "vollzogen", es prüft den return-Value von den oberen Tests und entscheidet dann.

#WelcherTest() - nimmt einen Figurennamen und sagt, welcher Test passt - z.B. "Turm" -> TurmTest()
#WelcheFarbe() - Gibt z.B. bei TurmS die Farbe "S", also Schwarz zurück

#PrintSpielfeld() - printet das Spielfeld in die Konsole, hat 2 modi

#PrintFarbe() - printet, welche Farbe die Figur hat

#FeldZähler() - Funktion von TurmTest() und LäuferTest(), schaut dass keine Figu im Weg ist
#FeldSucher() - Nimmt Koordinaten, z.B. (2,5) und gibt zurück, was dort zu finden ist - z.B. "BauerS"

#ConvertCoordinate() - nimmt Spieler-Koordinaten und wandelt sie um, z.B.  A 2 -> (0,3)




















#cool special settings

blackBegins = False
ignoreFarbe = False
ignoreCollisions = False
everyMovePossible = False
endWhenKingDied = True

FeldListe = [[[".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."]],

            [[".....",".....",".....",".....",".....",".....",".....","....."],
             [".....","LäuferW",".....",".....",".....","BauerS",".....","....."],
             [".....",".....","PferdS",".....","BauerW",".....",".....","....."],
             ["KönigS",".....",".....",".....","PferdS",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....","KönigW","....."],
             [".....",".....",".....",".....",".....",".....",".....","KönigS"],
             [".....","Turm W",".....",".....","KöniginS",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."]],

            [["Turm S","PferdS","LäuferS","KönigS","KöniginS","LäuferS","PferdS","Turm S"],
             ["BauerS","BauerS","BauerS","BauerS","BauerS","BauerS","BauerS","BauerS"],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             [".....",".....",".....",".....",".....",".....",".....","....."],
             ["BauerW","BauerW","BauerW","BauerW","BauerW","BauerW","BauerW","BauerW"],
             ["Turm W","PferdW","LäuferW","KönigW","KöniginW","LäuferW","PferdW","Turm W"]],

             [[".....", ".....", ".....", ".....", ".....", ".....", ".....", "....."],
              [".....", "BauerS", ".....", ".....", ".....", ".....", ".....", "....."],
              [".....", "Turm S", ".....", ".....", ".....", ".....", ".....", "....."],
              [".....", "KönigW", ".....", ".....", ".....", "Turm W", "PferdS", "....."],
              [".....", ".....", ".....", ".....", ".....", ".....", ".....", "....."],
              [".....", ".....", ".....", ".....", ".....", ".....", ".....", "....."],
              [".....", ".....", ".....", ".....", ".....", ".....", ".....", "....."],
              [".....", ".....", ".....", ".....", ".....", ".....", ".....", "....."]]]




def StandardProcedure(pos, ziel,farbe):


    # boundaries
    for i in (pos + ziel):
        if i > 8 or i < 0:
            return(1)

    #same position
    if(pos == ziel):
        return(3)

    #"Collisions"
    target = FeldSucher(ziel)
    if(target[len(target)-1] == farbe and ignoreCollisions == False):
        return(4)


####Figuren-Tests########################################################################################################



def KönigTest(pos, ziel, farbe):
    name = "König" + farbe
    x, y = pos
    x_, y_ = ziel

    if(StandardProcedure(pos, ziel, farbe)):
        return((StandardProcedure(pos, ziel, farbe), name, farbe))


    königList = ((x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                 (x - 1, y), ("Middle"), (x + 1, y),
                 (x - 1, y - 1), (x, y - 1), (x + 1, y - 1))

    try:
        königList.index(ziel)
        return ((0, name, farbe))
    except:
        return ((2, name, farbe))




#_______________________________________________________________________________________________________________________________

def TurmTest(pos, ziel, farbe):
    name = "Turm " + farbe
    x, y = pos
    x_, y_ = ziel

    if (StandardProcedure(pos, ziel, farbe)):
        return ((StandardProcedure(pos, ziel, farbe), name, farbe))

    # Bewegung in x und y - Richtung
    if(x == x_ and y != y_):
        if(y > y_):
            for i in range(FeldZähler(1, pos, ziel)):
                if (FeldSucher((x, y-(i+1))) != "....."):
                    print(FeldSucher((x, y-(i+1))), "ist im weg!")
                    return((5, name, farbe))
            return((0, name, farbe))

        elif (y < y_):
            for i in range(FeldZähler(1, pos, ziel)):
                if (FeldSucher((x, y + (i+1))) != "....."):
                    print(FeldSucher((x, y + (i+1))), "ist im weg!")
                    return ((5, name, farbe))
            return ((0, name, farbe))


    elif(y == y_ and x != x_):
        if (x > x_):
            for i in range(FeldZähler(2, pos, ziel)):
                if (FeldSucher((x - (i + 1), y )) != "....."):
                    print(FeldSucher((x - (i + 1), y )), "ist im weg!")
                    return ((5, name, farbe))
            return ((0, name, farbe))

        elif (x < x_):
            for i in range(FeldZähler(2, pos, ziel)):
                if (FeldSucher((x + (i + 1), y)) != "....."):
                    print(FeldSucher((x + (i + 1), y )), "ist im weg!")
                    return ((5, name, farbe))
            return ((0, name, farbe))




    else:
        return((2,name,farbe))



#_______________________________________________________________________________________________________________________________


def LäuferTest(pos, ziel,farbe):
    name = "Läufer" + farbe
    x, y = pos
    x_, y_ = ziel

    if (StandardProcedure(pos, ziel, farbe)):
        return ((StandardProcedure(pos, ziel, farbe), name,farbe))

    if(x-x_ == y-y_ or -(x-x_) == y-y_):
        print(FeldZähler(3, pos, ziel))

        if(x > x_):
            if(y > y_):
                #Links oben
                for i in range(FeldZähler(3, pos, ziel)):
                    if (FeldSucher((x - (i + 1), y - (i+1))) != "....."):
                        print(FeldSucher((x + (i + 1), y)), "ist im weg!")
                        return ((5, name, farbe))
                    return((0, name, farbe))

            else:
                #Links unten
                for i in range(FeldZähler(3, pos, ziel)):
                    if (FeldSucher((x - (i + 1), y + (i+1))) != "....."):
                        print(FeldSucher((x + (i + 1), y)), "ist im weg!")
                        return ((5, name, farbe))
                    return((0, name, farbe))

        else:
            if(y > y_):
                #Rechts oben
                for i in range(FeldZähler(3, pos, ziel)):
                    if (FeldSucher((x + (i + 1), y - (i+1))) != "....."):
                        print(FeldSucher((x + (i + 1), y)), "ist im weg!")
                        return ((5, name, farbe))
                    return((0, name, farbe))

            else:
                #Rechts unten
                for i in range(FeldZähler(3, pos, ziel)):
                    if (FeldSucher((x + (i + 1), y + (i + 1))) != "....."):
                        print(FeldSucher((x + (i + 1), y)), "ist im weg!")
                        return ((5, name, farbe))
                    return ((0, name, farbe))


        return ((0, name, farbe))
    else:
        return ((2, name, farbe))



#_______________________________________________________________________________________________________________________________


def KöniginTest(pos, ziel,farbe):
    name = "Königin" + farbe
    x, y = pos
    x_, y_ = ziel

    if (StandardProcedure(pos, ziel, farbe)):
        return ((StandardProcedure(pos, ziel, farbe), name, farbe))

    if (x == x_ and y != y_ or y == y_ and x != x_):
        r = TurmTest(pos, ziel, farbe)
        return(r[0], name, r[2])
    else:
        r = LäuferTest(pos, ziel, farbe)
        return (r[0], name, r[2])

#_______________________________________________________________________________________________________________________________


def BauerTest(pos, ziel,farbe):
    name = "Bauer" + farbe
    x, y = pos
    x_, y_ = ziel

    if(farbe == "W"):
        move = y-1
    else:
        move = y+1



    if (StandardProcedure(pos, ziel, farbe)):
        return ((StandardProcedure(pos, ziel, farbe), name,farbe))


    #Movement

    #Ein Zug nach vorne
    if(y_ == move and x_ == x):
        return((0, name, farbe))

    #Diagonaler Zug
    elif((x_ == x + 1 or x_ == x-1) and y_ == move):
        if(FeldSucher(ziel) != "....."):
            return ((0, name, farbe))
        else:
            return ((2, name,farbe))

    else:
        return ((2, name, farbe))



#_______________________________________________________________________________________________________________________________


def PferdTest(pos, ziel,farbe):
    name = "Pferd" + farbe
    x, y = pos
    x_, y_ = ziel


    if (StandardProcedure(pos, ziel, farbe)):
        return ((StandardProcedure(pos, ziel, farbe), name, farbe))


    pferdList = ((x + 1, y - 2), (x + 2, y - 1), (x + 2, y + 1),
                 (x + 1, y +2), ("Middle"), (x - 1, y - 2),
                 (x - 2, y - 1), (x -2, y + 1), (x - 1, y + 2))

    try:
        pferdList.index(ziel)
        return ((0, name,farbe))
    except:
        return ((2, name,farbe))


##################################################################################################################################################


def MoveTest(test, AmZug):

#Here is the code block for correct coordinates
    if(not test[0] or everyMovePossible):
        print("CORRECT")
        print(test[1], "\n")

        x,y = position
        x_,y_ = target


        spielFeld[y][x] = "....."
        spielFeld[y_][x_] = test[1]
        print("\nMove was Succesful!")






        if (test[1][0:len(test[1])-1] == "Bauer"):
            if(y_ == 0 or y_ == 7):
                print("Ein Bauer ist ans Ziel gelangt!")
                while True:
                    tauschList = ["Pferd", "Läufer", "Turm", "Königin"]
                    tauschen = int(input("Gegen welche Figur willst du ihn tauschen?\n\n1 = Pferd\n2 = Läufer\n3 = Turm\n4 = Königin\n"))
                    if(tauschen in [1, 2, 3, 4]):
                        spielFeld[y_][x_] = tauschList[tauschen-1] + test[2]
                        break
                    else:
                        print("Input a number from 1 to 4, it's not that hard!")


        #andere Farbe ist am Zug
        if(AmZug == "Weiß"):
            return("Schwarz")
        else:
            return("Weiß")



    elif(test[0] == 1):
        print("\nOut of boundaries!")

    elif (test[0] == 2):
        print("\nInvalid move!")

    elif (test[0] == 3):
        print("\nYou can't move to start position!")

    elif (test[0] == 4):
        print("\nOne figure is already there!")

    elif (test[0] == 5):
        print("\nA figure is blocking your way!")


    else:
        print("\nFor whatever reason, Invalid move!")
        print(test)
        print("Test-variable above me!")

#    printSpielfeld()


#nimmt einen Namen und entscheidet, welcher Test der richtige ist
def WelcherTest(figur):

    if(figur[:4] == "Turm"):
        return(TurmTest(position, target, WelcheFarbe(figur)))

    elif(figur[:5] == "Pferd"):
        return (PferdTest(position, target, WelcheFarbe(figur)))

    elif (figur[:7] == "Königin"):
        return (KöniginTest(position, target, WelcheFarbe(figur)))

    elif (figur[:5] == "König"):
        return (KönigTest(position, target, WelcheFarbe(figur)))

    elif (figur[:6] == "Läufer"):
        return (LäuferTest(position, target, WelcheFarbe(figur)))

    elif (figur[:5] == "Bauer"):
        return (BauerTest(position, target, WelcheFarbe(figur)))

    else:
        print(figur)
        return("Falsch!")



def WelcheFarbe(figur):
    if(figur[len(figur)-1] == "W"):
       return("W")

    elif(figur[len(figur)-1] == "S"):
       return("S")
    else:
       return("Unknown")


def PrintFarbe(f, mode = 0):
    if(WelcheFarbe(f) == "W"):
        if(mode):
            return("Weiß")
        else:
            print("Farbe: Weiß!")


    elif (WelcheFarbe(f) == "S"):
        if(mode):
            return("Schwarz")
        else:
            print("Farbe: Schwarz!")

    else:
        print("Keine Farbe!")



#####################################################################################

#Eine tolle Nebenfunktion
def FeldZähler(mode, pos, ziel):

#mode
# mode 1 - Turmbewegung in y-Richtung
# mode 2 -    --//--    in x-Richtung
# mode 3 - Läuferbewegung

    x, y = pos
    x_, y_ = ziel

    if(mode == 1):
        a = y - y_
        if(a<0):
            a = a * -1
        return(a-1)

    elif (mode == 2 or mode == 3):
        a = x - x_
        if (a < 0):
            a = a * -1
        return (a-1)

    else:
        print("Funktion \"Feldzähler\" wurde mit invalidem mode aufgerufen!")
        print("Argumente: mode=",mode," pos=",pos, " ziel=",ziel)




#Wandelt Buchstaben - Koordinaten in Zahlen um! z.B. A = 0, B = 1
def ConvertCoordinate(num):
    list = ("abcdefgh")
    try:
        a = list.index(num.lower())
    except:
        return(num, 1)
    else:
        return(a, 0)




#Gibt aus, was auf dem Feld zu finden ist (z.b. "König")
def FeldSucher(pos):
    x, y = pos
    return spielFeld[y][x]



#Printet das Spielfeld aus! (Mit hilfreichen Beschriftungen)
def PrintSpielfeld(mode = 1):
    if(mode):
        a = 1
        print("         [A]      [B]      [C]      [D]      [E]      [F]      [G]      [H]")
    else:
        a = 0
        print("         [0]      [1]      [2]      [3]      [4]      [5]      [6]      [7]")


    for reihe in spielFeld:
        print("[",a,"]", reihe)
        a += 1


########################################################################################


if(blackBegins):
    AmZug = "Schwarz"
else:
    AmZug = "Weiß"





spielFeld = FeldListe[1]



# Main Loop!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


while True:

    PrintSpielfeld()


######COORDINATE-INPUT!################################################
    position = []
    print("\n", AmZug, "ist am Zug")
    print("\nInput current position")

    i = ConvertCoordinate(input("x-koordinate:"))
    if(i[1]):
        print("Wrong! Your input was", i[0])
        continue
    position.append(int(i[0]))

    position.append(int(input("y-koordinate:"))-1)

    position = tuple(position)




    print("\n", FeldSucher(position), "ist auf diesem Feld!")
    PrintFarbe(FeldSucher(position))

    if (FeldSucher(position) == "....."):
        print("Das Feld ist doch leer!")
        continue

    if(PrintFarbe(FeldSucher(position), 1) != AmZug and not ignoreFarbe):
        print("Achtung,", AmZug, "ist am Zug!")
        continue


    target = []
    print("\nInput target position")

    j = ConvertCoordinate(input("x-koordinate:"))
    if (j[1]):
        print("Wrong! Your input was", j[0])
        continue

    target.append(int(j[0]))

    target.append(int(input("y-koordinate:"))-1)

    target = tuple(target)
########################################################################





#print(position)
#print("zu")
#print(target, "\n")




    if (FeldSucher(position) != "....."):
        ViewA = MoveTest(WelcherTest(FeldSucher(position)), AmZug)
        if(ViewA == "Schwarz" or ViewA == "Weiß"):
            AmZug = ViewA




    else:
        print("Das Feld ist doch leer!")











