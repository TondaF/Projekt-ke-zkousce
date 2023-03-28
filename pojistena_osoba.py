class PojistenaOsoba:
    _seznam_pojistene_osoby = list()


    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._tel_cislo = tel_cislo

    def __str__(self):
        return "Data: {0} {1}, věk: {2}, tel.číslo: {3}".format(self._jmeno, self._prijmeni, self._vek, self._tel_cislo)

    def pridej_pojistenou_osobu(self):
        PojistenaOsoba._seznam_pojistene_osoby.append(self)

    def get_seznam_pojistene_osoby(self):
        return PojistenaOsoba._seznam_pojistene_osoby


    def najdi_pojistenou_osobu(self, jmeno, prijmeni):
        for i in PojistenaOsoba._seznam_pojistene_osoby:
            if prijmeni == i._prijmeni and jmeno == i._jmeno:
                nalezen = True
                print("Hledaná osoba je {0} {1} věk: {2}, tel.číslo: {3}".format(i._prijmeni, i._jmeno, i._vek, i._tel_cislo))
                break
            else:
                nalezen = False
        if nalezen == False:
            print("Hledaná osoba není v seznamu pojištěnců.")


