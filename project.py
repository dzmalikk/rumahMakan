#M. Dzaki Irsyadul Malik, 10 Komputer 1

from os import system

print("----RUMAH MAKAN ABCD----")
access = input("Akses sebagai (Penjual(A)/Pembeli(B)) ? = ")
access = access.upper()

def searching_kode_mkn(makanan):
	if {data_mkn[makanan['kode']]} in data_mkn:
		return True
	else:
		print("Menu tidak ditemukan")
		return False
def searching_kode_mnm(minuman):
	if {data_mnm[minuman['kode']]} in data_mnm:
		return True
	else:
		print("Menu tidak ditemukan")
		return False

def searching_menu_mkn(makanan):
	if makanan in data_mkn:
		return True
	else:
		print("Menu tidak ditemukan")
		return False

def searching_menu_mnm(minuman):
	if minuman in data_mnm:
		return True
	else:
		print("Menu Tidak ditemukan")
		return False


data_mkn = {
		"Nasi Goreng" : {
			"harga" : 15000,
			"kode" : "1A"
		},
		"Mie Goreng" : {
			"harga" : 10000,
			"kode" : "2A"
		},
		"Nasi Ayam" : {
			"harga" : 20000,
			"kode" : "3A"
		}
	}

data_mnm = {
		"Es Teh" : {
			"harga" : 5000,
			"kode" : "1B"
		},
		"Air Putih" : {
			"harga" : 2000,
			"kode" : "2B"
		}
	}

if access == "A":
	#password = 123456
	kodeakses = input("Masukkan password : ")
	while kodeakses != "123456":
		print("Password Salah")
		kodeakses = input("Masukkan password : ")

	def view_menuA():
		system("cls")
		print("""
[A] Tampilkan Menu
[B] Menambah Menu Baru
[C] Memperbarui Menu
[D] Menghapus Menu 
[Q] Keluar
		""")

	def tampilkan_menu():
		system("cls")
		menu = input("Makanan / Minuman (MKN/MNM) : ")
		menu = menu.upper()
		if menu == "MKN":
			print("-----MAKANAN-----")
			for makanan in data_mkn:
				makanan = makanan
				harga = data_mkn[makanan]['harga']
				kode = data_mkn[makanan]['kode']
				print(f"{makanan}\nHarga = {harga}\nKode = {kode}")
			input("Tekan ENTER untuk kembali ke menu")

		elif menu == "MNM":
			print("---MINUMAN---")
			for minuman in data_mnm:
				minuman = minuman
				harga = data_mnm[minuman]['harga']
				kode = data_mnm[minuman]['kode']
				print(f"{minuman}\nHarga = {harga}\nKode = {kode}")
			input("Tekan ENTER untuk kembali ke menu")

	def verify_ans(pilihanA):
		pilihanA = pilihanA.upper()
		if pilihanA == "Y":
			return True
		else:
			return False


	def menambah_menu():
		system("cls")
		print("----Menambah Menu Baru----")
		menambahapa = input("Menambah menu apa? (MKN/MNM) = ")
		menambahapa = menambahapa.upper()
		if menambahapa == "MKN":
			makanan = input("Menu baru = ")
			harga = input("Harga = ")
			kode = input("Kode = ")

			penjual_ans = input("Tekan Y untuk menyimpan (Y/N) = ")

			if verify_ans(penjual_ans):
				print("Menyimpan menu baru ...")
				data_mkn[makanan] = {
					"harga" : harga,
					"kode" : kode
				}
				print("Data tersimpan")

			else:
				print("Data tidak tersimpan")

		else:
			minuman = input("Menu baru = ")
			harga = input("Harga = ")
			kode = input("Kode = ")

			penjual_ans = input("Tekan Y untuk menyimpan (Y/N) = ")

			if verify_ans(penjual_ans):
				print("Menyimpan menu baru ...")
				data_mnm[minuman] = {
					"harga" : harga,
					"kode" : kode
				}
				print("Data tersimpan")

			else:
				print("Data tidak tersimpan")

		input("Tekan ENTER untuk kembali ke menu")

	def memperbarui_harga_mkn(makanan):
		harga_baru = input("Harga baru = ")
		pilihanA = input("Apakah anda yakin untuk memperbarui menu (Y/N) ? = ")
		if verify_ans(pilihanA):
			data_mkn[makanan]['harga'] = harga_baru
			print("Menu telah diperbarui")
		else:
			print("Menu batal diperbarui")

	def memperbarui_kode_mkn(makanan):
		kode_baru = input("Kode baru = ")
		pilihanA = input("Apakah anda yakin untuk memperbarui menu (Y/N) ? = ")
		if verify_ans(pilihanA):
			data_mkn[makanan]['kode'] = kode_baru
			print("Menu telah diperbarui")
		else:
			print("Menu batal diperbarui")

	def memperbarui_harga_mnm(minuman):
		harga_baru = input("Harga baru = ")
		pilihanA = input("Apakah anda yakin untuk memperbarui menu (Y/N) ? = ")
		if verify_ans(pilihanA):
			data_mnm[minuman]['harga'] = harga_baru
			print("Menu telah diperbarui")
		else:
			print("Menu batal diperbarui")

	def memperbarui_kode_mnm(minuman):
		kode_baru = input("Kode baru = ")
		pilihanA = input("Apakah anda yakin untuk memperbarui menu (Y/N) ? = ")
		if verify_ans(pilihanA):
			data_mnm[minuman]['kode'] = kode_baru
			print("Menu telah diperbarui")
		else:
			print("Menu batal diperbarui")


	def memperbarui_menu():
		system("cls")
		print("----MEMPERBARUI MENU----")
		memperbaruiapa = input("Menu apa yang akan diperbarui (MKN/MNM)? = ")
		memperbaruiapa = memperbaruiapa.upper()
		if memperbaruiapa == "MKN":
			makanan = input("Makanan apa yang ingin diperbarui = ")
			result = searching_menu_mkn(makanan)
			if result:
				print("Apa yang ingin diperbarui ?\n[1] Harga\n[2] Kode")
				pilihanA = input("Pilihan = ")
				if pilihanA == "1":
					memperbarui_harga_mkn(makanan)
				elif pilihanA == "2":
					memperbarui_kode_mkn(makanan)

		elif memperbaruiapa == "MNM":
			minuman = input("Minuman apa yang ingin diperbarui = ")
			result = searching_menu_mnm(minuman)
			if result:
				pilihanA = input("Apa yang ingin diperbarui ?\n[1] Harga\n[2] Kode\nPilihan = ")
				if pilihanA == "1":
					memperbarui_harga_mnm(minuman)
				elif pilihanA == "2":
					memperbarui_harga_mnm(minuman)
		input("Tekan ENTER untuk kembali ke menu")

	def menghapus_menu():
		system("cls")
		print("----MENGHAPUS MENU----")
		menghapusapa = input("Menu apa yang akan dihapus (MKN/MNM)? =")	
		menghapusapa = menghapusapa.upper()
		if menghapusapa == "MKN":
			makanan = input("Makanan apa yang akan dihapus = ")
			result = searching_menu_mkn(makanan)
			if result:
				pilihanA = input("Apakah Anda yakin untuk menghapus menu ini (Y/N)? = ")
				if verify_ans(pilihanA):
					del data_mkn[makanan]
					print("Menu telah dihapus")
				else:
					print("Menu tidak terhapus")

		if menghapusapa == "MNM":
			minuman = input("Minuman apa yang akan dihapus = ")
			result = searching_menu_mnm(minuman)
			if result:
				pilihanA = input("Apakah Anda yakin untuk menghapus menu ini (Y/N)? = ")
				if verify_ans(pilihanA):
					del data_mnm[minuman]
					print("Menu telah dihapus")
				else:
					print("Menu tidak terhapus")

		input("Tekan ENTER untuk kembali ke menu")			

	def check_inputA(pilihanA):
		pilihanA = pilihanA.upper()
		if pilihanA == "Q":
			return True
		elif pilihanA == "A":
			tampilkan_menu()
		elif pilihanA == "B":
			menambah_menu()
		elif pilihanA == "C":
			memperbarui_menu()
		elif pilihanA == "D":
			menghapus_menu()

	stop = False
	while not stop:
		view_menuA()
		penjual_input = input("Pilihan : ")
		stop = check_inputA(penjual_input)


elif access == "B":
	def view_menuB():
		system("cls")
		print("""
[A] Tampilkan Menu
[B] Mencari Menu
[Q] Keluar
			""")

	def mencari_menu():
		system("cls")
		print("----MENCARI MENU----")
		menuapa = input("Menu apa yang ingin dicari (MKN/MNM) ? = ")
		menuapa = menuapa.upper()
		if menuapa == "MKN":
			makanan = input("Makanan apa yang ingin dicari = ")
			result = searching_menu_mkn(makanan)
			if result:
				print(f"{makanan}\nHarga = {data_mkn[makanan]['harga']}\nKode = {data_mkn[makanan]['kode']}")
		
		elif menuapa == "MNM":
			minuman = input("Minuman apa yang ingin dicari = ")
			result = searching_menu_mnm(minuman)
			if result:
				print(f"{minuman}\nHarga = {data_mnm[minuman]['harga']}\nKode = {data_mnm[minuman]['kode']}")
			
		input("Tekan ENTER untuk kembali ke menu")

	def tampilkan_menu():
		system("cls")
		menu = input("Makanan / Minuman (MKN/MNM) : ")
		menu = menu.upper()
		if menu == "MKN":
			print("-----MAKANAN-----")
			for makanan in data_mkn:
				makanan = makanan
				harga = data_mkn[makanan]['harga']
				kode = data_mkn[makanan]['kode']
				print(f"{makanan}\nHarga = {harga}\nKode = {kode}")
		
		elif menu == "MNM":
			print("----MINUMAN----")
			for minuman in data_mnm:
				minuman = minuman
				harga = data_mnm[minuman]['harga']
				kode = data_mnm[minuman]['kode']
				print(f"{minuman}\nHarga = {harga}\nKode = {kode}")
		input("Tekan ENTER untuk kembali ke menu")

	def check_inputB(pilihanB):
		pilihanB = pilihanB.upper()
		if pilihanB == "Q":
			return True
		elif pilihanB == "A":
			tampilkan_menu()
		elif pilihanB == "B":
			mencari_menu()

	stop = False
	while not stop:
		view_menuB()
		pembeli_input = input("Pilihan : ")
		stop = check_inputB(pembeli_input)