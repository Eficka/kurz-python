from typing import Dict, List

class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self) -> str:
        return f"Zvire druhu {self.druh} se jmenuje {self.jmeno} a vazi {self.vaha}."
    
    def export_to_dict(self) -> Dict:
        slovnik = {
            "jmeno" : self.jmeno,
            "druh" : self.druh,
            "vaha" : self.vaha
        }
        return slovnik

class Zamestnanec:
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice: str):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice
    
    def __str__(self) -> str:
        return f"Zamestnanec {self.cele_jmeno} na pozici {self.pozice} ma rocni plat {self.rocni_plat}."
    
    def ziskej_inicialy(self) -> str:
        jmena = self.cele_jmeno.split(" ")
        inicialy = [jmeno[0].upper() for jmeno in jmena]
        spojene_inicialy = ".".join(inicialy)
        return f"{spojene_inicialy}."

class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno: str, rocni_plat: int, oblibene_zvire: Zvire):
        super().__init__(cele_jmeno, rocni_plat, "Reditel")
        self.oblibene_zvire = oblibene_zvire

class Zoo:
    def __init__(self, jmeno: str, adresa: str, reditel: Reditel, zamestnanci: List[Zamestnanec], zvirata: List[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

    def vaha_vsech_zvirat_v_zoo(self) -> float:
        soucet_vahy: float = 0.0
        for zvire in self.zvirata:
            soucet_vahy += zvire.vaha
        return soucet_vahy
    
    def mesicni_naklady_na_zamestnance(self) -> float:
        soucet_platu: float = 0.0
        for zamestnanec in self.zamestnanci:
            soucet_platu += (zamestnanec.rocni_plat / 12)
        soucet_platu += (self.reditel.rocni_plat / 12)
        return soucet_platu


zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

zvirata = []

for zvire_dict in zvirata_dict:
    zvire = Zvire(zvire_dict["jmeno"], zvire_dict["druh"], zvire_dict["vaha"])
    zvirata.append(zvire)


zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

zamestnanci = []

for zamestnanec_dict in zamestnanci_dict:
    zamestnanec = Zamestnanec(zamestnanec_dict["cele_jmeno"], zamestnanec_dict["rocni_plat"], zamestnanec_dict["pozice"])
    zamestnanci.append(zamestnanec)


# Zkouska funkcnosti (opraveno L115 a L120)
# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
zamestnanec_2 = Zamestnanec('petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'
assert zamestnanec_2.ziskej_inicialy() == 'P.N.'

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno')  # Opraveno podle zadání
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.jmeno, str)  # Opraveno podle zadání
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
assert zoo.vaha_vsech_zvirat_v_zoo() == 150
assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12