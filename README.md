# Software-Auto-Login-JAKWIFI

<details>
<summary>Pendahuluan</summary>
<p>

JakWIFI merupakan Program Internet untuk Semua yang diluncurkan oleh Pemerintah Provinsi DKI Jakarta pada 28 Agustus 2020 secara virtual. Dengan menjunjung tinggi semangat kolaborasi, Pemprov DKI Jakarta bersama Asosiasi Penyelenggara Jaringan Telekomunikasi (Apjatel) dan PT Bali Towerindo Sentra (Molecool) berhasil meluncurkan program JakWIFI ini.
        
</p>
<p>
Pada awalnya, program JakWIFI dibuat untuk membantu para peserta didik dalam Pembelajaran Jarak Jauh (PJJ) yang dilakukan secara daring. Salah satu tujuan utama program ini adalah memudahkan para peserta didik yang tidak memiliki atau kesulitan mendapatkan akses internet, agar dapat melakukan PJJ dengan mudah. 
</p>
<p>
Namun, seiring perjalanan waktu, Program JakWIFI juga bertujuan membantu segala aktivitas secara daring yang dilakukan para pekerja dan pelaku UMKM di DKI Jakarta. Secara garis besar, Program JakWIFI hadir untuk mendukung konektivitas dan produktivitas masyarakat pada masa pandemi Covid-19, dengan menyediakan akses internet gratis di ribuan titik seluruh penjuru Ibu Kota.
</p>
</details>

---

<details>
<summary>Permasalahan dan Solusinya</summary>
<p>
        JaKWIFI mengharuskan calon pengguna untuk registrasi diri terlebih dahulu sebelum dapat menggunakan layanan internet gratis. Setelah registrasi selesai, pengguna dapat langsung login dengan mengisikan nomor hp dan password yang telah didaftarkan sebelumnya pada kolom yang ada. Setiap perangkat router/access point JakWIFI diprogram untuk melakukan restart perangkat setiap satu(1) jam sekali. Hal ini menyebabkan pengguna harus menginput kembali username dan password untuk mendapatkan akses internet gratis.
</p>
<p>
        Solusi dari permasalahan tersebut adalah dengan melakukan otomatisasi untuk login. Dengan otomatisasi, pengguna hanya perlu menjalankan aplikasi ketika ingin login dan aplikasi akan secara otomatis melakukan hal-hal berikut (pada langkah tertentu, pengguna diharuskan untuk terhubung ke internet terlebih dahulu):
</p>

1. Cek chrome driver apakah sudah menggunakan versi terbaru?
   - Jika belum, maka aplikasi akan force close
   - User diharuskan terhubung ke internet terlebih dahulu
   - Kemudian user diharuskan untuk membuka aplikasi Auto_Login_JAKWIFI.py sekali lagi.
   - Aplikasi akan secara otomatis mendownload chrome driver versi terbaru.
2. Membuka browser dan login page.
3. Mengecek apakah URL yang dituju dapat dibuka atau tidak, jika tidak webpage akan terus menerus direfresh dengan interval waktu 5 detik, sampai URL yang dituju dapat dibuka/ditampilkan.
4. Mengisi kolom No. HP, password. 
5. Menekan tombol submit.
6. Menutup web browser.
7. Menutup aplikasi.

        


</details>

---

        Aplikasi ini  dibuat menggunakan bahasa pemrograman Python dan Framework Selenium untuk web browser Google Chrome

## Halaman Login JakWifi
![This is an image](https://github.com/tyannk/Software-Auto-Login-JAKWIFI/blob/master/Foto/Halaman%20Login.PNG)
 
