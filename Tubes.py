list_mahasiswa = []

def pilihannya():
    print('\nSilahkan pilih menu yang tersedia : ')
    print ("1. masukan data.")
    print ("2. tampilkan data. ")
    print ("3. hapus data. ")
    print ("4. cari data. ")
    print ("5. update data. ")
    print ("0. logout.")
    pilihan = int(input('Masukkan Pilihanmu : '))

def pilihannya() :
    if pilihannya == 1:
        masukkan_data()
    elif pilihannya == 2:
        tampilkan_data()
    elif pilihannya == 3: 
        hapus_data()
    elif pilihannya == 4:
        cari_data()
    elif pilihannya == 5:
        update_data()
    elif pilihannya == 0:
        logout ()
    
#==================================================#
def masukkan_data():
    print("\========================================")
    print("   Anda Berada Pada Menu Masukkan Data   ")
    print("=========================================")
    print("\nMasukkan Data Anda : ")
    print("_______________________")
    n = input("Nama Mahasiswa      :")
    a = input("Asal                :")
    b = input("NIM                 :")
    c = input("Nilai               :")
    f = open("tubes1.txt", "a")
    aw = open("tubes1.txt", "r")
    nu = n.upper()
    aw = close()
    pilihan = int(input("""
        Ketik 1 untuk coba lagi
        Ketik 2 untuk kembali ke menu utama
        Ketik 3 untuk keluar program
    """))
    if a == 1:
        file = open("tubes1.txt", "r")
        file = close()
        masukkan_data()
    elif a == 2:
        menu()
    elif a == 3:
        exit()
    #else :
        f.writelines([nu+","+a.upper()+","+b.upper()+","+c.upper()+"\n"])
    f.close()
    print("\nTekan [Enter] untuk melanjutkan")

    input ()
    menu()
#==================================================================#

def tampilkan_data():
    print("\n=============================")
    print("Anda Berada pada Menu Menampilkan Data ")
    print("===============================")
    f = open("tubes1.txt", "a")
    f = open("tubes1.txt", "r")
    print("Tekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#==================================================================#

def hapus_data():
    print("\=============================")
    print("Anda Berada pada Menu Menghapus Data ")
    print("==============================")

    hapus = input("Masukkan Nama Mahasiswa yang ingin dihapus :")
    oi = hapus.upper()
    f = open("tubes1.txt")
    isi = f.readlines()
    #isi.sort()

    idx = 0
    for i in isi:
        h = i.split(",")
        if oi in h [0]:
            del(isi[idx])
            print("\nData Anda Berhasil Dihapus")
        idx+=1
    f.close()

    f = open("tubes1.txt", "w")
    isi = f.writelines(isi)

    print("\nTekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#===============================================================#

def cari_data():
    print("\n================================")
    print("Anda Berada pada Menu Mencari Data")
    print("==================================")
    f = open("tubes1.txt")
    nc = input("Masukkan Nama yang ingin anda cari : ")
    qwe = nc.upper()
    isi = f.readlines()
    
    idx = 0
    for a in isi :
 #       print(a)
        x = a.split(",")
        if qwe in x[0] :
            print("Data ditemukan !!")
            print("Nama             : "+x[0])
            print("NIM              : "+x[1])
            print("Nilai            : "+x[2])
            print("Mata Kuliah      : "+x[3])
            print("Asal             : "+x[4])
        idx += 1
    print("\nTekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#=========================================================#