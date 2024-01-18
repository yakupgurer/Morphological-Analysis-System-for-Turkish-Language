from flask import Flask, render_template, request
import re
#%run
#FiilEkAyrimi.ipynb
from FiilEkAyrimi import deger
from difflib import get_close_matches
import numpy as np
# %run Untitled1.ipynb
import random

app = Flask(__name__)

## global tanımlamalar (ekler)

ek_dosyalar = {
    "Opt": ["yalım", "yelim", "alım", "elim"],
    "Opt+A2sg": ["yasın", "yesin", "asın", "esin"],
    "Opt+A2pl": ["yasınız", "yesiniz", "asınız", "esiniz"],
    "Opt+A1sg": ["yayım", "yeyim", "ayım", "eyim"],
    ## noun suffixes
    "Pl": ["lar", "ler"],
    ## case suffixes
    "Dat": ["ya", "ye", "e", "a", "na", "ne"],
    "Loc": ["da", "de", "ta", "te", "nde", "nda"],
    "Abl": ["dan", "den", "tan", "ten", "ndan", "nden"],
    "Gen": ["nın", "nin", "nun", "nün", "ın", "in", "un", "ün", "yın", "yin", "yun", "yün", "ım", "im", "um", "üm",
            "m"],
    "Acc": ["yı", "yi", "yu", "yü", "ı", "i", "u", "ü", "nı", "ni", "nu", "nü"],
    "Inst": ["yla", "yle", "la", "le"],
    "P1sg": ["ım", "im", "um", "üm", "m", "yum"],
    "P2sg": ["ın", "in", "un", "ün", "n", "yun"],
    "P3sg": ["sı", "si", "su", "sü", "ı", "i", "u", "ü", "yu"],
    "P1pl": ["ımız", "imiz", "umuz", "ümüz", "mız", "miz", "muz", "müz", "yumuz"],
    "P2pl": ["ınız", "iniz", "unuz", "ünüz", "nız", "niz", "nuz", "nüz", "yunuz"],
    "P3pl": ["ı", "i", "u", "ü", "ları", "leri"],
    "Dim": ["cık", "cik", "cuk", "cük", "çık", "çik", "çuk", "çük", "cığ", "ciğ", "cuğ", "cüğ", "çığ", "çiğ", "çuğ",
            "çüğ"],
    "Dim2": ["cağız", "ceğiz"],
    "With": ["lı", "li", "lu", "lü"],
    "Without": ["sız", "siz", "suz", "süz"],
    "Since": ["dır", "dir", "dur", "dür", "tır", "tir", "tur", "tür"],
    "Related": ["sal", "sel"],
    "Ness": ["lık", "lik", "luk", "lük", "lığ", "liğ", "luğ", "lüğ"],
    "Acquire": ["lan", "len"],
    "Apply": ["la", "le"],
    "Resemb": ["ımsı", "imsi", "umsu", "ümsü", "msı", "msi", "msu", "msü"],
    "Rel": ["kı", "ki", "ku", "kü"],
    "By": ["ca", "ce"],
    "Cmp": ["ca", "ce"],
    "Agt": ["cı", "ci", "cu", "cü", "yıcı", "yici", "yucu", "yücü"],
    ## Adjective Suffixes
    "Become": ["laş", "leş"],
    "Ly": ["ca", "ce"],
    "Quite": ["ca", "ce"],
    ## number-person agreement suffixes
    "A1sg": ["yım", "yim", "yum", "yüm", "m", "ım", "im", "um", "üm"],
    "A2sg": ["sın", "sin", "sun", "sün", "n", "ın", "in", "un", "ün"],
    "A3sg": [""],
    "A1pl": ["yız", "yiz", "k", "yuz", "yüz", "ız", "iz", "uz", "üz"],
    "A2pl": ["sınız", "siniz", "sunuz", "sünüz", "nız", "niz", "nuz", "nüz", "ınız", "iniz", "unuz", "ünüz"],
    "A3pl": ["lar", "ler"],
    ### Numeral suffixes
    "Grouping": ["şar", "şer", "ız", "iz", "ar", "er"],
    "Ordinal": ["ıncı", "inci", "uncu", "üncü", "ncı", "nci", "ncu", "ncü"],
    "Division": ["da", "de", "ta", "te"],

    ### Derivational Suffixes

    "Trap_Eki": ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p",
                 "r", "s", "ş", "t", "u", "ü", "v", "y", "z"],

}


## global tanimlamalar sonu

def get_random_sentence(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file]
    return random.choice(sentences)


def find_longest_root(input_word, root_list):
    longest_root = ''
    for root in root_list:
        if input_word.startswith(root) and len(root) > len(longest_root):
            longest_root = root

    return longest_root


def correct_input(input_word, root_list, suffix_list):
    longest_root = find_longest_root(input_word, root_list)
    print(longest_root, "bu longest_root")
    geriyeKalanEk = input_word[len(longest_root):]
    print(geriyeKalanEk, "geriye kalan ek")

    if (geriyeKalanEk):
        suffix_correction = get_close_matches(geriyeKalanEk, suffix_list, n=1, cutoff=0.4)
        corrected_suffix = suffix_correction[0] if suffix_correction else geriyeKalanEk
        corrected_word = longest_root + corrected_suffix

    else:
        corrected_word = input_word

    return corrected_word


def sentence_splitter(text):
    sentence_endings = r"[.!?]"
    sentences = re.split(sentence_endings, text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences


def tokenizer(text):
    tokens = text.split()
    return tokens


def parcala_ve_kontrol_et(input_str):
    ozel_durumlar = {
        # "ımız": ["ım", "ız"],
        # "sinler":["s","i","n","ler"],
        # "leri":["ler","i"],
        # "sının":["sı","nın"],
        # "elim":["e","lim"],

    }

    sonuclar = []
    en_uzun_ekler = []

    while input_str:
        bulundu = False
        ozelBulundu = False
        en_uzun_ek = ""
        ek_adi_list = []

        # Özel durum kontrolü
        for ozel_ek, ayrilma_sekli in ozel_durumlar.items():
            if input_str.startswith(ozel_ek):
                for ayrilma in ayrilma_sekli:
                    for ad, ekler in ek_dosyalar.items():
                        if ayrilma in ekler and input_str.startswith(ayrilma):
                            en_uzun_ek = ayrilma
                            ek_adi = f"({ad})"
                            ozelBulundu = True
                            if ozelBulundu:
                                input_str = input_str[len(en_uzun_ek):].strip()
                                ek_adi_list.append(ek_adi)

        if not ozelBulundu:
            for ad, ekler in ek_dosyalar.items():
                for ek in ekler:
                    if input_str.startswith(ek) and len(ek) >= len(en_uzun_ek):
                        en_uzun_ek = ek
                        ek_adi = f"({ad})"
                        bulundu = True

            if bulundu:
                input_str = input_str[len(en_uzun_ek):].strip()
                for ad, ekler in ek_dosyalar.items():
                    if en_uzun_ek in ekler:
                        ek_adi_list.append(f"({ad})")
            else:
                ek_adi_list.append(f"({input_str})")

        if ek_adi_list:
            sonuclar.append((f"-{en_uzun_ek} ", ek_adi_list))
            en_uzun_ek = ""
            ek_adi_list = []

    print(sonuclar, "YKAUP BABA SONUCLAR")
    return sonuclar


def endswithKontrolu(input_str):
    ozel_durumlar = {
        # "ımız": ["ım", "ız"],
        # "sinler":["s","i","n","ler"],
        # "leri":["ler","i"],
        # "sının":["sı","nın"],
        # "elim":["e","lim"],

    }

    sonuclar = []
    en_uzun_ekler = []

    while input_str:
        bulundu = False
        ozelBulundu = False
        en_uzun_ek = ""
        ek_adi_list = []

        # Özel durum kontrolü
        for ozel_ek, ayrilma_sekli in ozel_durumlar.items():
            if input_str.startswith(ozel_ek):
                for ayrilma in ayrilma_sekli:
                    for ad, ekler in ek_dosyalar.items():
                        if ayrilma in ekler and input_str.startswith(ayrilma):
                            en_uzun_ek = ayrilma
                            ek_adi = f"({ad})"
                            ozelBulundu = True
                            if ozelBulundu:
                                input_str = input_str[len(en_uzun_ek):].strip()
                                ek_adi_list.append(ek_adi)

        if not ozelBulundu:
            for ad, ekler in ek_dosyalar.items():
                for ek in ekler:
                    if input_str.endswith(ek) and len(ek) >= len(en_uzun_ek):
                        en_uzun_ek = ek
                        ek_adi = f"({ad})"
                        bulundu = True

            if bulundu:
                input_str = input_str[:-len(en_uzun_ek)].strip()
                for ad, ekler in ek_dosyalar.items():
                    if en_uzun_ek in ekler:
                        ek_adi_list.append(f"({ad})")
            else:
                ek_adi_list.append(f"({input_str})")

        if ek_adi_list:
            sonuclar.insert(0, (f"-{en_uzun_ek} ", ek_adi_list))
            en_uzun_ek = ""
            ek_adi_list = []

    print(sonuclar, "PUKAY BABA SONUCLAR")
    return sonuclar


def find_and_process_suffixes_v2(base_word, dataset_path):
    def find_suffixes(word, suffixes):
        found_suffixes = [suffix for suffix in suffixes if word.endswith(suffix)]
        for x in found_suffixes:
            print(x, "yakup ek")
        return found_suffixes

    def process_dataset(base_word, suffixes):
        matches = []
        suffix_categories = []
        matches2 = []
        suffix_categories2 = []
        new_base_word = ""

        print(base_word, "process_dataya gelen base_word")
        print(suffixes, "bu da process_dataya gelen suffixes")
        with open(dataset_path, 'r', encoding='utf-8') as dataset_file:
            for line in dataset_file:
                parts = line.strip().split()

                if len(parts[0]):
                    current_word, word_type = parts[0], parts[1:]

                    if not suffixes:
                        if base_word == current_word:
                            matches.append(current_word)
                            suffix_categories.append(f"({word_type})")

                    for suffix in suffixes:

                        if base_word == current_word:

                            matches.append(current_word)
                            suffix_categories.append(f"({word_type})")
                            matches2.append(current_word)
                            suffix_categories2.append(f"({word_type})")

                            if any('CL_FIIL' in category for category in word_type):
                                return matches, ["CL_FIIL"], "", ""
                                print("eyw")
                            else:
                                sonuclar = parcala_ve_kontrol_et(suffix)
                                print(sonuclar, "bunlar da sonuclar")
                                sonuclar2 = endswithKontrolu(suffix)
                                print(sonuclar2, "SONUCLAR 2")
                                for ek, dosya_adi in sonuclar:
                                    matches.append(ek)
                                    suffix_categories.append(f"({dosya_adi})")
                                for ek, dosya_adi in sonuclar2:
                                    print("BURAYA GIRIYON MU PEKI")
                                    matches2.append(ek)
                                    suffix_categories2.append(f"({dosya_adi})")
                        else:
                            if base_word.endswith('b'):
                                new_base_word = base_word[:-1] + 'p'
                            elif base_word.endswith('c'):
                                new_base_word = base_word[:-1] + 'ç'
                            elif base_word.endswith('d'):
                                new_base_word = base_word[:-1] + 't'
                            elif base_word.endswith('ğ'):
                                new_base_word = base_word[:-1] + 'k'
                            if new_base_word == current_word:
                                matches.append(current_word)
                                suffix_categories.append(f"({word_type})")

                                sonuclar = parcala_ve_kontrol_et(suffix)
                                print(sonuclar, "bunlar da sonuclar")
                                sonuclar2 = endswithKontrolu(suffix)
                                print(sonuclar2, "SONUCLAR 2")
                                for ek, dosya_adi in sonuclar:
                                    matches.append(ek)
                                    suffix_categories.append(f"({dosya_adi})")
                                for ek, dosya_adi in sonuclar2:
                                    print("BURAYA GIRIYON MU PEKI")
                                    matches2.append(ek)
                                    suffix_categories2.append(f"({dosya_adi})")

        print(matches2, "RETURN ETMEDEN ONCEKI MATCHES2")
        return matches, suffix_categories, matches2, suffix_categories2

    ihtimalVarmi = False
    fiilDondu = False

    unlu_dusmesi = {
        "ağz": "ağız",
        "aln": "alın",
        "burn": "burun",
        "bağr": "bağır",
        "beyn": "beyin",
        "göğs": "göğüs",
        "karn": "karın",
        "omz": "omuz",
        "oğl": "oğul",
        "gönl": "gönül",
        "akl": "akıl",
        "fikr": "fikir",
        "cism": "cisim",
        "ayr": "ayır",
        "devr": "devir",
        "çevr": "çevir",
        "sıyr": "sıyır",
        "kıvr": "kıvır",
        "devr": "devir",
        "kayb": "kayıp",
        "haps": "hapis",
        "sabr": "sabır",
        "ufk": "ufuk",
        "benz": "beniz",
        "boyn": "boyun",
        "bağr": "bağır",
        "genz": "geniz",
        "gönl": "gönül",
        "oğl": "oğul",

    }

    with open('C:/endings.txt', 'r', encoding='utf-8') as endings_file:
        suffixes = [line.strip() for line in endings_file]

    eksizEslesme, suffix_categories, eksizEslesme2, suffix_categories2 = process_dataset(base_word, [])

    if any('CL_FIIL' in category for category in suffix_categories):
        # return 'Bu bir fiil oldugu icin burasi lokmandan gelecek'
        return deger(base_word)

    all_suffixes = find_suffixes(base_word, suffixes)

    if eksizEslesme:
        return ''.join(eksizEslesme), ''.join(suffix_categories)
    elif all_suffixes:
        result_suffixes = []

        for suffix in sorted(all_suffixes, key=len, reverse=True):
            print(suffix, "yakuk")
            remaining_word = base_word[:-len(suffix)]
            print(remaining_word, "bu da remaining word")
            if remaining_word.endswith(("iyor", "iyo", "üyor", "üyo")):
                if (not fiilDondu):
                    remaining_word = remaining_word.replace("iyor", "e").replace("iyo", "e").replace("üyor",
                                                                                                     "e").replace("üyo",
                                                                                                                  "e",
                                                                                                                  1)
                    print(remaining_word, "yeni remaining word bu")
            if remaining_word.endswith(("ıyor", "ıyo", "uyor", "uyo")):
                if (not fiilDondu):
                    remaining_word = remaining_word.replace("ıyor", "a").replace("ıyo", "a").replace("uyor",
                                                                                                     "a").replace("uyo",
                                                                                                                  "a",
                                                                                                                  1)
                    print(remaining_word, "yeni remaining word bu")

            if remaining_word in unlu_dusmesi:
                remaining_word = unlu_dusmesi[remaining_word]

            matches, suffix_categories, matches2, suffix_categories2 = process_dataset(remaining_word, [suffix])
            print(matches, "bu matches")
            print(suffix_categories, "bu sofik kategori")
            print(matches2, "BU MATCHES2")

            if matches:

                if any(any(keyword in category for keyword in ('CL_FIIL', 'Apply', 'Become')) for category in
                       suffix_categories):
                    # return 'Bu bir fiil oldugu icin burasi lokmandan gelecek'
                    if (ihtimalVarmi):
                        result_suffixes.extend('<br>')
                        result_suffixes.extend(f' <br> Eşleşen diğer bir seçenek: ')
                        result_suffixes.extend(deger(base_word))
                        result_suffixes.extend(' ')
                        tempBaseWord = base_word
                        fiilDondu = True
                        return ''.join(result_suffixes)

                    else:
                        ihtimalVarmi = True
                        print(deger(base_word), "SFAJGJSDAGJASDLGASDKGJKSDLJL")
                        result_suffixes.extend(deger(base_word))
                        result_suffixes.extend(' ')
                        result_suffixes.extend('<br>')
                        fiilDondu = True
                        return ''.join(result_suffixes)

                else:
                    if (ihtimalVarmi):
                        # if all("Trap_Eki" not in suffix_category for suffix_category in suffix_categories):
                        result_suffixes.extend('<br>')
                        result_suffixes.extend(f' <br> Eşleşen diğer bir seçenek: ')
                        result_suffixes.extend(matches)
                        result_suffixes.extend(suffix_categories)
                        result_suffixes.extend(' ')
                        if (matches != matches2 and suffix_categories != suffix_categories2):
                            result_suffixes.extend('<br>')
                            result_suffixes.extend('<br>')
                            result_suffixes.extend(matches2)
                            result_suffixes.extend(suffix_categories2)
                            result_suffixes.extend(' ')
                    else:
                        # if all("Trap_Eki" not in suffix_category for suffix_category in suffix_categories):
                        ihtimalVarmi = True
                        result_suffixes.extend(matches)
                        result_suffixes.extend(suffix_categories)
                        result_suffixes.extend(' ')
                        if (matches != matches2 and suffix_categories != suffix_categories2):
                            result_suffixes.extend('<br>')
                            result_suffixes.extend('<br>')
                            result_suffixes.extend(matches2)
                            result_suffixes.extend(suffix_categories2)
                            result_suffixes.extend(' ')


            else:
                # kontrolVar=deger(base_word)
                # if(kontrolVar):
                # result_suffixes.extend(deger(base_word))
                # else:
                # return f"{base_word} kelimesi için eşleşme bulunamadı."
                print("sebze")

        return ''.join(result_suffixes)


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    root_list_path = 'C:/dataset.txt'
    suffix_list_path = 'C:/endings.txt'
    with open(root_list_path, 'r', encoding='utf-8') as root_file:
        root_list = [line.strip().split()[0] for line in root_file]

    with open(suffix_list_path, 'r', encoding='utf-8') as suffix_file:
        suffix_list = [line.strip() for line in suffix_file]

    if request.method == "POST":
        if request.form.get("generate_random_sentence"):
            user_input = get_random_sentence('C:/turkceCumleler.txt')
        else:
            user_input = request.form.get("user_input", "")
    else:
        user_input = ""

    user_input = user_input.lower()
    user_input = user_input.replace("'", ' ').replace('"', '').replace(',', ' ').replace(';', ' ')
    normalizasyonAktif = request.form.get("normalizasyonAktif")

    sentences = sentence_splitter(user_input)

    for sentence in sentences:
        tokens = tokenizer(sentence)
        processed_tokens = []

        for token in tokens:
            if normalizasyonAktif == "True":
                corrected_word = correct_input(token, root_list, suffix_list)
                result = find_and_process_suffixes_v2(corrected_word, 'C:/dataset.txt')
                processed_tokens.append((corrected_word, result))
            elif normalizasyonAktif == "False":
                result = find_and_process_suffixes_v2(token, 'C:/dataset.txt')
                processed_tokens.append((token, result))

        results.append(processed_tokens)

    return render_template("index.html", results=results, user_input=user_input)


@app.route('/developers')
def developers():
    return render_template('developers.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)