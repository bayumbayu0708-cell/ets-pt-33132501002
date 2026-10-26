class Lampu:
    """Kelas lampu indikator panel otomasi."""
    jumlah_lampu = 0   # untuk butir b

    def __init__(self, nama):
        self.nama = nama
        self.aktif = False
        self.kecerahan = 0
        Lampu.jumlah_lampu += 1   # untuk butir b

    def nyalakan(self):
        self.aktif = True
        self.kecerahan = 100

    def matikan(self):
        self.aktif = False
        self.kecerahan = 0

    def atur(self, nilai):
        """Mengubah kecerahan hanya bila lampu aktif dan 0<=nilai<=100."""
        if self.aktif and 0 <= nilai <= 100:
            self.kecerahan = nilai

    def __str__(self):   # untuk butir b
        return f"Lampu {self.nama}: aktif = {self.aktif}, kecerahan = {self.kecerahan}"