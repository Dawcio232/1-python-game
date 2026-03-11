#-=IMPORTS=-
import random
#====
#-=ZMIENNE=-
odp = 0
level = 0
akt_tryb = 0
a = 0
b= 0
wynik = 0
punkty = 0
il_poziom = 0
zakres1 = 0
zakres2 = 0
wygrana = 0
przegrana = 0
#====
#-=START=-
print("Cześć! Witaj w tescie tabliczki mnożenia!") 
print("Wybierz tryb:\n1.Easy \n2.Normal \n3.Medium\n4.Hard\n5.Extreme")
odp = int(input("Wybierz tryb od 1 do 5: \n"))
#--Presetowanie trybów--
if odp == 1:
    akt_tryb = 1
    print("Bambik. Wybrałeś: Łatwy")
    punkty = 0
    il_poziom = 4
    wygrana = 1
    przegrana = 0
    zakres1 = 0
    zakres2 = 5
elif odp == 2:
    akt_tryb = 2
    print("Człowiek. Wybrałeś:Normalny")
    il_poziom = 5
    zakres1 = 1
    zakres2 = 10
    wygrana = 1
    przegrana = 0
elif odp == 3:
    akt_tryb = 3
    print("Kujon. Wybrałeś: średni")
    il_poziom = 7
    zakres1 = 1
    zakres2 = 20
    wygrana = 1
    przegrana = 1
elif odp == 4:
    akt_tryb = 4
    print("Baba z Matmy. Wybrałeś: Trudny")
    il_poziom = 10
    zakres1 = 6
    zakres2 = 80
    wygrana =  1
    przegrana = 1
elif odp == 5:
    akt_tryb = 5
    print("AI. Wybrałeś Extreme. Powodzonka.")
    il_poziom = 20
    zakres1 = 11
    zakres2 = 200
    wygrana = 1
    przegrana = 2
elif odp == 67:
    akt_tryb = 6
    print("DEBUG Wybrałeś:", akt_tryb)
    punkty = int(input("punkty:\n"))
    il_poziom = int(input("ilosc poziom:\n"))
    zakres1 = int(input("od\n"))
    zakres2 = int(input("do\n"))
    wygrana = int(input("wygrana\n"))
    przegrana = int(input("przegrana\n"))
#-------------------------------
#--MAINFRAME--
print("")
for i in range(il_poziom):
    a = random.randint(zakres1, zakres2)
    b = random.randint(zakres1, zakres2)
    odp = 0
    level = level + 1
    print("Oblicz", a, "razy", b, ".")
    odp = int(input("Twoja odpowiedz: "))
    if odp == a * b:
        print("\nBrawo! Zdobywasz", wygrana, "punkt!")
        punkty = punkty + wygrana
    else:
        print("\nŹle! Przegrywasz:", przegrana)
        punkty = punkty - przegrana
    print("\nAktualnie masz:", punkty, "punktów. Jest to:", level, "poziom\n")
#---------------
#--End--
print("\n\nKoniec. Grałeś:", level, "leweli. Miałeś:", punkty, "punktów.")
#------------
print("")
#--Ocena--
if punkty < 0:
    print("Czabyło nie grać w takie gry. Ocena: -1")
elif punkty == 0:
    print("Jesteś bardzo głupi albo zrobiłeś to specialnie.")
elif punkty < 3 and punkty > 0:
    print("Poszło ci marnie. ocena 2.")
elif punkty < 5 and punkty > 3:
    print("Poszło ci nieźle ale jeszcze potrenuj. ocena 4.")
elif punkty == 5:
    print("BRAWO dostałeś dość dużo punktów. Ocena 6")
elif punkty > 5:
    print("HACKER chłopie. nie miałeś tyle dostać. To nie możliwe. Jesteś panią z matematyki czy co? Zapisz to lepiej w kalendarzu jak zhakowałeś gre matemqtyczną!")

   
