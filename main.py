from datetime import datetime
tid = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



class Produkter:
    def __init__(self, id, namn, pris):
        self.id = id
        self.namn = namn
        self.pris = pris


produkt100 = Produkter(id="100", namn="Lax ", pris=120)
produkt150 = Produkter(id="150", namn="Sallad", pris=10)
produkt200 = Produkter(id="200", namn="Kycklingfilé", pris=130)
produkt250 = Produkter(id="250", namn="Fläskfilé", pris=100)
produkt300 = Produkter(id="300", namn="Lammkött", pris=140)
produkt350 = Produkter(id="350", namn="Ägg", pris=60)
produkt400 = Produkter(id="400", namn="Mjölk", pris=15)
produkt450 = Produkter(id="450", namn="Smör", pris=40)
produkt500 = Produkter(id="500", namn="Gurka", pris=10)
produkt550 = Produkter(id="550", namn="Bröd", pris=23)
produkt600 = Produkter(id="600", namn="Potatis", pris=10)

alla_produkter = {
    "100": produkt100,
    "150": produkt150,
    "200": produkt200,
    "250": produkt250,
    "300": produkt300,
    "350": produkt350,
    "400": produkt400,
    "450": produkt450,
    "500": produkt500,
    "550": produkt550,
    "600": produkt600,
}


class Kassa:
    def __init__(self, produkter):
        self.produkter = produkter

    def kör_kassan(self):
        kundkorg = []

        while True:
            print("\n--- KASSA ---")
            print("Tillgängliga produkter:")
            for p in self.produkter.values():
                print(f"{p.id}: {p.namn} - {p.pris} kr")

            print("\nSkriv: <produkt_id> <antal> (t.ex. 100 2)")
            print("Skriv PAY för att betala")
            print("Skriv EXIT för att gå tillbaka till huvudmenyn")

            val = input("Välj: ").strip().upper()

            if val == "PAY":
                total = 0
                print("\n--- KVITTO  ---")

                #___datum o tid___
                tidpunkt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Datum och tid: {tidpunkt}")

                for produkt, antal in kundkorg:
                    summa = produkt.pris * antal  
                    total = total + summa                 
                    print(f"{produkt.namn} x {antal} = {summa} kr")

                print(f"TOTALT: {total} kr")
                print("Tack för ditt köp!")
                break

            elif val == "EXIT":
                print("Tillbaka till huvudmenyn.")
                break

            else:
                
                try:
                    produkt_id, antal_text = val.split()
                except ValueError:
                    print("Fel format. Använd t.ex. 100 2")
                    continue

                if produkt_id not in self.produkter:
                    print("Ogiltigt produkt_id.")
                    continue

                
                try:
                    antal = int(antal_text)
                except ValueError:
                    print("Antal måste vara ett heltal.")
                    continue

                produkt = self.produkter[produkt_id]
                kundkorg.append((produkt, antal))
                print(f"Lade till {antal} st {produkt.namn} i kundkorgen.")

    def admin_meny(self):
        print("\n--- ADMINMENY ---")
        print("1. ✅ Lägga till produkt")
        print("2. ❌ Ta bort produkter")
        print("0. tillbaka till huvudmenyn")

        while True:
            välja = input(" >:  ")

            
            if välja == "0":
                break

            # LÄGGA TILL PRODUKT
            elif välja == "1":
                
                while True:
                    ny_id = input("produkt id: ")
                    if ny_id in alla_produkter:
                        print("produkt id finns redan!⛔ skriv ett annat.")
                        continue
                    if not ny_id.isdigit():
                        print ("fel!⛔ OBS: produkt id måste vara siffror")

                    else:
                        break

                ny_namn = input("produkt namn: ")
                ny_pris = input("produkt pris: ")

                
                ny_produkt = Produkter(int (ny_id), ny_namn, int(ny_pris))
                alla_produkter[ny_id] = ny_produkt

                print("produkten lade till!✅")

                import json

                with open("produkter.json", "w") as fil:
                 json.dump({id: vars(p) for id, p in alla_produkter.items()}, fil)

            # TA BORT PRODUKT
            elif välja == "2":
                
                while True:
                    tabort_id = input("skriv produkt id (0 = avbryt): ")

                    if tabort_id == "0":
                        break

                    if tabort_id in alla_produkter:
                        alla_produkter.pop(tabort_id)
                        print("Produkten har tagits bort ✅.")
                        break
                    else:
                        print("Produkt-id finns inte ⛔, försök igen .")

            else:
                print("Ogiltigt val ❌")


def huvudmeny():
    kassa = Kassa(alla_produkter)

    while True:
        print("\nHUVUDMENY")
        print("1. 🛒 Kassa")
        print("2. 🧩🔧 Admin")
        print("0. ❌ Avsluta")
        val = input("Välj (0-2): ")

        if val == "0":
            print("Programmet avslutas ❌.")
            break
        elif val == "1":
            kassa.kör_kassan()
        elif val == "2":
            kassa.admin_meny()
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
    huvudmeny()
    