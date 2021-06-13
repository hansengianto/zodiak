from bs4 import BeautifulSoup
import requests
from os import system

cls = lambda: system('cls')

def zodiakfimela(zodiak, harimingguan):
    if harimingguan == "mingguan":
        page = requests.get('https://fimela.com/zodiak/{}/minggu-ini'.format(zodiak))
        final = "Ramalan Zodiak {} Mingguan\n\n".format(zodiak)
    if harimingguan == "harian":
        page = requests.get('https://fimela.com/zodiak/{}/harian'.format(zodiak))
        final = "Ramalan Zodiak {} Harian\n\n".format(zodiak)

    soup = BeautifulSoup(page.text, 'html.parser')
    if page.status_code==200:
        div = soup.find(class_="zodiak--content__readpage--left")


    articles = div.find_all('div', class_="zodiak--content__content")

    num = 1

    for a in articles:
        single = a.find('p')
        final_result = single.text

        output_zodiak = final_result.replace("Couple:", "\n\n  Couple:")
        if num == 1:
            sem1 = "• Umum\n"
            sem1 += "  "+output_zodiak+"\n\n"
        if num == 2:
            sem2 = "• Love\n"
            sem2 += "  "+output_zodiak+"\n\n"
        if num == 3:
            sem3 = "• Keuangan\n"
            sem3 += "  "+output_zodiak

        num += 1
    nomor_keberuntungan = soup.find(class_="zodiak--content__numbers").text
    tanggal_zodiak = soup.find(class_="zodiak--content-header__date").text

    final += sem1+sem2+sem3
    final += "\n\n• Nomor Keberuntungan : "+nomor_keberuntungan

    return(final)

cls()
input_zodiak = str(input("Silahkan Isi Zodiak Kamu : "))
harian_mingguan = str(input("Silahkan Isi Harian Atau Mingguan :"))
zodiakk = ("aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagitarius", "capricorn", "aquarius", "pisces")
if input_zodiak.lower() in zodiakk:
    cls()
    print(zodiakfimela(input_zodiak.lower(), harian_mingguan.lower()))
else:
    cls()
    print("Sepertinya Kamu Salah Dalam Pengetikan, Silahkan Cek Juga Spasi Penulisan\n\n[Zodiak List]\n-Aries\n-Taurus\n-Gemini\n-Cancer\n-Leo\n-Virgo\n-Libra\n-Scorpio\n-Sagitarius\n-Capricorn\n-Aquarius\n-Pisces")
