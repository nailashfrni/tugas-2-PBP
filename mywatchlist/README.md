# Tugas 3 PBP: My Watch List

## Heroku Link

[Click Here](https://katalog-app-pbp.herokuapp.com/mywatchlist/)
<br><br>

## Questions

### **1. Perbedaan antara JSON, XML, dan HTML**<br><br>
Hyper Text Markup Language (HTML) adalah bahasa yang digunakan untuk membentuk struktur halaman web, sebagai markup yang mengindikasikan bagian-bagian dari web yang akan ditampilkan di browser. Halaman HTML terdiri dari berbagai HTML tag untuk mengatur konten dan strukturnya yang memiliki fungsi masing-masing.

eXtensible Markup Language (XML) biasanya digunakan untuk menyajikan data terstruktur ataupun pesan. Mirip dengan HTML, data-data pada XML ditulis dalam XML tag, di mana setiap tag mendeskripsikan atribut yang dipunya oleh data.

JavaScript Object Notation (JSON) umumnya digunakan untuk menyimpan dan mengirim data, mirip dengan XML. Namun, penulisan data di JSON merupakan pasangan key-value dan juga array, bukan berupa tag. Syntax JSON mirip dengan syntax JavaScript Object. Hal ini dapat memberi kemudahan apabila pengguna meminta data berformat JSON karena datanya dapat langsung diubah menjadi object pada JavaScript.

|HTML|XML|JSON|
|---------------|---------------------|--------------------|
|Extension file berupa .html|Extension file berupa .xml|Extension file berupa .json|
|Berfokus untuk menampilkan halaman data|Berfokus pada transfer data|Berfokus pada transfer data|
|HTML berfungsi untuk _markup_ atau mengatur struktur konten di web browser|XML digunakan untuk _markup_ yang berarti dapat menampilkan konten/data|JSON tidak dapat menampilkan konten|
|Case insensitive|Case sensitive|Case insensitive|
|Elemen HTML berupa tag|Data di XML menggunakan tag|JSON data tidak memiliki tag|
|Tidak membutuhkan code tambahan untuk parsing text, dapat langsung memakai eval function di JavaScript|Sulit untuk dilakukan _parse_|Sangat mudah dilakukan _parsing_ ke javascript object|
|HTML bersifat document-oriented|XML bersifat document-oriented|JSON bersifat data-oriented|
|Ukuran file HTML tidak terlalu besar|XML umumnya lebih sulit dibuat dan ukuran filenya lebih besar|Ukuran JSON file tidak terlalu besar|

### **2. Mengapa diperlukan _data delivery_ dalam pengimplementasian platform?**<br><br>
Data menjadi aspek terpenting dalam mengembangkan suatu aplikasi. Semua hal yang terjadi di aplikasi, baik dari sisi klien ataupun server, disimpan dalam bentuk data. Kebutuhan untuk dapat mengolah dan menganalisis data tersebut membuat diadakannya suatu fitur disebut _data delivery_.

_Data delivery_ adalah proses pengiriman data dari suatu aplikasi tertentu. _Data delivery_ memungkinkan suatu pihak mengirim _request_ data kepada server yang nantinya akan diolah untuk kepentingan bisnis atau pengembangan aplikasi ke depannya. Untuk melakukan proses _data delivery_ tersebut, diperlukan suatu struktur atau format yang mendefinisikan data. Struktur tersebut dapat berupa XML atau JSON.

_Data delivery_ juga sangat berguna apabila kita mengembangkan aplikasi berbasis web dan mobile sekaligus. Agar data pada kedua aplikasi tersebut bisa tetap tersinkronisasi dengan baik, tentu kita tidak bisa menyimpan datanya secara terpisah. Di situlah _developer_ memanfaatkan adanya _data delivery_. Data akan disimpan dalam satu tempat yang dapat diakses oleh semua aplikasi dari berbagai platform sekaligus. Saat pengguna mengirim _request_ untuk mengakses data melalui aplikasi mobile, _request_ tersebut akan diteruskan kepada server untuk mendapatkan data-datanya (proses _data delivery_). Begitu juga apabila pengguna mengakses data melalui aplikasi web, akan dikirimkan _request_ ke server yang sama. Dengan begitu, _developer_ cukup mengurus data di satu tempat saja untuk digunakan di banyak tempat sekaligus. _Data delivery_ juga dapat meningkatkan keamanan karena data terpusat pada 1 tempat dan tidak dapat diakses oleh sembarang pihak.

### **3. Proses Pengerjaan**<br><br>
Untuk membuat app baru dalam project Django, saya menjalankan perintah ```python manage.py startapp mywatchlist``` dan menambahkan aplikasi mywatchlist pada settings.py

Ketika men-generate app tadi, akan terbuat folder yang berisi models.py, views.py, tests.py, dan sebagainya. Pada file models.py, tambahkan class baru MyWatchList sebagai model dan juga spesifikasikan atribut apa saja yang dimiliki. Models tersebut kemudian dimigrate agar terdaftar dalam database.

Untuk menambahkan 10 data pada MyWatchList, saya membuat file .json pada folder fixtures. File tersebut berisi data-data film berdasarkan format JSON sesuai atribut yang sebelumnya dispesifikasikan. Kemudian, saya menjalankan perintah loaddata untuk menambahkan data-data JSON tersebut pada database.

Setelah itu, saya membuat 3 buah fungsi baru pada views.py untuk meng-handle request yang diberikan pengguna, masing-masing untuk request HTML, XML, dan JSON. Saya juga membuat halaman HTML baru yang berfungsi untuk menampilkan data-data dari model, yang akan ditampilkan saat pengguna mengirim request untuk html-nya.

Agar aplikasi mywatchlist dapat diakses melalui browser, saya menambahkan path baru dalam urls.py pada folder project_django dan mywatchlist, dengan handler yang sesuai pada views. Sebelum dilakukan push ke github, saya menambahkan perintah loaddata di Procfile agar data JSON yang sebelumnya saya buat dapat terdaftar di aplikasi Heroku. Langkah terakhir, saya melakukan push berkas-berkas ke GitHub dan secara otomatis Heroku akan melakukan deployment aplikasi baru yang saya buat.

## Screenshot Postman
HTML
![HTML](../assets/Tugas%203/postman-html.png)
<br>

XML
![XML](../assets/Tugas%203/postman-xml.png)
<br>

JSON
![JSON](../assets/Tugas%203/postman-json.png)
<br>

## Tests

Untuk melakukan _unit testing_, jalankan perintah<br>
```python manage.py test mywatchlist```

## Referensi
- Slide Data Delivery PBP Ganjil 2022/2023
- https://www.javatpoint.com/json-vs-xml
- https://www.guru99.com/xml-vs-html-difference.html#:~:text=XML%20is%20abbreviation%20for%20extensible,while%20HTML%20is%20Case%20insensitive.