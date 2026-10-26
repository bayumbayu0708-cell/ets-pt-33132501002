def galat_absolut(hasil, acuan):
    """Selisih absolut hasil terhadap acuan."""
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    """Galat relatif dalam persen. ValueError bila acuan 0."""
    if acuan == 0:
        raise ValueError("Acuan tidak boleh nol")
    return abs(hasil - acuan) / abs(acuan) * 100


def status_kelulusan(galat_rel, toleransi=0.5):
    return "LULUS" if galat_rel <= toleransi else "TIDAK LULUS"


if __name__ == "__main__":
    hasil = 14.2
    acuan = 14.0
    galat_abs = galat_absolut(hasil, acuan)
    galat_rel = galat_relatif(hasil, acuan)

    print(f"Hasil pengukuran: {hasil}")
    print(f"Nilai acuan     : {acuan}")
    print(f"Galat absolut   : {galat_abs:.2f}")
    print(f"Galat relatif   : {galat_rel:.2f}%")
    print(f"Status          : {status_kelulusan(galat_rel)}")