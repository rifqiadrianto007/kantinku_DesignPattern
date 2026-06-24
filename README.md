# Kantinku

Kantinku adalah aplikasi kasir kantin sederhana berbasis command line. Project ini dibuat untuk mendemonstrasikan beberapa design pattern dalam Python sambil tetap bisa digunakan untuk alur order dasar: customer memasukkan nama, memilih menu, menambah topping, mengonfirmasi order, dan menandai order selesai.

## Fitur

- Input nama customer.
- Menampilkan daftar menu makanan dan minuman.
- Memilih menu dan jumlah pesanan.
- Menambahkan topping sesuai kategori menu.
- Menghitung total harga otomatis.
- Menyimpan order ke database sederhana berbentuk dictionary di memori.
- Memberi notifikasi status order ke dapur, kasir, dan display.

## Struktur Project

```text
kantinku/
├── factory.py
├── main.py
├── observer.py
├── topping.py
└── README.md
```

Penjelasan file:

- `main.py`: entry point aplikasi. Berisi data menu, data topping, database order, validasi input, dan alur utama pemesanan.
- `factory.py`: berisi class menu dan factory untuk membuat objek `FoodItem` atau `DrinkItem`.
- `topping.py`: berisi decorator generic `MenuTopping` untuk menambahkan topping ke menu.
- `observer.py`: berisi sistem order dan observer untuk notifikasi kitchen, cashier, dan display.

## Design Pattern yang Digunakan

### 1. Creational Pattern

Creational Pattern digunakan di `factory.py` melalui `MenuFactory`.

Tujuannya adalah membuat objek menu berdasarkan kategori tanpa membuat objek `FoodItem` atau `DrinkItem` secara langsung di `main.py`.

Contoh:

```python
item = MenuFactory.create("Drink", "Americano", 20000)
```

Jika kategori adalah `Drink`, factory akan membuat `DrinkItem`. Jika kategori adalah `Food`, factory akan membuat `FoodItem`.

### 2. Topping Pattern

Structural Pattern digunakan di `topping.py` melalui `MenuTopping`.

Tujuannya adalah menambahkan topping ke item tanpa mengubah class asli item tersebut. Setiap topping menambah nama dan harga item.

Contoh:

```python
item = MenuTopping(item, "Milk", 3000)
```

Jika item awal adalah `Americano` seharga `Rp20,000`, setelah ditambah `Milk`, nama menjadi `Americano + Milk` dan harga menjadi `Rp23,000`.

### 3. Behavioral Pattern

Behavioral Pattern digunakan di `observer.py`.

Tujuannya adalah memberi notifikasi otomatis ketika status order berubah.

Observer yang tersedia:

- `KitchenObserver`: menerima notifikasi saat order dikonfirmasi.
- `CashierObserver`: menampilkan total saat order dikonfirmasi dan status selesai saat order complete.
- `DisplayObserver`: menampilkan status order ke display.

Contoh alur:

```python
order.confirm()
order.complete()
```

Saat status berubah, semua observer yang sudah di-attach akan menerima update.

## Database Sederhana

Project ini belum menggunakan database eksternal seperti SQLite atau MySQL. Data masih disimpan menggunakan dictionary di `main.py`.

### Menu

Data menu disimpan di `MENU_DB`.

```python
MENU_DB = {
    1: {"category": "Drink", "name": "Americano", "price": 20000},
    2: {"category": "Drink", "name": "Latte", "price": 24000},
}
```

### Topping

Data topping disimpan di `TOPPING_DB`.

```python
TOPPING_DB = {
    1: {
        "name": "Milk",
        "price": 3000,
        "categories": ["Drink"],
    },
}
```

Field `categories` menentukan topping tersebut boleh digunakan untuk kategori menu apa saja.

### Order

Order yang dibuat disimpan di `ORDER_DB`.

```python
ORDER_DB = {}
```

Database ini hanya hidup selama program berjalan. Jika program ditutup, data order akan hilang.

## Cara Menjalankan

Pastikan Python sudah terpasang, lalu jalankan:

```bash
python main.py
```

Jika menggunakan Windows dan command `python` tidak tersedia, coba:

```bash
py main.py
```

## Contoh Alur Penggunaan

1. Jalankan program.
2. Masukkan nama customer.
3. Pilih menu dari daftar.
4. Masukkan jumlah pesanan.
5. Pilih topping atau pilih `0` untuk tanpa topping.
6. Tambahkan pesanan lain jika diperlukan.
7. Lihat ringkasan order.
8. Konfirmasi order.
9. Tandai order selesai jika sudah diproses.

Contoh output ringkasan:

```text
==== RINGKASAN ORDER ====
Order #1
Customer : Rifqi
2 x Americano + Milk + Sugar -> Rp48,000
----------------------------------------
TOTAL : Rp48,000
```

## Cara Menambah Menu

Tambahkan data baru ke `MENU_DB` di `main.py`.

Contoh:

```python
7: {"category": "Drink", "name": "Chocolate", "price": 22000},
```

Kategori yang didukung oleh `MenuFactory` saat ini:

- `Food`
- `Drink`

Jika ingin menambah kategori baru, tambahkan class baru di `factory.py` dan update method `MenuFactory.create()`.

## Cara Menambah Topping

Tambahkan data baru ke `TOPPING_DB` di `main.py`.

Contoh topping untuk minuman:

```python
4: {
    "name": "Caramel",
    "price": 4000,
    "categories": ["Drink"],
},
```

Contoh topping yang bisa dipakai untuk makanan dan minuman:

```python
5: {
    "name": "Chocolate",
    "price": 3500,
    "categories": ["Food", "Drink"],
},
```

Tidak perlu membuat class topping baru di `topping.py`, karena `MenuTopping` sudah dibuat generic.
