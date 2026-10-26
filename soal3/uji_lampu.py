from lampu import Lampu

lp = Lampu("L1")
print("Awal:", lp.aktif, lp.kecerahan)
lp.nyalakan()
print("Setelah nyalakan:", lp.aktif, lp.kecerahan)
lp.atur(60)
print("Setelah atur(60):", lp.aktif, lp.kecerahan)
lp.atur(150)
print("Setelah atur(150):", lp.aktif, lp.kecerahan)
lp.atur(-5)
print("Setelah atur(-5):", lp.aktif, lp.kecerahan)
lp.matikan()
print("Setelah matikan:", lp.aktif, lp.kecerahan)