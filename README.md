# Tugas 2 PBP

## Heroku Link


[Click Here](https://katalog-app-pbp.herokuapp.com/katalog/)
<br><br>

## Questions
---

### **1. Bagan kaitan antara urls.py, views.py, models.py, dan HTML**<br><br>

![Bagan MTV Django](./assets/MTV%20Django%20(1).jpg)
<br>
Ketika pengguna mengirimkan _request_ untuk mengakses aplikasi, _request_ tersebut pertama-tama diterima oleh urls.py. Berkas urls.py akan melakukan _routing_ atau pemetaan _request_ ke suatu fungsi di views.py yang sesuai sebagai _handler_. Fungsi tersebut dapat melakukan modifikasi data pada models.py, seperti menambah, mengupdate, mengambil, dan menghapus data, tergantung _request_ yang didapatkan. Models.py sendiri berisi class Python yang diibaratkan sebuah tabel dan mendefinisikan atribut yang dimiliki setiap _entry_ data.

Data yang telah diolah di views.py kemudian ingin ditampilkan kepada pengguna. Hal ini dapat dilakukan dengan me-_render_ atau memasukkan data ke dalam berkas HTML, yang fungsinya seperti template. Di dalamnya terdapat bagian-bagian _syntax_ yang akan diganti sesuai parameter yang diberikan dari views.py. Setelah proses _render_ berhasil, halaman HTML akan ditampilkan kepada pengguna sebagai respons akhir dari _request_.
<br>

### **2. _Virtual Environment_**

_Virtual environment_ digunakan untuk mengeksekusi suatu aplikasi web Django secara terisolasi dari aplikasi lainnya. _Virtual environment_ bertujuan agar workspace antar-aplikasi tidak tercampur sehingga memudahkan pembuatan dan pengorganisasian aplikasi. Ibaratnya, _virtual environment_ memberikan sekat antar aplikasi yang ada, termasuk versi Python dan library apa saja yang diinstall pada aplikasi tertentu, tanpa khawatir akan timbulnya error atau adanya berkas yang tercampur.

Sebagai contoh, aplikasi A ingin dijalankan pada python 2.7, sedangkan aplikasi B ingin dijalankan di python 3.5. Hal tersebut dimungkinkan apabila kita menggunakan _virtual environment_. Namun demikian, aplikasi web berbasis Django dapat tetap dijalankan meskipun tanpa _virtual environment_.

### **3. Proses Pengerjaan**

**Poin 1**: Fungsi yang saya buat pada berkas views.py adalah show_katalog. Fungsi show_katalog akan mengurusi _request_ yang diberikan pengguna ketika mengakses url tertentu. Fungsi tersebut akan mengambil semua _entry_ data pada model CatalogItem, yang kemudian di-_passing_ kepada halaman HTML. Fungsi show_katalog akan mengembalikan hasil _render_ halaman HTML tersebut dan ditampilkan kepada pengguna.

Selain itu, meskipun class CatalogItem di models.py telah didefinisikan, class tersebut masih belum terbuat modelnya di database. Oleh karena itu, perlu dilakukan makemigrations dan migrate terlebih dahulu agar tabel dapat digunakan. Data-data katalog berbentuk file .json yang diberikan pun belum masuk ke database sehingga perlu dilakukan _load data_ terlebih dahulu.

**Poin 2**: Agar fungsi show_katalog sebelumnya dapat digunakan, perlu dispesifikasi path atau _urlpattern_ apa yang akan memanggil fungsi tersebut. Hal tersebut dilakukan pada berkas urls.py, baik pada folder project_django maupun folder katalog.

Pada urls.py di folder project_django, dituliskan: ketika pengguna mengakses path katalog/, _request_ akan diteruskan ke urls.py milik folder katalog. Kemudian, pada berkas urls.py di folder katalog akan dispesifikasi lagi sub-path mana yang diakses dan nantinya memanggil suatu fungsi di views.py yang sesuai. Pada kasus ini, subpath '' dispesifikasi ke views show_katalog. Maka, ketika pengguna mengakses localhost.com/katalog/, fungsi show_katalog di views.py akan dipanggil.

**Poin 3**: Untuk menampilkan halaman response ke pengguna, perlu adanya berkas HTML dimana sifatnya sebagai template. Data yang sebelumnya sudah di-_passing_ di views.py dapat dimasukan ke dalam berkas HTML menggunakan _syntax_ {{ nama_key }}. Ingat bahwa data yang dimasukkan berupa dictionary, berbentuk pasangan key dan value, dan yang ditulis di HTML adalah key-nya. Untuk mengisi HTML dengan data dari model, perlu dilakukan looping untuk menampilkan setiap instance/_entry_ dari CatalogItem. 

**Poin 4**: Untuk melakukan deployment, saya membuat aplikasi baru di Heroku dan memasukan action secret pada repository GitHub yang sesuai. Kemudian, semua berkas aplikasi dipush ke GitHub. GitHub akan memproses deployment ini dan prosesnya sangat cepat apabila set-up dilakukan dengan benar. Heroku menyediakan opsi auto-deploy agar apabila suatu saat terdapat perubahan isi berkas, aplikasi yang ter-deploy di Heroku akan berubah sendiri sesuai berkas yang telah dipush di GitHub.

## Tests
---

Untuk melakukan unit testing, jalankan perintah<br>
```python manage.py test katalog.tests```

## Credits
---

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.