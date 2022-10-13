# Tugas 6 PBP: AJAX

## Questions

### **1. Perbedaan _asynchronous programming_ dengan _synchronous programming_**<br>
- Asynchronous programming adalah programming yang memungkinkan pengguna bisa melakukan hal lain saat request sebelumnya masih diproses, sehingga tidak perlu menunggu dan bisa mengirim request secara bersamaan.
- Synchronous programming adalah programming yang prosesnya hanya bisa terjadi 1 kali dalam 1 waktu, tidak bisa ada beberapa request yang terkirim secara bersamaan. Dengan ini, pengguna harus menunggu request sebelumnya selesai diproses server dahulu, baru bisa melakukan task lain.

### **2. Paradigma _Event-Driven Programming_**<br>
Paradigma _event-driven programming_ adalah paradigma yang berfokus pada event yang terjadi dalam suatu program. Event tersebut akan mengatur alur dari program, dimana setiap event memiliki handler masing-masing. Saat programnya mulai, handler akan bersiap menerima event, sehingga saat event terjadi, handler tersebut baru akan mengeksekusi sesuai event yang didapatnya.

### **3. Penerapan _asynchronous programming_ pada AJAX**<br>
AJAX (Asynchronous Javascript & XML) adalah suatu teknik atau teknologi yang memungkinkan pengiriman request secara asinkronus. _Asynchronous programming_ pada AJAX dapat dilakukan melalui method jQuery $.ajax() yang mengirimkan request di background sehingga pengguna masih bisa melakukan hal lain, tanpa perlu menunggu request selesai diproses. Method tersebut menerima parameter seperti url yang akan diakses, HTTP Method yang digunakan, data yang akan dikirimkan, dll. Terdapat juga method jQuery lain yang mengimplementasikan AJAX seperti $.get() dan $.post().

### **4. Cara Implementasi _Checklist_**<br>
1. Membuat views baru untuk menampilkan data todolist berbentuk json sesuai user yang sedang login, tambahkan pula path baru di urls.py agar dapat diakses
2. Di dalam tag script di halaman HTML, ditambahkan function getJson untuk mendapatkan data-data dalam bentuk JSON dan ditampilkan ke HTML secara asinkronus dalam bentuk cards. Dibuat juga function JavaScript untuk membuat card.
3. Menambahkan elemen modal dari Bootstrap sebagai form menambahkan task baru
4. Buat views baru untuk menghandle request POST melalui ajax, yang mereturn JSON object berisi informasi task untuk digunakan di dalam HTML-nya. 
5. Tambahkan pula path add baru di urls.py yang dihubungkan ke views yang baru dibuat sebelumnya
5. Membuat function JavaScript untuk POST AJAX, yaitu dengan mengambil data dari form dan kirimkan request secara asinkronus. Setelah selesai, card baru akan terbuat dan isi dari form akan direset.

## Referensi
- https://www.outsystems.com/blog/posts/asynchronous-vs-synchronous-programming/
- https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_eventdriven_programming.htm
- https://medium.com/geekculture/asynchronous-programming-in-javascript-e1f47b3bf606