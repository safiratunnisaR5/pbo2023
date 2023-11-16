import math

def hitung_luas_persegiPanjang(pj, lb):
    L = pj * lb 
    return L

def hitung_keliling_persegiPanjang(pj, lb):
        K = 2 * (pj + lb)
        return K


def hitung_luas_kerucut(jari_jari, tinggi) :
    L = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari * 2 + tinggi * 2))
    return L
                               

def volume_kerucut(jari_jari, tinggi):
   volume_kerucut  = (1/3) * math.pi * jari_jari * tinggi * 2
   return volume_kerucut



def hitung_luas_bola(jari_jari):
    L = 4 * math.pi * jari_jari
    return L
    
def volume_bola(jari_jari):
    V= (4/3) * math.pi * jari_jari
    return V

def hitung_luas_limas_segi_empat(jari_jari, tinggi):
 L = (2 * math.pi * jari_jari) * jari_jari + tinggi
 return L

def hitung_volume_limas_segi_empat(jari_jari, Tinggi):
    hitung_volume_limas_segi_empat = math.pi * jari_jari * 2 * Tinggi
    return hitung_volume_limas_segi_empat

def hitung_luas_alas_segitiga(sisi1, sisi2, sisi3, tinggiprisma):
    luasalas = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma
    return luasalas

def hitung_luas_sisi_segitiga(sisi1, sisi2, sisi3, tinggiprisma, alas, tinggi):
    luassisi = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma + alas * tinggi
    return luassisi

def hitung_luas_limas_segitiga(alassegitiga, tinggisegitiga, tinggilimas):
    luas = 4*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return luas

def hitung_volume_limas_segitiga(alassegitiga, tinggisegitiga, tinggilimas):
    Volume_limas_segitiga =  1/3*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return Volume_limas_segitiga


def hitung_luas_kubus(rusuk):
    L  = 6 * rusuk ** 2
    return L

def hitung_volume_kubus(rusuk):
    Volume_kubus = rusuk ** 3
    return Volume_kubus

def hitung_luas_balok(panjang, lebar):
    luas_balok = panjang * lebar
    return luas_balok

def hitung_volume_balok(panjang, lebar, tinggi) :
    volume_balok = panjang * lebar * tinggi 
    return volume_balok

def hitung_luas_tabung(jari_jari, tinggi):
    luas_tabung = (2 * math.pi * jari_jari) * jari_jari + tinggi
    return luas_tabung

def hitung_volume_tabung(jari_jari, Tinggi):
    Volume_tabung = math.pi * jari_jari * 2 * Tinggi
    return Volume_tabung

def hitung_luas_prisma_segitiga(sisi1,sisi2,sisi3,tinggiprisma):
    hitung_luas_prisma_segitiga = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma
    return hitung_luas_prisma_segitiga

def hitung_luassisi_prisma_segitiga(sisi1,sisi2,sisi3,tinggiprisma,alas,tinggi):
    hitung_luassisi_prisma_segitiga = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma + alas * tinggi
    return hitung_luassisi_prisma_segitiga

def hitung_volume_prisma_segitiga(alas,tinggi,luas,tinggiprisma,sisi1,sisi2,sisi3):
    hitung_volume_prisma_segitiga = ( alas * tinggi ) / 2 * tinggiprisma
    return hitung_volume_prisma_segitiga

    

