from perangkat import SensorSuhu, SensorDebit

suhu = SensorSuhu("Suhu")
for v in [30.1, 30.6, 30.3]:
    suhu.baca(v)

debit = SensorDebit("Debit", "L/menit")
for v in [12.0, 15.0, 15.0]:
    debit.baca(v)

daftar = [suhu, debit]
for p in daftar:
    print(f"{p.nama} -> {p.proses()}")