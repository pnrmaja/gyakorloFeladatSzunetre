import math
def feladat1():
    szam=int(input("Kérek 200 és 920 között egy számot"))

    if (200<=szam and 920>=szam):
        print(szam//100)
    else:
        print("Hiba üzenet")

def feladat2(szam):
   tizedes=1
   while (szam>0):
       print(f"{tizedes} db: {szam%10}")
       tizedes*=10
       szam=szam//10

def feladat3(szam):
    osszeg=0
    szamalap=szam
    while (szam>0):
        osszeg+=szam%10
        szam=szam//10
    print(f"{szamalap} számjegyeink összege: {osszeg}")

def feladat4(szam):
    if (szam==1):
        print("Még 90% on vagyunk!")
    elif (szam==2 or szam==3):
        print("Még bírjuk (60%).")
    elif (szam>=4 and szam<=7):
        print("Progit tanulunk, töltődünk! 70%")
    elif (szam==8 or szam==9):
        print("Lassan nem bírjuk tovább! 50%")
    elif (szam==0):
        print("Be se jövök")
    else:
        print("Ez már tényleg túlzás.")

def feladat5(nap,ora):
    if ("hétfő"==nap):
        print("alszik")
    elif ("kedd"==nap):
        if (ora=="hittan"):
            print("figyel")
        else:
            print("alszik")
    elif ("szerda"==nap and ora=="programozás"):
        print("dolgozik")

    elif ("csütörtök"==nap):
        print("figyel")
    elif ("péntek"==nap):
        print("félig van jelen")
    else:
        print("nincs info")

def feladat6():
    szam= float(input("Kérek egy valós számot"))
    if (szam<0):
        print(f"Hiba üzenet")
    else:
        print(f"A szám négyzetgyöke {math.sqrt(szam)}")

def feladat7():
    szam= float(input("Kérek egy valós számot."))
    szam1= float(input("Kérek egyy másik valós számot."))
    if (szam>0 and szam1>0):
        kerulet=2*(szam+szam1)
        terulet= szam*szam1
        print(f"A téglalap kerülete: {kerulet:.2f}  A téglalap területe: {terulet:.2f}")

    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")

def feladatkiallitas():
    szektor=input("Kérek egy szektort")
    if (szektor=="A"):
        print("Nemzetközi Csarnok, World Conservation Forum 2021")
    elif (szektor=="B" or szektor=="E"):
        print("Kereskedelmi Csarnok ")
    elif (szektor=="C"):
        print("Konferencia-központ Innovációs Showroom")
    elif (szektor=="D"):
        print("Hal, Víz és Ember")
    elif (szektor=="F"):
        print("Hagyományos Vadászati Módok Csarnoka")
    elif (szektor=="G"):
        print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
    elif (szektor=="H"):
        print("Központi Magyar Kiállítás")
    elif (not szektor.isdigit()):
        print("Forduljon a pénztárhoz")
    else:
        print("HIBA: Adjon meg egy betűt A-H-ig!")

def feladat8():
    x=1
    while (x<=10):
        szorzat=x*10
        print(f"{x} x 10 = {szorzat}")
        x=x+1

def feladat9():
    db=0
    vaneA= "Nincs"
    leghosszabbNev=""
    nev= input("Kérek egy nevet")
    while (nev != "@"):
        db=db+1
        if (nev[0] == "A"):
            vaneA= "Van"
        if (len(leghosszabbNev)<len(nev)):
            leghosszabbNev=nev
        nev = input("Kérek egy nevet")

    print(f"Megadott nevek száma: {db}")
    print(f"Van-e benne A betűvel kezdődő név? {vaneA}")
    print(f"A leghosszabb név: {leghosszabbNev}")

def feladat10():
    x=0
    db=0
    leghosszabb=0
    elozoerme=""
    fsorozat=0
    while (x<10):
        erme=input("Pénzérme dobás eredménye: (f/i)")
        while (erme != "f" and erme!="i"):
            erme=input("Kérem újra az eredményt (f/i)")
        if (erme=="f"):
            db=db+1
            if(elozoerme=="f"):
                fsorozat=fsorozat+1
                if (fsorozat>leghosszabb):
                    leghosszabb=fsorozat
            else:
                fsorozat=1
        elozoerme=erme
        x=x+1
    print(f"f betűk száma: {db}")
    print(f"A leghosszabb f sorozat: {leghosszabb}")

def feladat11():
    szam=int(input("Kérek egy pozitív egész számot"))
    x=1
    osszeg=0
    while (x<=szam):
        if (szam % x ==0):
            osszeg=osszeg+x
        x=x+1

    if (osszeg==szam*2):
        print(f"Ez a szám tökéletes")
    else:
        print(f"Ez a szám nem tökéletes")

def feladat12(szam,szam2):
    lnko = 1
    x = 1
    if (szam>szam2):
            while(x<=szam2):
                if (szam % x ==0 and szam2 % x ==0):
                    lnko=x

                x=x+1

    else:
        while (x <= szam):
            if (szam % x == 0 and szam2 % x == 0):
                lnko = x

            x = x + 1
    if (lnko>1):
        print(f" A legnagyobb közös osztó: {lnko}")
    else:
        print("Nincs közös osztó")
def feladat12_a(szam,szam2):
    if (szam>szam2):
        feladat12_a(szam2,szam)
    else:
        lnko = 1
        x = szam
        while (x > 1):
            if (szam % x == 0 and szam2 % x == 0):
                lnko = x
                x = 1
            x = x - 1
        if (lnko>1):
            print(f" A legnagyobb közös osztó: {lnko}")
        else:
            print("Nincs közös osztó")

def feladat13(szam,szam1):

    if (szam<szam1):
        feladat13(szam1,szam)
    else:
        lkkt = szam * szam1
        x=szam
        while (x < lkkt):
            if (x % szam==0 and x % szam1==0):
                lkkt=x
            x=x+1
        print(f" A legkisebb közös többszörös: {lkkt}")
