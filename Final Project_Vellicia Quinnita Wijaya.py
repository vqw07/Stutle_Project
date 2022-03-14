
menu_obat = ["Paracetamol", "Decolgen", "Vitacimin"]
harga = {
    "Paracetamol": 20000,
    "Decolgen": 10000,
    "Vitacimin": 20000
}

stock = {
    "Paracetamol": 5,
    "Decolgen": 4,
    "Vitacimin": 3
}


def total_belanja(pembelian):
    total = 0
    for item in pembelian:
        stock_count = stock[item]
        if stock_count == 0:
            raise ValueError ("item %s is out of stock" % item)
        tot = harga[item]
        total += tot
        stock[item] -= 1
    return total

keranjang = []


print("Selamat Datang di Toko Obat Stutle")
print("Ketik Perintah untuk membuka menu")
print(
    " 1. List Obat \n 2. Beli Obat \n 3. Hapus Obat \n 4. Melihat Daftar Keranjang \n 5. Transaksi Pembelian"
)

perintah = ""
while perintah != "exit":
    print("Masukkan Perintah: ")
    perintah = input()

    if perintah == "list-obat":
            print(menu_obat)
    
    if not perintah.find("beli"):
        obat = perintah[5:]
        if obat in menu_obat:
            keranjang.append(obat)
            print("Anda berhasil memasukkan " + obat + " ke dalam keranjang")
            print("Keranjang Anda: "+ str(keranjang[0::]))
        else:
            print("Obat tidak ada di menu")
    
    if not perintah.find("hapus"):
        obat = perintah[6:]
        if obat in keranjang:
            keranjang.remove(obat)
            print("Anda berhasil hapus " + obat + " dari keranjang")
            print("Keranjang Anda: "+ str(keranjang[0::]))
        else:
            print("Obat tidak ada di keranjang")
    
    if perintah == "keranjang":
        print(keranjang)

    if perintah == "checkout":
        print("Total Belanjaan Anda sebesar: " + str(total_belanja(keranjang)))
        print("\nSisa Stock: \n")
        print(stock)
    
    if perintah == "exit":
        break
