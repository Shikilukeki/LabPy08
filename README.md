# LabPy08

Nama         : Rifqi Maulana

Kelas        : TI.24.A.5

Mata Kuliah  : Bahasa Pemograman

## Diagram Class

![Image](https://github.com/Shikilukeki/Foto/blob/main/Diagram%20class%20LabPy08.png?raw=true)

## Flowchart program

![Image](https://github.com/Shikilukeki/Foto/blob/main/LabPy08.png?raw=true)

## Penjelasan Program

Berikut penjelasan per fungsi dari kode dalam class ProgramMahasiswa:

```init(self):```

Fungsi ini adalah konstruktor yang digunakan untuk menginisialisasi objek dari kelas ProgramMahasiswa. Di sini, self.data_mahasiswa adalah sebuah dictionary yang akan menyimpan data mahasiswa.

```hitung_nilai_akhir(self, nilai_tugas, nilai_uts, nilai_uas):```

Fungsi ini menghitung nilai akhir mahasiswa berdasarkan bobot nilai tugas, UTS, dan UAS. Nilai akhir dihitung dengan rumus:

```python
(0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)
```
```tambah(self):```

Fungsi ini menambahkan data mahasiswa baru ke dalam data_mahasiswa. Pengguna akan diminta untuk memasukkan nama, nilai tugas, nilai UTS, dan nilai UAS. Nilai akhir dihitung menggunakan fungsi hitung_nilai_akhir dan data disimpan dalam dictionary data_mahasiswa.

```ubah(self, nama):```

Fungsi ini mengubah data mahasiswa yang sudah ada. Pengguna diminta untuk memasukkan nama mahasiswa yang datanya ingin diubah. Jika nama ditemukan, pengguna akan diminta untuk memasukkan data baru. Data lama dihapus dan diganti dengan data baru.

```hapus(self, nama):```

Fungsi ini menghapus data mahasiswa berdasarkan nama yang diberikan. Nama dicari dalam dictionary data_mahasiswa, dan jika ditemukan, data tersebut akan dihapus.

```tampilkan(self):```

Fungsi ini menampilkan semua data mahasiswa yang tersimpan dalam dictionary data_mahasiswa. Jika tidak ada data, akan ditampilkan pesan bahwa belum ada data mahasiswa.

```menu_utama(self):```

Fungsi ini menampilkan menu utama dan meminta pengguna untuk memilih opsi. Opsi yang tersedia adalah menambah data, mengubah data, menghapus data, melihat data, dan keluar dari program. Pilihan yang dimasukkan pengguna akan diarahkan ke fungsi yang sesuai.

```ubah_data(self):```

Fungsi pembantu ini meminta pengguna untuk memasukkan nama mahasiswa yang datanya akan diubah, dan kemudian memanggil fungsi ubah.

```hapus_data(self):```

Fungsi pembantu ini meminta pengguna untuk memasukkan nama mahasiswa yang datanya akan dihapus, dan kemudian memanggil fungsi hapus.

```keluar(self):```

Fungsi ini menampilkan pesan keluar dan mengakhiri program.

```invalid(self):```

Fungsi ini menangani pilihan menu yang tidak valid. Jika pengguna memasukkan pilihan yang tidak ada dalam menu, akan ditampilkan pesan kesalahan.

## Hasil eksekusi program

### Tambah data

![Image](https://github.com/Shikilukeki/Foto/blob/main/Tambah%20data%20Mahasiswa.png?raw=true)

### Ubah data
![Image](https://github.com/Shikilukeki/Foto/blob/main/Ubah%20data%20Mahasiswa.png?raw=true)

### Hapus data
![Image](https://github.com/Shikilukeki/Foto/blob/main/Hapus%20data%20Mahasiswa.png?raw=true)
