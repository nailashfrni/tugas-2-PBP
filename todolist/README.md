# Tugas 4 PBP: To-do List

## Heroku Link

[Click Here](https://katalog-app-pbp.herokuapp.com/todolist/)
<br><br>

## Questions

### **1. Kegunaan {% csrf_token %}**<br>
`{% csrf_token %}` pada elemen `<form>` berfungsi untuk membuat (_generate_) token keamanan demi mencegah terjadinya serangan CSRF (Cross Site Request Forgery). CSRF sendiri adalah serangan yang memungkinkan _attacker_ melakukan sesuatu yang tidak seharusnya dilakukan, tanpa sepengetahuan pemiliknya, seperti mengubah email/password tanpa izin. Dengan mengimplementasikan CSRF Token, setiap session akan mempunyai token yang bersifat unik dan berupa kode acak yang panjang sehingga sulit ditebak oleh orang lain. Apabila tidak menggunakan `{% csrf_token %}` pada `<form>`, `<form>` akan tetap berjalan sebagaimana mestinya. Namun, tidak ada mekanisme pencegahan sehingga lebih rentan terkena serangan CSRF.

### **2. Apakah bisa membuat form secara manual?**<br>
Bisa, form pada Django dapat dibuat secara manual. Pada berkas HTML, form dapat dibuat dengan tag/elemen `<form>`. Di dalam elemen tersebut dapat ditambahkan beberapa elemen `<input>` sesuai jumlah isian (+input submit) yang diinginkan. Elemen `<input>` memiliki beberapa tipe, seperti isian teks singkat, checkbox, radio button, color, tombol submit, dan masih banyak lagi.

Pada elemen `<form>` perlu dispesifikasikan atribut action dan method. Action memberi informasi halaman/path/fungsi mana yang akan menghandle request form setelah disubmit, sedangkan method mendefinisikan HTTP Request Method yang akan digunakan ketika mengakses path pada action. 

Kemudian, buat pula fungsi pada views.py untuk meng-_handle_ request yang diterima dari form. Di dalam fungsi tersebut dapat disesuaikan operasi apa yang akan dilakukan kepada database, misal menambah data, mengupdate data, dll. Data input dari form bisa didapat dengan request.POST.get(nama_field).

### **3. Alur submisi pengguna melalui HTML Form, penyimpanan data, sampai tampilnya data di template HTML**<br>
Pengguna memasukan data submisi melalui form di HTML. Data-data tersebut akan terkirim melalui method POST dan requestnya akan di-_handle_ oleh fungsi yang sesuai di views.py. Pada views, data-data submisi tersebut diambil dan divalidasi, termasuk mekanisme pencegahan CSRF. Apabila datanya valid, data disimpan ke database (atau bisa juga diolah terlebih dahulu sesuai kebutuhan). Views tersebut akan melakukan _redirect_ atau pengalihan akses langsung ke fungsi yang akan menampilkan data-data di HTML. Karena data submisi telah tersimpan di database, ketika fungsi views mengambil data dari database, data tersebut akan terambil dan bisa dirender ke dalam template HTML. Dengan demikian, data submisi yang baru saja dimasukan pengguna dapat langsung ditampilkan di halaman HTML.

### **4. Cara Implementasi _Checklist_**<br>
Pertama-tama, saya membuat aplikasi todolist dengan command `python manage.py startapp todolist` yang akan membuat folder baru todolist dan beberapa file di dalamnya. Saya juga mendaftarkan aplikasi todolist di INSTALLED_APPS pada settings.py. 

Kemudian, saya membuat model Task pada models.py yang di dalamnya memiliki atribut sesuai tipe datanya masing-masing. Lakukan pula makemigrations dan migrate untuk menyimpan model tersebut di database. Tambah path `todolist/` pada urls.py di project_django untuk mengimplementasikan aplikasi todolist dapat diakses.

**Membuat Form Registrasi dan Login**<br>
Saya membuat fungsi register dan login_user pada views.py. Fungsi tersebut akan menghandle 2 method: GET dan POST. Apabila pengguna mengakses dengan GET, fungsi tersebut akan menampilkan halaman form HTML. Apabila pengguna mengakses dengan method POST, data submisi register/login pengguna akan divalidasi dan disimpan dalam database. Pengguna kemudian diarahkan ke halaman selanjutnya.

Setelah views, saya mengimplementasikan register.html dan login.html berupa halaman form HTML yang akan diisi oleh pengguna. Saya juga menambahkan path register/ dan login/ pada urls.py agar dapat diakses pengguna.

**Membuat Halaman Utama To-do List**<br>
Buat fungsi show_todolist pada views.py yang akan mengambil semua data to-dolist milik user yang login, dan masukan data-data tersebut untuk dirender ke halaman HTML. Fungsi tersebut perlu ditambah decorator login_required agar hanya dapat diakses apabila user telah login. Buat pula berkas todolist.html yang akan menampilkan table berisi data-data task milik user dan button yang akan mengarah ke halaman buat task baru. Buat juga button logout yang akan mengarahkan ke path logout user. Tidak lupa tambahkan path '' di urls.py agar dapat diakses user.

**Membuat Fungsi Logout**<br>
Buat fungsi logout pada views, di dalamnya hanya memanggil fungsi logout(user) milik Django. Setelah berhasil logout, user akan diarahkan langsung ke halaman login. Tambahkan pula path `logout/` di urls.py agar dapat diakses.

**Halaman Buat Task Baru**<br>
Buat file forms.py yang berisi class baru TaskForm untuk membuat form. Di dalamnya dispesifikasikan isian apa saja yang akan diisi pada form, yakni title dan description. Buat fungsi di views yang akan menghandle request buat task baru, untuk method GET dan POST. Apabila pengguna mengakses dengan GET, views akan menampilkan halaman HTML untuk membuat task baru. Namun, apabila pengguna mengakses dengan POST, pengguna berarti mengirimkan data melalui form. Data tersebut akan divalidasi dan disimpan ke dalam database. Kemudian fungsi tersebut akan mengalihkan langsung ke halaman utama todolist.

Buat pula halaman HTML baru untuk menampilkan form. Form akan di-generate secara otomatis menggunakan `{{ form.as_table }}`. Tambahkan pula input submit untuk mengirim data-data yang diisi ke server. Terakhir, tambahkan path `create-task/` pada urls.py agar dapat diakses user. 

**Finishing**<br>
Saya melakukan push berkas-berkas ke GitHub dan secara otomatis Heroku akan melakukan deployment aplikasi baru yang saya buat. Akses web heroku dan buat 2 akun serta 3 task pada masing-masing akunnya. Tambahkan superuser melalui heroku bash, dengan command `python manage.py createsuperuser`. Setelah membuat super user, data-data yang dimasukkan dapat dicek dengan mengakses `<web-heroku-app>/admin` dengan login memakai superuser.

## Referensi
- Slide Form, Authentication, Session, and Cookie PBP Ganjil 2022/2023
- https://portswigger.net/web-security/csrf

<br>

# Tugas 5 PBP: To-do List ~ Web Design Using HTML, CSS, and CSS Framework

## Questions

### **Perbedaan Inline, Internal, dan External CSS**<br>
|Perbedaan|Inline|Internal|External|
|--------|--------|--------|--------|
|Peletakan CSS|Ditulis langsung pada atribut elemen HTML|Ditulis di dalam berkas HTML|Ditulis di file CSS terpisah, di luar file HTML|
| Kelebihan | Sangat berguna jika ingin melihat perubahan style satu elemen|Hanya dapat mengatur style pada satu halaman saja|Struktur HTML lebih rapi karena tidak tercampur dengan styling|
| | Memiliki bobot yang tertinggi sehingga perubahan style dapat langsung terdeteksi|File yang dibuat lebih sedikit karena HTML dan CSS digabung di dalam file yang sama|Loading website lebih cepat|
| | Proses request HTTP lebih kecil sehingga website dapat diload lebih cepat|Class dan ID dapat digunakan oleh internal stylesheet|Dapat mengatur CSS pada beberapa halaman sekaligus
|Kekurangan|CSS hanya bisa diterapkan pada satu elemen sehingga tidak efisien|Tidak efisien jika menggunakan CSS yang sama pada beberapa halaman|Web akan menjadi berantakan apabila file CSS tidak berhasil diload|
|||Performa web menjadi lebih lambat karena akan loading ulang CSS setiap berganti halaman|

### **Tag HTML5 yang diketahui**<br>
- `<a>` untuk membuat anchor atau link 
- `<body>` menspesifikasi body dari halaman HTML
- `<br>` menyisipkan sebuah _line break_
- `<button>` menspesifikasikan button
- `<div>` menspefisikasikan section pada suatu halaman
- `<b>` membuat text yang bold atau tebal
- `<i>` membuat text yang italic (miring)
- `<form>` menspesifikasikan form dalam halaman
- `<h1> - <h6>` untuk membuat header, dimana h1 berukuran paling besar dan h6 paling kecil
- `<img>` menyisipkan gambar
- `<label>` menspesifikasikan label pada suatu form control
- `<p>` menspesifikasikan paragraf
- `<table>` menspesifikasikan table

### **Tipe-tipe CSS selector**<br>
1. Universal selector (*)<br>
Selector untuk memilih semua elemen pada HTML.
Syntax: `*`, `ns|*`, `*|*`

2. Type selector<br>
Memiliih semua elemen dengan node tertentu. Syntax: `namaelemen`.<br>
Contoh: `p` akan match dengan semua elemen `<p>`.

3. Class selector<br>
Memilih semua elemen dengan atribut class tertentu. Syntax: `.namaclass`.<br>
Contoh: `.btn` akan match dengan semua elemen yang mempunyai atribut `class="btn"`.

4. ID selector<br>
Memilih semua elemen dengan atribut ID tertentu. Syntax: `#namaID`.<br>
Contoh: `#tombol-submit` akan match dengan semua elemen yang mempunyai atribut `id="tombol-submit"`.

5. Attribute selector<br>
Memilih semua elemen yang memiliki atribut tertentu.
Contoh: `[autoplay]` akan match dengan semua elemen yang memiliki atribut `autoplay`.

5. Grouping Selector
    - Selector list `,` adalah metode grouping beberapa node, dimana akan memilih semua elemen yang match. Contoh: `div, span` akan match dengan semua elemen `<div>` dan `<span>`.

    - Selector `" "` akan menyeleksi semua node yang merupakan keturunan dari elemen pertama. Contoh: `div span` akan match dengan semua elemen `<span>` yang ada di dalam elemen `<div>`.

    - `>` combinator akan memilih node yang merupakan anak langsung dari elemen pertama. Contoh: `tr > td` akan match dengan semua elemen `<td>` yang merupakan anak langsung dari elemen `<tr>`.

    - `A ~ B` akan memilih semua elemen B yang diikuti oleh elemen A (langsung ataupun tidak), dan memiliki parent yang sama.

    - `A + B` akan match semua elemen B yang langsung diikuti oleh elemen A.

    - `A || B` akan match semua elemen B yang berada di dalam scope A.

6. Pseudo classes
    `:` memilih elemen berdasarkan informasi status. Contoh: `a:hover` akan match dengan semua elemen `<a>` saat cursor berada di atasnya.

7. Pseudo-elements
    Contoh: `p::first-line` akan match dengan baris pertama pada semua elemen `<p>`.

### **Implementasi _Checklist_**<br>
1. Setting up pada template base.html agar dapat menggunakan komponen bootstrap.
2. Melakukan styling semua elemen HTML dengan memanfaatkan class bootstrap, dengan kombinasi inline, internal, dan external CSS.
3. Kerap kali saya juga mencari inspirasi template melalui internet.

## Referensi
- https://idwebhost.com/blog/css-adalah-perbedaan-internal-css-external-css-inline-css/
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors?retiredLocale=id