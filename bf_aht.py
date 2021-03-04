#-*- coding:cp1254 -*-
import locale
import random
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")
sayac=0
sayac2=0
yenistr=""
print"""

\AnadoluHackTeam Brute Forcer version 3.5/
Tools Judas tarafından yazılmıştır.
IYI SALDIRILAR"""

while True:
    harf=raw_input("Brute Force için kullanılacak karakter setini belirleyin.//Aynı harfleri girmemeye özen gösterin:")
    liste=[]
    for i in harf:
        liste.append(i)
    tkr=raw_input("Ne kadar parola istersiniz(tam sayı giriniz):")
    while sayac2<int(tkr):
        while sayac<len(liste):
            a=random.choice(liste)
            yenistr=yenistr+a
            sayac=sayac+1
        sayac=0
        print yenistr
        yenistr=""
        sayac2=sayac2+1
    sayac2=0
    raw_input("")

