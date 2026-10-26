
class Perangkat:
    """Kelas dasar perangkat pengukuran."""
    def __init__(self, nama):
        self.nama = nama
        self.data = []

    def baca(self, nilai):
        self.data.append(nilai)

    def proses(self):
        raise NotImplementedError("Metode proses() harus diimplementasikan di subclass")


class SensorSuhu(Perangkat):
    """Sensor suhu: proses mengembalikan nilai tertinggi."""
    def proses(self):
        return max(self.data)


class SensorDebit(Perangkat):
    """Sensor debit: proses mengembalikan rata-rata."""
    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan

    def proses(self):
        return sum(self.data) / len(self.data)