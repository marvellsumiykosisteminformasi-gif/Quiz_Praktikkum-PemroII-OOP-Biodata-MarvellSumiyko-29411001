from peserta import Peserta

jumlah = int(input("Masukkan jumlah peserta: "))

for i in range(jumlah):
    print("\nData Peserta ke-", i + 1)

    peserta = Peserta.input_data()

    print("\n--- HASIL PENILAIAN ---")
    peserta.tampilkan_data()
    print("Nilai Akhir:", round(peserta.hitung_nilai_akhir(), 2))
    print("Grade:", peserta.hitung_grade())
    print("Status:", peserta.cek_kelulusan())