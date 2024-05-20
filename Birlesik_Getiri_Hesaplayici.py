from datetime import datetime

maas = int(input("Maaşınızı giriniz: "))
toplam_birikim = int(input("Toplam birikiminizi giriniz: "))
maas_yuzde = int(input("Paranızın yüzde kaçıyla yatırım yaparsınız: %"))
aylik_yatirim = maas * maas_yuzde / 100
senelik_zam = int(input("Her sene maaşınıza yüzde kaç zam yapılır: %"))
aylik_kazanc = int(input("Aylık ortalama yüzde kaç kazanıyorsunuz: %"))

current_date = datetime.today()
month = current_date.month
year = current_date.year

count = 0

print('\n')

while year - current_date.year < 20:

    count += 1

    print(f"Ay: {count} - Tarih: {month}/{year}")
    toplam_birikim = toplam_birikim * (1 + aylik_kazanc / 100) + aylik_yatirim

    print('Maaş:', "{:,.2f} TL".format(maas))
    print('Toplam birikim:', "{:,.2f} TL".format(toplam_birikim))
    print('\n')

    if toplam_birikim >= 1000000:
        break

    month += 1

    if month > 12:
        month = 1
        year += 1

    if count % 12 == 0:
        maas = maas + (maas * senelik_zam / 100)

son_tarih = f"{month}/{year}"

print(f'\nYaklaşık, {count} ayda yani {son_tarih} tarihinde 1 milyon TL\'ye ulaşabilirsiniz!')
print("\n")
print("Programdan çıkış yapmak isteseniz enter tuşuna basabilirsiniz.")
input()
print("Programdan çıkış yapıldı...")