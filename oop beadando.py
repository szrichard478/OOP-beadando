from datetime import date, datetime

class Szoba:
    def __init__(self, szobaszam, szalloda):
        self.szobaszam = szobaszam
        self.szalloda = szalloda
        self.foglalva = []

    def foglal(self, datum):
        self.foglalva.append(datum)

    def lemond(self, datum):
        self.foglalva.remove(datum)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}

    def uj_szoba_felvetele(self, szobaszam):
        self.szobak[szobaszam] = Szoba(szobaszam, self)

    def foglalas(self, szobaszam, datum):
        if szobaszam in self.szobak:
            szoba = self.szobak[szobaszam]
            if datum >= date.today():
                foglalva = [f for f in szoba.foglalva if f >= date.today()]
                if datum not in foglalva:
                    szoba.foglal(datum)
                    return szoba
                else:
                    print("A szoba már foglalt ezen a napon.")
            else:
                print("Csak jövőbeli dátumot lehet megadni a foglaláshoz.")
        else:
            print("Nem található ilyen szobaszám a szállodában.")
        return None

    def foglalas_lemondasa(self, szobaszam, datum):
        if szobaszam in self.szobak:
            szoba = self.szobak[szobaszam]
            if datum in szoba.foglalva:
                szoba.lemond(datum)
                return True
            else:
                print("Nem található ilyen foglalás a megadott adatokkal.")
        else:
            print("Nem található ilyen szobaszám a szállodában.")
        return False

def feltoltes(szalloda):
    # Szobák létrehozása és hozzáadása a szállodához
    szalloda.uj_szoba_felvetele("102")
    szalloda.uj_szoba_felvetele("201")
    szalloda.uj_szoba_felvetele("301")

    # Foglalások létrehozása és hozzáadása a szobákhoz
    szalloda.foglalas("102", date(2024, 5, 10))
    szalloda.foglalas("102", date(2024, 5, 15))
    szalloda.foglalas("201", date(2024, 6, 20))
    szalloda.foglalas("301", date(2024, 7, 5))
    szalloda.foglalas("301", date(2024, 7, 10))

def main():
    szalloda = Szalloda("Luxus Palace")
    
    # Adatok feltöltése a szállodába
    feltoltes(szalloda)

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Kilépés")

        valasztas = input("Kérem válasszon (1-3): ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum_str = input("Adja meg a foglalás napját (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
                szoba = szalloda.foglalas(szobaszam, datum)
                if szoba:
                    print(f"A foglalás sikeres a(z) {szoba.szobaszam} szobára.")
            except ValueError:
                print("Hibás dátum formátum. Használja az ÉÉÉÉ-HH-NN formátumot.")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            datum_str = input("Adja meg a foglalás napját (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
                if szalloda.foglalas_lemondasa(szobaszam, datum):
                    print("A foglalás sikeresen lemondva.")
            except ValueError:
                print("Hibás dátum formátum. Használja az ÉÉÉÉ-HH-NN formátumot.")

        elif valasztas == "3":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérem válasszon 1 és 3 között.")


if __name__ == "__main__":
    main()
