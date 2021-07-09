import random

jmlvc = raw_input("Masukkan Jumlah Voucher .:")
giga = raw_input("Masukkan Jumlah GigaBytes Voucher .:")
giga1 = int(giga) * 10737418241824
com  = raw_input("Comment.:")

for i in range (0,int(jmlvc)):
    ab = (random.randint(10000000,99999999))
    print ("ip hotspot user add name=%s password=%s profile=default comment=%s limit-bytes-total=%s "%(ab,ab,com,str(giga1)))

