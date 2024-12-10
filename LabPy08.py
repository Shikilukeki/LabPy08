class ProgramMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def hitung_nilai_akhir(self, nilai_tugas, nilai_uts, nilai_uas):
        return (0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)

    def tambah(self):
        while True:
            try:
                nama = input("Masukkan nama: ")
                nilai_tugas = float(input("Masukkan nilai tugas: "))
                nilai_uts = float(input("Masukkan nilai UTS: "))
                nilai_uas = float(input("Masukkan nilai UAS: "))

                nilai_akhir = self.hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
                self.data_mahasiswa[nama.lower()] = {
                    "nama": nama,
                    "nilai_tugas": nilai_tugas,
                    "nilai_uts": nilai_uts,
                    "nilai_uas": nilai_uas,
                    "nilai_akhir": nilai_akhir
                }
                print("Data berhasil ditambahkan.")
                break
            except ValueError:
                print("Input tidak valid. Silakan coba lagi.")

    def ubah(self, nama):
        nama_lower = nama.lower()
        if nama_lower in self.data_mahasiswa:
            while True:
                try:
                    nama_baru = input("Masukkan nama baru: ")
                    nilai_tugas = float(input("Masukkan nilai tugas baru: "))
                    nilai_uts = float(input("Masukkan nilai UTS baru: "))
                    nilai_uas = float(input("Masukkan nilai UAS baru: "))

                    nilai_akhir = self.hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
                    del self.data_mahasiswa[nama_lower]
                    self.data_mahasiswa[nama_baru.lower()] = {
                        "nama": nama_baru,
                        "nilai_tugas": nilai_tugas,
                        "nilai_uts": nilai_uts,
                        "nilai_uas": nilai_uas,
                        "nilai_akhir": nilai_akhir
                    }
                    print("Data berhasil diubah.")
                    return
                except ValueError:
                    print("Input tidak valid. Silakan coba lagi.")
        else:
            print("Data tidak ditemukan.")

    def hapus(self, nama):
        nama_lower = nama.lower()
        if nama_lower in self.data_mahasiswa:
            del self.data_mahasiswa[nama_lower]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    def tampilkan(self):
        print("\nDaftar Data Mahasiswa:")
        print("===================================================================")
        
        if self.data_mahasiswa:
            for i, mahasiswa in enumerate(self.data_mahasiswa.values(), start=1):
                print(f"{i}. Nama: {mahasiswa['nama']}")
                print(f"   Nilai Tugas: {mahasiswa['nilai_tugas']}")
                print(f"   Nilai UTS: {mahasiswa['nilai_uts']}")
                print(f"   Nilai UAS: {mahasiswa['nilai_uas']}")
                print(f"   Nilai Akhir: {mahasiswa['nilai_akhir']:.2f}")
                print("-------------------------------------------------------------------")
        else:
            print("Belum ada data mahasiswa.")
            print("===================================================================")

    def menu_utama(self):
        pilihan_menu = {
            '1': self.tambah,
            '2': self.ubah_data,
            '3': self.hapus_data,
            '4': self.tampilkan,
            '5': self.keluar
        }

        while True:
            print("\nProgram mendata mahasiswa")
            pilihan = input("[1] Tambah data\n[2] Ubah data\n[3] Hapus data\n[4] Lihat data\n[5] Keluar\nPilih menu: ")
            pilihan_menu.get(pilihan, self.invalid)()

    def ubah_data(self):
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        self.ubah(nama)

    def hapus_data(self):
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        self.hapus(nama)

    def keluar(self):
        print("Keluar dari program. Terima kasih!")
        exit()

    def invalid(self):
        print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    program = ProgramMahasiswa()
    program.menu_utama()
