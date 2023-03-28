from pojistena_osoba import PojistenaOsoba
import os
def zobraz_menu():
    print("-------------------------------------")
    print("Evidence pojistenych")
    print("--------------------------------------")
    print("Vyberte si akci:")
    print("1 - Pridat nového pojisteného")
    print("2 - Vypsat vsechny pojistené")
    print("3 - Vyhledat pojisteného")
    print("4 - Konec")

#zadané osoby pro testování
pojistena_osoba = PojistenaOsoba("Petr", "Novák", 22 ,732444123)
pojistena_osoba.pridej_pojistenou_osobu()
pojistena_osoba = PojistenaOsoba("Pavel", "Novotný", 33 ,778244123)
pojistena_osoba.pridej_pojistenou_osobu()
pokracuj = True
while pokracuj:
    zobraz_menu()

    volba = int(input())

    if volba == 1:
        print("Zvolil jsi volbu 1.")
        jmeno = input("Zadejte jmeno pojisteného: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = input("Zadejte vek: ")
        tel_cislo = input("Zadejte telefonní číslo: ")
        poj_osoba = PojistenaOsoba(jmeno, prijmeni, vek, tel_cislo)
        print("Budou uložena data: {0} {1}, věk: {2}, tel.číslo: {3}".format(jmeno, prijmeni, vek, tel_cislo))
        poj_osoba.pridej_pojistenou_osobu()
        print("\n")
        input("Data byla uložena. Pokračujte klávesou enter ...")
        os.system('cls')

    elif volba == 2:
        print("Zvolil jsi volbu 2.")
        for poj_osoba in pojistena_osoba.get_seznam_pojistene_osoby():
            print(poj_osoba)
        print("")
        input("Pokračujte klávesou enter...")
        os.system('cls')

    elif volba == 3:
        print("Zvolil jsi volbu 3.")
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")
        pojistena_osoba.najdi_pojistenou_osobu(jmeno, prijmeni)
        print("")
        input("Pokračujte klávesou enter...")
        os.system('cls')

    elif volba == 4:
        print("Zvolil jsi volbu 4.")
        print("Aplikace bude ukončena.")
        pokracuj = False
    else:
        print("Opakuj volbu.")


