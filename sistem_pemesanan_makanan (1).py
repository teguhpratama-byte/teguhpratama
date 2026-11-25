# PROJECT SISTEM PEMESANAN MAKANAN
class MenuMakanan:

    # CONSTRUCTOR
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # PROPERTY GETTER NAMA
    @property
    def nama(self):
        return self.__nama

    # PROPERTY SETTER NAMA
    @nama.setter
    def nama(self, nama_baru):
        if nama_baru.strip() == "":
            raise ValueError("Nama makanan tidak boleh kosong!")

        self.__nama = nama_baru

    # PROPERTY GETTER HARGA
    @property
    def harga(self):
        return self.__harga

    # PROPERTY SETTER HARGA
    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga harus lebih dari 0!")

        self.__harga = harga_baru

    # PROPERTY GETTER STOK
    @property
    def stok(self):
        return self.__stok

    # METHOD MENGURANGI STOK
    def kurangi_stok(self, jumlah):
        if jumlah > self.__stok:
            raise ValueError("Stok makanan tidak mencukupi!")

        self.__stok -= jumlah

    # CLASS METHOD
    @classmethod
    def dari_data(cls, data):
        return cls(
            data["nama"],
            data["harga"],
            data["stok"]
        )


# ==================================================
# CLASS PEMESANAN
# ==================================================

class Pemesanan:

    # CONSTRUCTOR
    def __init__(self, nama_pelanggan):
        self.nama_pelanggan = nama_pelanggan
        self.__keranjang = {}
        self.__total = 0

    # STATIC METHOD
    @staticmethod
    def format_rupiah(angka):
        return "Rp {:,}".format(angka).replace(",", ".")

    # METHOD MENAMPILKAN MENU
    def tampilkan_menu(self, daftar_menu):

        print("\n========== DAFTAR MENU MAKANAN ==========")

        for nomor, menu in enumerate(daftar_menu, start=1):

            print(
                f"{nomor}. {menu.nama}"
                f" | Harga: {self.format_rupiah(menu.harga)}"
                f" | Stok: {menu.stok}"
            )

        print("=========================================")

    # METHOD MENAMBAHKAN PESANAN
    def tambah_pesanan(self, menu, jumlah):

        if jumlah <= 0:
            print("Jumlah pesanan harus lebih dari 0!")
            return

        if jumlah > menu.stok:
            print("Maaf, stok makanan tidak mencukupi!")
            return

        menu.kurangi_stok(jumlah)

        if menu not in self.__keranjang:
            self.__keranjang[menu] = 0

        self.__keranjang[menu] += jumlah

        print(
            f"\n{menu.nama} berhasil ditambahkan "
            f"ke keranjang!"
        )

    # METHOD MENAMPILKAN KERANJANG
    def tampilkan_pesanan(self):

        print("\n========== KERANJANG PESANAN ==========")

        if not self.__keranjang:
            print("Belum ada makanan yang dipesan!")
            return

        self.__total = 0

        for menu, jumlah in self.__keranjang.items():

            subtotal = menu.harga * jumlah
            self.__total += subtotal

            print(f"Nama makanan : {menu.nama}")
            print(f"Jumlah       : {jumlah}")
            print(
                f"Harga        : "
                f"{self.format_rupiah(menu.harga)}"
            )
            print(
                f"Subtotal     : "
                f"{self.format_rupiah(subtotal)}"
            )
            print("----------------------------------------")

        print(
            f"TOTAL PESANAN: "
            f"{self.format_rupiah(self.__total)}"
        )

        print("========================================")

    # METHOD MENGHITUNG TOTAL
    def hitung_total(self):

        self.__total = 0

        for menu, jumlah in self.__keranjang.items():
            self.__total += menu.harga * jumlah

        return self.__total

    # METHOD PEMBAYARAN / CHECKOUT
    def checkout(self):

        if not self.__keranjang:
            print("\nKeranjang pesanan masih kosong!")
            return

        total = self.hitung_total()

        print("\n========== PEMBAYARAN ==========")
        print("Nama pelanggan:", self.nama_pelanggan)
        print("Total bayar:", self.format_rupiah(total))

        # INPUT UANG PEMBAYARAN
        while True:

            try:
                uang = int(input("Masukkan uang pembayaran: Rp "))

                if uang < 0:
                    print("Pembayaran tidak boleh negatif!")
                    continue

                if uang < total:
                    print("Uang pembayaran tidak mencukupi!")
                    continue

                break

            except ValueError:
                print("Masukkan nominal berupa angka!")

        kembalian = uang - total

        # MENAMPILKAN STRUK
        print("\n")
        print("========================================")
        print("          STRUK PEMESANAN")
        print("========================================")
        print("Nama pelanggan:", self.nama_pelanggan)
        print("----------------------------------------")

        for menu, jumlah in self.__keranjang.items():

            subtotal = menu.harga * jumlah

            print(f"{menu.nama} x {jumlah}")
            print(
                f"Subtotal: "
                f"{self.format_rupiah(subtotal)}"
            )

        print("----------------------------------------")
        print("Total     :", self.format_rupiah(total))
        print("Pembayaran:", self.format_rupiah(uang))
        print("Kembalian :", self.format_rupiah(kembalian))
        print("========================================")
        print("     TERIMA KASIH TELAH MEMESAN!")
        print("========================================")

        # MENGOSONGKAN KERANJANG
        self.__keranjang.clear()
        self.__total = 0


# ==================================================
# PROGRAM UTAMA
# ==================================================

# DATA MENU MAKANAN DAN MINUMAN
data_menu = [

    {"nama": "Nasi Goreng", "harga": 15000, "stok": 20},
    {"nama": "Mie Ayam", "harga": 12000, "stok": 20},
    {"nama": "Ayam Geprek", "harga": 18000, "stok": 15},
    {"nama": "Bakso", "harga": 13000, "stok": 15},
    {"nama": "Sate Ayam", "harga": 20000, "stok": 10},
    {"nama": "Es Teh", "harga": 5000, "stok": 30},
    {"nama": "Es Jeruk", "harga": 7000, "stok": 25},
    {"nama": "Jus Alpukat", "harga": 10000, "stok": 15}

]


# MEMBUAT OBJECT MENU MENGGUNAKAN CLASS METHOD
daftar_menu = [

    MenuMakanan.dari_data(data)

    for data in data_menu

]


# MEMBUAT OBJECT PEMESANAN
pesanan = Pemesanan("Pelanggan")


# ==================================================
# MENU UTAMA PROGRAM
# ==================================================

while True:

    print("\n")
    print("========================================")
    print("       SISTEM PEMESANAN MAKANAN")
    print("========================================")
    print("1. Lihat Menu Makanan")
    print("2. Pesan Makanan")
    print("3. Lihat Keranjang Pesanan")
    print("4. Pembayaran / Checkout")
    print("5. Keluar")
    print("========================================")

    pilihan = input("Pilih menu (1-5): ")

    # MENU 1: MELIHAT DAFTAR MAKANAN
    if pilihan == "1":

        pesanan.tampilkan_menu(daftar_menu)

    # MENU 2: MEMESAN MAKANAN
    elif pilihan == "2":

        pesanan.tampilkan_menu(daftar_menu)

        try:

            nomor = int(input("\nPilih nomor makanan: "))

            if nomor < 1 or nomor > len(daftar_menu):
                print("Nomor menu tidak tersedia!")
                continue

            jumlah = int(input("Masukkan jumlah pesanan: "))

            pesanan.tambah_pesanan(
                daftar_menu[nomor - 1],
                jumlah
            )

        except ValueError:

            print("Input harus berupa angka!")

    # MENU 3: MELIHAT KERANJANG
    elif pilihan == "3":

        pesanan.tampilkan_pesanan()

    # MENU 4: PEMBAYARAN
    elif pilihan == "4":

        pesanan.checkout()

    # MENU 5: KELUAR
    elif pilihan == "5":

        print("\nTerima kasih telah menggunakan")
        print("Sistem Pemesanan Makanan!")

        break

    # JIKA INPUT SALAH
    else:

        print("\nPilihan tidak tersedia!")
        print("Silakan pilih menu 1 sampai 5.")
