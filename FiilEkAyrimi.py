import csv
import os


def bastan_en_uzun_kok(en_uzun_kok, ek_diziler):
    batan_en_uzun = {"ek": "", "dizi": ""}

    for dizi_turu, ek_dizi in ek_diziler.items():
        for ek in ek_dizi:
            if en_uzun_kok.startswith(ek):
                if len(ek) > len(batan_en_uzun["ek"]):
                    batan_en_uzun["ek"] = ek
                    batan_en_uzun["dizi"] = dizi_turu

    return batan_en_uzun


def ek(en_uzun_kok):
    OptA = ["alım", "elim"]
    A1sg = ["yım", "yim", "yum", "yüm", "m", "ım", "im", "um", "üm"]
    Become = ["laş", "leş"]
    A2sg = ["sın", "sin", "sun", "sün", "n", "ın", "in", "un", "ün"]  # Prog Prog2 Fut Evid
    A1pl = ["yız", "yiz", "k", "yuz", "yüz", "ız", "iz", "uz", "üz"]
    A2pl = ["sınız", "siniz", "sunuz", "sünüz", "ınız", "iniz", "unuz", "ünüz", "nız", "niz", "nuz", "nüz"]
    A3pl = ["lar", "ler"]
    Aor = ["r", "ar", "er", "ür", "ir", "ır", "ur"]
    Prog = ["iyor", "ıyor", "üyor", "uyor", "yor"]
    Prog2 = ["makta", "mekte"]
    Fut = ["acak", "ecek", "acağ", "eceğ", "yacak", "yecek", "yacağ", "yeceğ"]
    Past = ["tı", "dı", "ti", "di", "du", "tu", "tü", "dü"]
    Evid = ["mış", "miş", "muş", "müş"]
    Neg = ["ma", "me", "m", "mez", "maz"]
    Cond = ["se", "sa"]
    necess = ["malı", "meli"]
    Opt = ["a", "e", "ye", "ya"]
    Imp = ["sin", "sın", "sün", "sun", "in", "ın", "ün", "un", "yün", "yin", "yın", "yun", "iniz", "ınız", "ünüz",
           "unuz", "yünüz", "yiniz", "yınız", "yunuz"]
    PastCop = ["tı", "dı", "ti", "di", "du", "tu", "tü", "dü", "ytı", "ydı", "yti", "ydi", "ydu", "ytu", "ytü", "ydü"]
    EvidCop = ["mış", "miş", "muş", "müş", "ymış", "ymiş", "ymuş", "ymüş"]
    CondCop = ["ysa", "yse", "se", "sa"]
    While = ["ken", "yken"]
    Caus = ["t", "tır", "dır", "dir", "tir", "tür", "dür", "dur", "tur"]
    Cop = ["dır", "dir", "tır", "tir", "dür", "dur", "tür", "tur"]
    Pass = ["il", "ıl", "ül", "ul", "n", "in", "ın", "ün", "un", "nıl", "nil", "nül", "nul"]
    Recip = ["iş", "ış", "üş", "uş", "yüş", "yuş", "yiş", "yış", "ş"]
    Inf3 = ["iş", "ış", "üş", "uş", "yüş", "yuş", "yiş", "yış"]
    Reflex = ["n", "in", "ın", "ün", "un"]
    Abil = ["ebil", "abil", "yebil", "yabil"]
    NegAbil = ["eme", "ama", "yeme", "yama"]
    Cont = ["edur", "adur", "yedur", "yadur"]
    EverSince = ["egel", "agel", "yegel", "yagel"]
    Cont2 = ["egör", "agör", "yegör", "yagör"]
    Almost = ["eyaz", "ayaz", "yeyaz", "yayaz"]
    Hastily = ["uver", "üver", "iver", "ıver", "yuver", "yüver", "yiver", "yıver"]
    Stay = ["ekal", "akal", "yekal", "yakal"]
    Inf = ["mak", "mek"]
    Inf2 = ["ma", "me"]
    FutPart = ["acak", "ecek", "acağ", "eceğ", "yacak", "yecek", "yacağ", "yeceğ"]
    EvidPart = ["miş", "muş", "müş", "mış"]
    PastPart = ["tığ", "dığ", "tiğ", "diğ", "duğ", "tuğ", "tüğ", "düğ"]
    PresPart = ["an", "en", "yan", "yen"]
    AorPart = ["r", "ar", "er", "ür", "ir", "ır", "ur"]
    AfterDoing = ["ip", "ıp", "up", "üp", "yip", "yıp", "yup", "yüp"]
    Agt = ["ucu", "ici", "ıcı", "ücü", "yucu", "yici", "yıcı", "yücü"]
    FeelLike = ["esi", "ası", "yesi", "yası"]
    WorthyOfDoing = ["esi", "ası", "yesi", "yası"]
    SinceDoing = ["eli", "alı", "yeli", "yalı"]
    AsLongAs = ["dikçe", "dıkça", "tikçe", "tıkça", "dükçe", "tükçe", "dukça", "tukça"]
    When = ["ınca", "ince", "yınca", "yince", "unca", "yunca", "yünce", "ünce"]
    ByDoing = ["arak", "erek", "yarak", "yerek"]
    WithoutDoing = ["madan", "meden"]
    WithoutDoing2 = ["maksızın", "meksizin"]
    RatherThanInsteadOfDoing = ["maktansa", "mektense"]
    UnableToDo = ["yemeden", "yamadan", "emeden", "amadan"]
    ActOf = ["maca", "mece"]
    NotState = ["mazlık", "mazlığ", "mezlik", "mezliğ"]
    Aslf = ["casına", "çasına", "cesine", "çesine"]
    Adamantly = ["esiye", "asıya", "yesiye", "yasıya"]
    Cop = ["dir", "tir", "dır", "tır", "dur", "tur", "dür", "tür"]

    ek_diziler = {
        "NotState": NotState,
        "Opt + A1pl": OptA,
        "Caus": Caus,
        "Cop": Cop,
        "Imp": Imp,
        "A1sg": A1sg,
        "A2sg": A2sg,
        "A1pl": A1pl,
        "A2pl": A2pl,
        "A3pl": A3pl,
        "Stay": Stay,
        "Hastily": Hastily,
        "Almost": Almost,
        "Cont2": Cont2,
        "EverSince": EverSince,
        "Cont": Cont,
        "NegAbil": NegAbil,
        "Abil": Abil,
        "Reflex": Reflex,
        "z": Recip,
        "Pass": Pass,
        "Cop": Cop,
        "While": While,
        "Evid": Evid,
        "Past": Past,
        "Cond": Cond,
        "CondCop": CondCop,
        "EvidCop": EvidCop,
        "PastCop": PastCop,
        "Opt": Opt,
        "necess": necess,
        "Neg": Neg,
        "Fut": Fut,
        "Prog2": Prog2,
        "Prog": Prog,
        "Aor": Aor,
        "UnableToDo": UnableToDo,
        "RatherThanInsteadOfDoing": RatherThanInsteadOfDoing,
        "WithoutDoing2": WithoutDoing2,
        "WithoutDoing": WithoutDoing,
        "ByDoing": ByDoing,
        "When": When,
        "AsLongAs": AsLongAs,
        "SinceDoing": SinceDoing,
        "x": WorthyOfDoing,
        "x": FeelLike,
        "Agt": Agt,
        "AfterDoing": AfterDoing,
        "AorPart": AorPart,
        "PresPart": PresPart,
        "PastPart": PastPart,
        "EvidPart": EvidPart,
        "FutPart": FutPart,
        "z": Inf3,
        "Inf2": Inf2,
        "Inf": Inf,
        "ActOf": ActOf,
        "Aslf": Aslf,
        "Adamantly": Adamantly,
        "Become": Become

    }

    eklerr = ""
    ek_turu = ""

    while en_uzun_kok:
        bastan_en_uzun = bastan_en_uzun_kok(en_uzun_kok, ek_diziler)

        if bastan_en_uzun["ek"]:
            eklerr += "+" + bastan_en_uzun["ek"]
            ek_turu += "+" + bastan_en_uzun["dizi"]

            en_uzun_kok = en_uzun_kok[len(bastan_en_uzun["ek"]):]
        else:

            en_uzun_kok = en_uzun_kok[1:]

    eklerr = eklerr[1:]
    ek_turu = ek_turu[1:]

    if (eklerr[0] == 't') and eklerr[2] in ['r', 'ğ', 'k']:
        ek_turu = ek_turu.replace("Past", "Caus")
        eklerr = eklerr.replace("tı+", "t+")

    if "Fut" in ek_turu:

        if "Past" in ek_turu:

            ek_turu = ek_turu.replace("Past", "PastCop")


        elif "Evid" in ek_turu:
            ek_turu = ek_turu.replace("Evid", "EvidCop")

        elif "Cond" in ek_turu:
            ek_turu = ek_turu.replace("Cond", "CondCop")

    if ek_turu.find("Pass") != -1 and ek_turu.find("x") != -1 and ek_turu.find("Pass") < ek_turu.find("x"):
        ek_turu = ek_turu.replace("x", "WorthyOfDoing")
    else:

        ek_turu = ek_turu.replace("x", "FeelLike")

    if "z" in ek_turu and any(element in ek_turu for element in ["Aor", "Prog", "Fut", "Past", "Evid", "Imp"]):
        ek_turu = ek_turu.replace("z", "Recip")
    else:

        ek_turu = ek_turu.replace("z", "Inf3")

    if "Imp" in ek_turu and (any(element in ek_turu for element in ["Aor", "Prog", "Fut", "Past", "Evid"])):
        ek_turu = ek_turu.replace("Imp", "A2sg")

    if not any(element in ek_turu for element in ["A1sg", "A2sg", "A1pl", "A2pl", "A3pl"]):
        ek_turu += "+A3sg"
    if ek_turu.startswith("A1sg") and ek_turu[4] == '+':
        ek_turu = ek_turu.replace("A1sg", "Neg", 1)

    for i in ["mez", "maz", "mezler", "mazlar"]:
        if eklerr.find(i) != -1:
            ek_turu = ek_turu.replace("Neg", "Neg+Aor")
            break
    v = "Verb+"
    ek_turu = v + ek_turu
    return eklerr, ek_turu


def load_database():
    data = []
    with open('Ekler.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                data.append(row[0].lower())
    return data


def kelime_norm(word, database):
    kelime = []
    en_uzun_kok = ""
    for i in database:
        if i in word:
            kelime.append(i)
            if len(i) > len(en_uzun_kok):
                en_uzun_kok = i

    kelime = [x for x in kelime if x.endswith(word[-1:])]

    en_uzun_kok = max(kelime, key=len)

    if len(word[:-len(en_uzun_kok)]) in [0, 1] and word[:-len(en_uzun_kok)] != "y" and word[:-len(en_uzun_kok)] != "d":
        kelime.remove(en_uzun_kok)
        en_uzun_kok = max(kelime, key=len)

    return kelime, en_uzun_kok


datasett = 'FiilSozluk.txt'
with open(datasett, 'r', encoding='utf-8') as file:
    fiil_listesi = [line.strip() for line in file.readlines()]


def check2(kelime, en_uzun_kok):
    x = kelime[-1]

    if x in ['c', 'd', 'ğ', 'b'] and en_uzun_kok[0] in ['i', 'a', 'ı', 'e', 'u', 'ü', 'o', 'ö']:
        if x == 'd':
            kelime = kelime[:-1] + 't'

        if x == 'c':
            kelime = kelime[:-1] + 'ç'

        if x == 'ğ':
            kelime = kelime[:-1] + 'k'

        if x == 'b':
            kelime = kelime[:-1] + 'p'

    return kelime


def ilkKontrol(girdi, fiiller):
    for i in fiiller:
        if i[:-3] == girdi:
            return True

    return False


def en_kisa_kelimeyi_bul(girdi, kelimeler):
    filtrelenmis_kelimeler = [kelime for kelime in kelimeler if girdi in kelime]

    if not filtrelenmis_kelimeler:
        return girdi

    filtrelenmis_kelimeler = [kelime for kelime in filtrelenmis_kelimeler if kelime.startswith(girdi)]
    en_kisa_kelime = min(filtrelenmis_kelimeler, key=len)

    return en_kisa_kelime


def check(en_kisa_kelime, kelime, kokler, en_uzun_kok, database):
    f = ""
    kontrol = False

    if len(kelime) > 1:
        uzunluk = len(kelime)
        i = 0

        try:
            if en_kisa_kelime[uzunluk] in ['u', 'a', 'e', 'i', 'ü']:
                return f + en_uzun_kok, kontrol
        except IndexError:
            kokler, f = kelime_norm(en_kisa_kelime, database)
            kontrol = True

            uzunluk -= 1

        x = en_uzun_kok

        while en_kisa_kelime[uzunluk] == x[i]:
            if en_kisa_kelime[uzunluk] == 'm':
                return f + en_uzun_kok, kontrol

            temp = en_uzun_kok
            kokler.remove(en_uzun_kok)
            try:
                en_uzun_kok = max(kokler, key=len)
                uzunluk += 1
                i += 1
            except IndexError:
                return f + temp, kontrol

    return f + en_uzun_kok, kontrol


def fiil_kok(giris):
    database = load_database()

    if (ilkKontrol(giris, fiil_listesi)):
        return (f'{giris}+ (Verb+Imp+A1sg)')

    kokler, en_uzun_kok = kelime_norm(giris, database)

    kelime = giris[:-len(en_uzun_kok)]

    if len(kelime) > 1:
        kelime = check2(kelime, en_uzun_kok)

    en_kisa_kelime = en_kisa_kelimeyi_bul(kelime, fiil_listesi)

    if "leş" in giris or "laş" in giris:
        index = giris.find("laş")
        if index == -1:
            index = giris.find("leş")

        en_kisa_kelime = giris[:index]

        sonuc = giris[index:]

        return (f'{en_kisa_kelime}+{ek(sonuc)}')


    else:
        en_uzun_kok, kontrol = check(en_kisa_kelime, kelime, kokler, en_uzun_kok, database)
        kelime = giris[:-len(en_uzun_kok)]

        if kontrol == True:
            en_kisa_kelime = en_kisa_kelimeyi_bul(kelime, fiil_listesi)

        return (f'{en_kisa_kelime[:-3]}+ {ek(en_uzun_kok)}')


def deger(girdi):
    araba = fiil_kok(girdi)
    return araba


