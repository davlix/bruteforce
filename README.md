# Brute Force Login Script

Skrip ini adalah sebuah program sederhana yang digunakan untuk melakukan serangan brute force pada halaman login. Skrip ini ditulis dalam bahasa Python dan menggunakan library `requests` dan `termcolor`.

## Instalasi

1. Pastikan Anda memiliki Python 3.x terinstal di komputer Anda.

2. Unduh atau salin kode `brute_force_login.py` ke dalam direktori kerja Anda.

3. Instal library `requests` dan `termcolor` dengan menggunakan perintah berikut melalui terminal:

   ```shell
   pip install requests termcolor
   ```

## Penggunaan

1. Jalankan skrip `brute_force_login.py` melalui terminal.

2. Program akan meminta beberapa input dari pengguna:

   - URL: Masukkan URL halaman login yang ingin Anda serang.

   - Username: Masukkan username yang akan digunakan untuk melakukan serangan brute force.

   - File Kata Sandi: Masukkan path file yang berisi daftar kata sandi yang akan dicoba.

   - String Gagal: Masukkan string yang muncul pada halaman jika login gagal.

   - Nilai Cookie (opsional): Masukkan nilai cookie jika halaman login menggunakan mekanisme autentikasi cookie.

3. Setelah semua input dimasukkan, program akan memulai serangan brute force dengan mencoba setiap kata sandi dalam daftar.

4. Jika username dan kata sandi yang tepat ditemukan, program akan menampilkan pesan berhasil dan berhenti.

5. Jika tidak ada kata sandi yang cocok ditemukan, program akan menampilkan pesan bahwa kata sandi tidak ditemukan dalam daftar.

## Perhatian

Penting untuk diingat bahwa melakukan serangan brute force pada halaman login tanpa izin yang sah atau legal adalah ilegal dan melanggar etika. Pastikan Anda memiliki izin dan hak yang sesuai sebelum menggunakan skrip ini untuk tujuan apa pun.

**Penulis tidak bertanggung jawab atas penggunaan yang salah atau ilegal dari skrip ini. Gunakan dengan risiko Anda sendiri.**

## Kontribusi

Kontribusi terbuka dan saran perbaikan selalu diterima. Jika Anda ingin memberikan perbaikan atau peningkatan pada skrip ini, silakan buat _pull request_ atau sampaikan melalui _issue_.

## Lisensi

Skrip ini dilisensikan di bawah [MIT License](LICENSE). Silakan merujuk ke file Lisensi untuk informasi lebih lanjut.

---
