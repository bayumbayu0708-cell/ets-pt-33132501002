
import csv
from pathlib import Path


def baca_log(nama_file):
    """Membaca log_debit.csv dan memvalidasi setiap baris data.

    Aturan validasi:
      1. Jumlah kolom harus 2.
      2. Nilai debit harus berupa angka.
      3. Nilai debit harus 5 <= nilai <= 25 (inklusif).

    Input : nama_file (str) — path file CSV
    Output: (data_valid, data_ditolak)
            data_valid  : list of float
            data_ditolak: list of dict {baris, isi, alasan}
    """
    valid = []
    ditolak = []

    with open(nama_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for nomor, row in enumerate(reader, start=1):
            if nomor == 1:
                continue  # lewati header

            # Cek 1: jumlah kolom
            if len(row) != 2:
                ditolak.append({"baris": nomor, "isi": row,
                                "alasan": f"jumlah kolom {len(row)}, harus 2"})
                continue

            
            teks = row[1].strip().replace(",", ".")

           
            try:
                nilai = float(teks)
            except ValueError:
                ditolak.append({"baris": nomor, "isi": row,
                                "alasan": "nilai debit bukan angka"})
                continue

           
            if not (5 <= nilai <= 25):
                ditolak.append({"baris": nomor, "isi": row,
                                "alasan": f"nilai {nilai} di luar rentang 5-25"})
                continue

            valid.append(nilai)

    return valid, ditolak


if __name__ == "__main__":
    file_log = Path(__file__).with_name("log_debit.csv")
    valid, ditolak = baca_log(file_log)

    print("Jumlah data valid  :", len(valid))
    print("Jumlah data ditolak:", len(ditolak))
    print("\nAlasan penolakan:")
    for d in ditolak:
        print(f"  Baris {d['baris']}: {d['isi']} -> {d['alasan']}")

    rata = sum(valid) / len(valid)
    print(f"\nRata-rata data valid: {rata:.2f}")