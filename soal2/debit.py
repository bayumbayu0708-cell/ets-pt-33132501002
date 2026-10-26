
data_debit = [12.5, 14.0, 13.5, 15.0, 11.0]


def hitung_rata_rata(data):
    """Menghitung rata-rata dari list data debit.

    Input : data (list of float) — daftar pembacaan debit air
    Output: float — rata-rata seluruh elemen data
    """
    total = 0
    for i in range(len(data)):       
        total = total + data[i]
    return total / len(data)


def cari_terendah(data):
    """Mencari nilai terendah dari list data.

    Input : data (list of float)
    Output: float — nilai terkecil pada data
    """
    terendah = data[0]
    for nilai in data:
        if nilai < terendah:
            terendah = nilai
    return terendah


def cek_status(debit):                  
    """Mengecek status debit air (L/menit).

    Input : debit (float) — nilai debit air
    Output: str — "RENDAH", "NORMAL", atau "TINGGI"
    Batas kategori:
      - RENDAH : debit < 10
      - NORMAL : 10 <= debit <= 20
      - TINGGI : debit > 20
    """
    if debit < 10:
        return "RENDAH"
    elif debit <= 20:
        return "NORMAL"
    else:
        return "TINGGI"


if __name__ == "__main__":
    rata = hitung_rata_rata(data_debit)
    print("Rata-rata :", rata)
    print("Terendah  :", cari_terendah(data_debit))  
    print("Status    :", cek_status(rata))