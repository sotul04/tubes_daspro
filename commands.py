from argparse import *
from time import sleep
import os
from data_manipulate import *
from function import *
from data_type import *
from typing import List,Type
from undo import stack, undo

""" ================================ COMMANDs in GAME ======================================= """

#F13
def load(folder:List[str])->None:
# procedure load (input/output folder : array of string)
# Menjalankan load saat program pertama kali dijalankan dan mengubah nilai input/output
# folder menjadi path data eksternal yang digunakan jika tersedia, jika tidak program keluar

# KAMUS LOKAL
# parser : ArgumentParser
# args : parse_args
# foldr : string
# ALGORITMA
    parser = ArgumentParser()
    parser.add_argument("nama_folder",nargs="?",type=str,default="")
    args = parser.parse_args()
    foldr = args.nama_folder
    if foldr == "":
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: "+"\x1B[3m" + "python main.py" + "\x1B[0m" + " <nama_folder>")
        exit()
    elif os.path.isdir("save/"+foldr):
        print("Loading...")
        sleep(1.3)
        print("\nSelamat datang di program \"Manajerial Candi\"")
        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        folder[0] = "save/"+foldr
    else:
        print(f"\nFolder \"{foldr}\" tidak ditemukan.")
        exit()
#F14
def save(user:Type[user],candi:Type[candi],bahan:Type[bahan],stack:Type[stack])->None:
# procedure save(input user : user, input candi : candi, input bahan : bahan)
# Menjalankan prosedur save untuk menyimpan data perubahan selama permainan dijalankan

# KAMUS LOKAL
# path, folder, test, fold_temp : string
# repet, i : int
# ALGORITMA
    path = input("Masukkan nama folder: ")
    folder = "save"
    folder +="/"+path
    print("\nSaving...\n")
    repet = path_counter(folder)
    test = split(folder,"/")
    fold_temp = ''
    stack.pos, stack.users, stack.candi = 0, [], [] # mengosongkan stack
    for i in range(repet):
        if i > 0:
            fold_temp += "/"
        fold_temp += test[i]
        if not (os.path.isdir(fold_temp)):
            os.mkdir(fold_temp)
            print(f"Membuat folder {fold_temp}...")
            if i == repet-1:
                print()
            sleep(1)
        if i == repet-1:
            save_csv(user, fold_temp+"/user.csv")
            save_csv(candi, fold_temp+"/candi.csv")
            save_csv(bahan, fold_temp+"/bahan_bangunan.csv")
            print(f"Berhasil menyimpan data di folder {fold_temp}!\n")


#F08
def batch_kumpul(user:Type[user],bahan:Type[bahan],numbers:Type[number_colc])->None:
# procedure batch_kumpul(input user : user, input/output bahan : bahan, input/output numbers : number_colc)
# melakukan fitur F08 - batchkumpul

# KAMUS LOKAL
# data : array of string {menyimpan username-username bertipe jin pengumpul}
# racikan : array of int {menyimpan total bahan yang terkumpul}
# pasir, batu, air : int {menyimpan data acak bahan-bahan yang terkumpul}
# i : int
# ALGORITMA
    data = list_jin("jin_pengumpul", user)
    racikan = [0,0,0]
    if data[0] == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.\n")
    else:
        print(f"Mengerahkan {data[0]} jin untuk mengumpulkan bahan.")
        for i in range (data[0]):
            pasir = acak_kumpul(numbers)
            batu = acak_kumpul(numbers)
            air = acak_kumpul(numbers)
            racikan[0] += pasir
            racikan[1] += batu
            racikan[2] += air
        print(f"Jin menemukan total {racikan[0]} pasir, {racikan[1]} batu, {racikan[2]} air.\n")
        update_bahan(racikan, bahan)

def batch_bangun(user:Type[user],candi:Type[candi],bahan:Type[bahan],numbers:Type[number_colc])->None:
# procedure batch_bangun (input user : user, input/output candi : candi, input/output bahan : bahan, input/output numbers : number_colc)
# melakukan fitur F08 - batchbangun

# KAMUS LOKAL
# data : array of string {menyimpan username-username bertipe jin pembangun}
# bahan_total : array of int {menyimpan total bahan yang diperlukan untuk membangun candi}
# temp : array of [string, int, int, int] {menyimpan data jin pembangun dan bahan-bahan candi}
# bahan_cukup : bool
# kurang : array of int {menyimpan kekurangan bahan jika bahan tidak cukup}
# i : unt
# ALGORITMA
    data = list_jin("jin_pembangun", user)
    bahan_total = [0,0,0]
    if data[0] == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.\n")
    else:
        temp = [[] for i in range(data[0])]
        for i in range(data[0]):
            pasir = acak_bangun(numbers)
            batu = acak_bangun(numbers)
            air  = acak_bangun(numbers)
            temp[i] = [data[1][i],pasir,batu,air]
            bahan_total[0] += pasir
            bahan_total[1] += batu
            bahan_total[2] += air
        bahan_cukup = True
        for i in range(3):
            if bahan.detail[i+1][2] < bahan_total[i]:
                bahan_cukup = False
                break
        print(f"Mengerahkan {data[0]} jin untuk membangun candi dengan total bahan {bahan_total[0]} pasir, {bahan_total[1]} batu, dan {bahan_total[2]} air.")
        if bahan_cukup:
            update_bahan([-bahan_total[0],-bahan_total[1],-bahan_total[2]], bahan)
            for i in range(data[0]):
                add_candi(temp[i][0], [temp[i][1],temp[i][2],temp[i][3]], candi)
            print(f"Jin berhasil membangun total {data[0]} candi.\n")
        else:
            kurang = [0,0,0]
            for i in range (3):
                kurang[i] = bahan_total[i]-bahan.detail[i+1][2]
                if kurang[i] < 0:
                    kurang[i] = 0
            print(f"Bangun gagal. Kurang {kurang[0]} pasir, {kurang[1]} batu, {kurang[2]} air.\n")

# F09 - Ambil Laporan Jin
def laporanjin(user:Type[user],candi:Type[candi],bahan:Type[bahan])->None:
# procedure laporanjin(input user : user, input candi : candi, input bahan : bahan)
# melakukan prosedur pengambilan laporan jin

# KAMUS LOKAL
# total_jin, jin_kumpul, jin_bangun, jlh_pembuat, count, jumlah, index, jumlah_malas : int
# candi_list : array of [string, int] {menyimpan jumlah pembuat candi dan total candi yang telah dia bangun}
# jin_terajin, jin_termalas : string
# list_rajin : array of string {menyimpan username jin-jin terajin}
# list_malas : array of string {menyimpan username jin-jin termalas}
# i, j : int
# ALGORITMA
    total_jin = count_jin(user)[0]
    jin_kumpul = count_jin(user)[1]
    jin_bangun = count_jin(user)[2]
    jlh_pembuat = list_candi(user, candi)[0]
    candi_list = list_candi(user, candi)[1]
    if jlh_pembuat == 0:
        jin_termalas = '-'
        jin_terajin = '-'
    else:
        count = 1
        jumlah = candi_list[0][1]
        for j in range (1,jlh_pembuat):
            if jumlah < candi_list[j][1]:
                jumlah = candi_list[j][1]
                count = 1
            elif jumlah == candi_list[j][1]:
                count += 1
        list_rajin = [0 for i in range(count)]
        index = 0
        for i in range(jlh_pembuat):
            if candi_list[i][1] == jumlah:
                list_rajin[index] = candi_list[i][0]
                index += 1
        urut_abjad(list_rajin, count)
        jin_terajin = list_rajin[0]
        if count == jlh_pembuat:
            jin_termalas = list_rajin[count-1]
        else:
            count = 1
            jumlah_malas = candi_list[0][1]
            for j in range (1,jlh_pembuat):
                if jumlah_malas > candi_list[j][1]:
                    jumlah_malas = candi_list[j][1]
                    count = 1
                elif jumlah_malas == candi_list[j][1]:
                    count += 1
            list_malas = [0 for i in range(count)]
            index = 0
            for j in range(jlh_pembuat):
                if candi_list[j][1] == jumlah_malas:
                    list_malas[index] = candi_list[j][0]
                    index += 1
            urut_abjad(list_malas, count)
            jin_termalas = list_malas[count-1]
    print(f"\n> Total Jin: {total_jin}")
    print(f"> Total Jin Pengumpul: {jin_kumpul}")
    print(f"> Total Jin Pembangun: {jin_bangun}")
    print(f"> Jin Terajin: {jin_terajin}")
    print(f"> Jin Termalas: {jin_termalas}")
    print(f"> Jumlah Pasir: {bahan.detail[1][2]} unit")
    print(f"> Jumlah Batu: {bahan.detail[2][2]} unit")
    print(f"> Jumlah Air: {bahan.detail[3][2]} unit\n")


# F10 - Ambil Laporan Candi
def laporancandi(candi:Type[candi])->None:
# procedure laporancandi(input candi : candi)
# Melakukan prosedur F10 

# KAMUS LOKAL
# total_candi, idx, i, j : int
# total_bahan : array of int
# candi_detail : array of [string, int] {menyimpan data pembuat dan harga candi}
# cond : [int, string, int, int, int]
# id_mahal, id_murah : string
# ALGORITMA
    total_candi = candi.Neff-1
    total_bahan = [0,0,0]
    candi_detail = [[0,0] for i in range (total_candi)]
    for i in range(1,candi.Neff):
        for j in range (3):
            total_bahan[j] += candi.detail[i][j+2]
        cond = candi.detail[i]
        candi_detail[i-1] = [cond[0],(cond[2]*10000+cond[3]*15000+cond[4]*7500)]
    if total_candi == 0:
        id_mahal = "-"
        id_murah = "-"
    else:
        for i in range (1,total_candi):
            min = candi_detail[i][1]
            idx = i-1
            while idx >= 0 and min < candi_detail[idx][1]:
                candi_detail[idx+1],candi_detail[idx] = candi_detail[idx],candi_detail[idx+1]
                idx -= 1
        if total_candi == 1:
            id_mahal = str(candi_detail[0][0])+" ("+ribuan_parse(candi_detail[0][1])+")"
            id_murah = str(candi_detail[0][0])+" ("+ribuan_parse(candi_detail[0][1])+")"
        else:
            id_mahal = str(candi_detail[total_candi-1][0])+" ("+ribuan_parse(candi_detail[total_candi-1][1])+")"
            id_murah = str(candi_detail[0][0])+" ("+ribuan_parse(candi_detail[0][1])+")"
    print(f"\n> Total Candi: {total_candi}")
    print(f"> Total Pasir yang digunakan: {total_bahan[0]}")
    print(f"> Total Batu yang digunakan: {total_bahan[1]}")
    print(f"> Total Air yang digunakan: {total_bahan[2]}")
    print(f"> ID Candi Termahal: {id_mahal}")
    print(f"> ID Candi Termurah: {id_murah}\n")    

# F04 - Hilangkan Jin
def hapusjin(user:Type[user],candi:Type[candi],stack:Type[stack])->None:
# procedure hapusjin(input/output user : user, input/output candi : candi, input/output stack : stack)
# Melakukan prosedur hapusjin //Akses: Bandung Bondowoso 

# KAMUS LOKAL
# username : string
# ubah : char
# cond : arraf of string
# tabcandi : tabCandi
# ALGORITMA
    from undo import update_stack, tabCandi
    username = input("Masukkan username jin : ")
    cond = search_log(username, user)
    if cond == False:
        print("\nTidak ada jin dengan username tersebut.\n")
    else:
        if cond[2] != "jin_pengumpul" and cond[2] != "jin_pembangun":
            print("\nTidak ada jin dengan username tersebut.\n")
        else:
            hapus = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
            while hapus != "Y" and hapus != "N" and hapus != "y" and hapus != "n":
                print("\nInput anda salah silahkan input ulang.")
                hapus = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
            if hapus == "Y" or hapus == "y":
                print("\nJin telah dihapus dari alam gaib.\n")
                remove_jin(username, user)
                tabcandi = tabCandi(0)
                remove_candi(username, candi, tabcandi)
                update_stack(stack, cond, tabcandi)
            else:
                print("\nJin batal dihapus dari alam gaib.\n")

# F05 - Ubah Tipe Jin
def ubahjin(user:Type[user])->None:
# procedure ubahjin(input/ouput user : user)
# melakukan prosedur ubahjin

# KAMUS LOKAL
# username, tipe_jin, ubah_ke : string
# ubah : char
# idx : int
# cond : array of string
# ALGORITMA
    username = input("Masukkan username jin : ")
    cond = search_log(username, user)
    if cond == False:
        print("\nTidak ada jin dengan username tersebut.\n")
    else:
        if cond[2] != "jin_pengumpul" and cond[2] != "jin_pembangun":
            print("\nTidak ada jin dengan username tersebut.\n")
        else:
            tipe_jin = "Pengumpul" if cond[2] == "jin_pengumpul" else "Pembangun"
            ubah_ke = "Pengumpul" if cond[2] != "jin_pengumpul" else "Pembangun"
            ubah = input(f"Jin ini bertipe \"{tipe_jin}\". Yakin ingin mengubah ke tipe \"{ubah_ke}\" (Y/N)? ")
            while ubah != "Y" and ubah != "N" and ubah != "n" and ubah != 'y':
                ubah = input(f"Jin ini bertipe \"{tipe_jin}\". Yakin ingin mengubah ke tipe \"{ubah_ke}\" (Y/N)? ")
            if ubah == "Y" or ubah == "y":
                print("\nJin telah berhasil diubah.\n")
                idx = search_position(username, user)
                user.detail[idx][2] = "jin_pengumpul" if ubah_ke != "Pembangun" else "jin_pembangun"
            else:
                print("\nJin batal diubah.\n")

# F03 - Summon Jin
def summonjin(user:Type[user])->None:
# procedure summonjin(input/output user : user)
# menjalankan prosedur summon jin

# KAMUS LOKAL
# jenis : char
# tipe_jin, username, password : string
# ALGORITMA
    if user.Neff < 103:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi\n")
        jenis = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        while jenis != "1" and jenis != "2":
            print(f"\nTidak ada jenis jin \"{jenis}\"!\n")
            jenis = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        if jenis == "1":
            print("\nMemilih jin \"Pengumpul\".\n")
            tipe_jin = "jin_pengumpul"
        else:
            print("\nMemilih jin \"Pembangun\".\n")
            tipe_jin = "jin_pembangun"
        username = input("Masukkan username jin: ")
        while search_log(username, user) != False or not(isRequired(username)):
            if search_log(username, user) != False:
                print(f"\nUsername \"{username}\" sudah diambil!\n")
            else:
                print("\nUsername mengandung karakter yang tidak didukung. Silahkan input username lain!\n")
            username = input("Masukkan username jin: ")
        password = input("Masukkan password jin: ")
        while len(password)<5 or len(password)>25 or not(isRequired(password)):
            if len(password)<5 or len(password)>25:
                print(f"\nPassword panjangnya harus 5-25 karakter!\n")
            else:
                print("\nPassword mengandung karakter yang tidak didukung. Silahkan input password lain!\n")
            password = input("Masukkan password jin: ")
        print("\nMengumpulkan sesajen...")
        sleep(1)
        print("Menyerahkan sesajen...")
        sleep(1)
        print("Membaca mantra...")
        sleep(1)
        print(f"\nJin {username} berhasil dipanggil!\n")
        add_jin([username,password,tipe_jin], user)
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu\n")

# F06 - Jin Pembangun
def bangun(username:str,candi:Type[candi],bahan:Type[bahan],numbers:Type[number_colc])->None:
# procedure bangun(input username : string, input/output candi : candi, input/output bahan : bahan, input/output numbers : number_colc)
# melakukan prosedur jin pembangun

# KAMUS LOKAL
# pasir, batu, air, i : int
# racikan : array of int
# bisa_dibangun : bool
# ALGORITMA
    pasir = acak_bangun(numbers)
    batu = acak_bangun(numbers)
    air = acak_bangun(numbers)
    racikan = [pasir,batu,air]
    bisa_dibangun = True
    for i in range (3):
        if bahan.detail[i+1][2] < racikan[i]:
            bisa_dibangun = False
            break
    if bisa_dibangun:
        add_candi(username, racikan, candi)
        racikan = [-pasir,-batu,-air]
        update_bahan(racikan, bahan)
        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {101-candi.Neff}.\n")
    else:
        print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!\n")

# F07 - Jin Pengumpul
def kumpul(bahan:Type[bahan],numbers:Type[number_colc])->None:
# procedure kumpul(input/output bahan : bahan, input/output numbers : number_colc)
# melakukan prosedur jin pengumpul

# KAMUS LOKAL
# pasir, batu, air : int
# racikan : array of int
# ALGORITMA
    pasir = acak_kumpul(numbers)
    batu = acak_kumpul(numbers)
    air = acak_kumpul(numbers)
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.\n")
    racikan = [pasir,batu,air]
    update_bahan(racikan, bahan)

# F11 - Hancurkan Candi
def hancurkancandi(candi:Type[candi])->None:
# procedure hancurkancandi(input/output candi : candi)
# melakukan prosedur hancurkan candi

# KAMUS LOKAL
# id, pos : int
# permit : char
# ALGORITMA
    id = int(input("Masukkan ID candi: "))
    pos = search_position(id, candi)
    if pos == 0:
        print("\nTidak ada candi dengan ID tersebut.\n")
    else:
        permit = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
        while permit != 'y' and permit != 'Y' and permit != 'n' and permit != 'N':
            permit = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
        if permit == 'y' or permit == 'Y':
            print("\nCandi telah berhasil dihancurkan.\n")
            delete_candi(id, candi)
        else:
            print("\nCandi batal dihancurkan.\n")

# F12 - Ayam Berkokok
def ayamberkokok(candi:Type[candi])->None:
# procedure ayamberkokok(input candi : candi)
# melakukan prosedur Ayam Berkokok

# KAMUS LOKAL
# jumlah_candi : int
# ALGORITMA
    print("Kukuruyuk.. Kukuruyuk..\n")
    sleep(1)
    jumlah_candi = candi.Neff-1
    print(f"Jumlah Candi: {jumlah_candi}\n")
    sleep(1)
    if jumlah_candi == 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!\n")
    else:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.\n")
    exit()

# F15 - Help
def help()->None:
# procedure help()
# menampilkan command yang tersedia sebelum login
# KAMUS LOKAL
# ALGORITMA
    print("=========== HELP ===========")
    print("1. login\n   Untuk masuk menggunakan akun")
    print("2. save\n   Untuk menyimpan perubahan data selama permainan")
    print("3. exit\n   Untuk keluar dari program dan kembali ke terminal\n")

def help_bandung()->None:
# procedure help_bandung()
# menampilkan command yang tersedia saat login sebagai Bandung Bondowoso
# KAMUS LOKAL
# ALGORITMA
    print("=========== HELP ===========")
    print("1.  logout\n    Untuk keluar dari akun yang digunakan sekarang")
    print("2.  summonjin\n    Untuk memanggil jin")
    print("3.  hapusjin\n    Untuk menghapus jin sekaligus candi yang dibuatnya")
    print("4.  ubahjin\n    Untuk menukar tipe jin")
    print("5.  batchkumpul\n    Untuk mengerahkan semua Jin Pengumpul mengumpulkan bahan-bahan")
    print("6.  batchbangun\n    Untuk mengerahkan semua Jin Pembangun membangun candi")
    print("7.  laporanjin\n    Untuk melihat semua data pekerjaan dari semua jin")
    print("8.  laporancandi\n    Untuk melihat semua data candi")
    print("9.  undo\n    Untuk mengembalikan jin dan candinya setelah dia dihapus")
    print("10. save\n    Untuk menyimpan perubahan data selama permainan")
    print("11. exit\n    Untuk keluar dari program dan kembali ke terminal\n")

def help_roro()->None:
# procedure help_roro()
# menampilkan command yang tersedia saat login sebagai Roro Jonggrang
# KAMUS LOKAL
# ALGORITMA
    print("=========== HELP ===========")
    print("1. logout\n   Untuk keluar dari akun yang digunakan sekarang")
    print("2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia")
    print("3. ayamberkokok\n   Untuk menentukan pemenang permainan dan keluar dari program")
    print("4. save\n   Untuk menyimpan perubahan data selama permainan")
    print("5. exit\n   Untuk keluar dari program dan kembali ke terminal\n")

def help_jinbangun()->None:
# procedure help_jinbangun()
# menampilkan command yang tersedia saat login sebagai Jin Pembangun
# KAMUS LOKAL
# ALGORITMA
    print("=========== HELP ===========")
    print("1. logout\n   Untuk keluar dari akun yang digunakan sekarang")
    print("2. bangun\n   Untuk membangun candi")
    print("3. save\n   Untuk menyimpan perubahan data selama permainan")
    print("4. exit\n   Untuk keluar dari program dan kembali ke terminal\n")

def help_jinkumpul()->None:
# procedure help_jinkumpul()
# menampilkan command yang tersedia saat login sebagai Jin Pengumpul
# KAMUS LOKAL
# ALGORITMA
    print("=========== HELP ===========")
    print("1. logout\n   Untuk keluar dari akun yang digunakan sekarang")
    print("2. kumpul\n   Untuk mengumpulkan bahan-bahan")
    print("3. save\n   Untuk menyimpan perubahan data selama permainan")
    print("4. exit\n   Untuk keluar dari program dan kembali ke terminal\n")

# LOGIN HARUS DIBUAT PALING AKHIR, LANJUTKAN CODE DI ATAS BAGIAN INI
# F01 - Login
def login(user:Type[user],candi:Type[candi],bahan:Type[bahan],numbers:Type[number_colc],role:str,stack:Type[stack])->None:
# procedure login(input/output user : user, input/output candi : candi, input/output bahan : bahan, input/output numbers : number_colc, input role : string, input/output stack : stack)
# melakukan prosedur login

# KAMUS LOKAL
# username, password, pilihan : string
# simpan : char
# cond : array of string
# ALGORITMA
    username = input("Username: ")
    password = input("Password: ")
    cond = search_log(username, user)
    if cond != False:
        if password == cond[1]:
            print(f"\nSelamat datang, {cond[0]}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
            role = cond[2]
            while True:
                pilihan = input(">>> ")
                if pilihan == "save":
                    save(user, candi, bahan, stack)
                elif pilihan == "logout":
                    break
                elif pilihan == "help":
                    if role == "bandung_bondowoso":
                        help_bandung()
                    elif role == "roro_jonggrang":
                        help_roro()
                    elif role == "jin_pengumpul":
                        help_jinkumpul()
                    else:
                        help_jinbangun()
                elif pilihan == "exit":
                    simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
                    while simpan != "y" and simpan != "Y" and simpan != "n" and simpan != "N":
                        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
                    if simpan == "y" or simpan == "Y":
                        save(user, candi, bahan, stack)
                    exit()
                elif pilihan == "login":
                    print("Login gagal!")
                    print(f"Anda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.\n")
                elif pilihan == "summonjin":
                    if role == "bandung_bondowoso":
                        summonjin(user)
                    else:
                        print("Summon Jin hanya dapat diakses oleh akun Bandung Bodowoso.\n")
                elif pilihan == "hapusjin":
                    if role == "bandung_bondowoso":
                        hapusjin(user, candi, stack)
                    else:
                        print("Hapus Jin hanya dapat diakses oleh akun Bandung Bondowoso.\n")
                elif pilihan == "ubahjin":
                    if role == "bandung_bondowoso":
                        ubahjin(user)
                    else:
                        print("Ubah Jin hanya dapat diakses oleh akun Bandung Bondowoso.\n")
                elif pilihan == "bangun":
                    if role == "jin_pembangun":
                        bangun(username, candi, bahan, numbers)
                    else:
                        print("Bangun hanya dapat diakses oleh akun Jin Pembangun.\n")
                elif pilihan == "kumpul":
                    if role == "jin_pengumpul":
                        kumpul(bahan, numbers)
                    else:
                        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.\n")
                elif pilihan == "batchkumpul":
                    if role == "bandung_bondowoso":
                        batch_kumpul(user, bahan, numbers)
                    else:
                        print("Batch Kumpul hanya dapat diakses oleh akun Bandung Bondowoso.\n")
                elif pilihan == "batchbangun":
                    if role == "bandung_bondowoso":
                        batch_bangun(user, candi, bahan, numbers)
                    else:
                        print("Batch Bangun hanya dapat diakses oleh akun Bandung Bondowoso.\n")
                elif pilihan == "laporanjin":
                    if role == "bandung_bondowoso":
                        laporanjin(user, candi, bahan)
                    else:
                        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.\n")
                elif pilihan == "laporancandi":
                    if role == "bandung_bondowoso":
                        laporancandi(candi)
                    else:
                        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.\n")
                elif pilihan == "undo":
                    if role == "bandung_bondowoso":
                        undo(stack, user, candi)
                    else:
                        print("Undo hanya dapat diakses oleh akun Bandung Bondowoso.\n")
                elif pilihan == "hancurkancandi":
                    if role == "roro_jonggrang":
                        hancurkancandi(candi)
                    else:
                        print("Hancurkan Candi hanya dapat diakses oleh akun Roro Jonggrang.\n")
                elif pilihan == "ayamberkokok":
                    if role == "roro_jonggrang":
                        ayamberkokok(candi)
                    else:
                        print("Ayam Berkokok hanya dapat diakses oleh akun Roro Jonggrang.\n")
                else:
                    print("Command tidak tersedia. Silahkan input command \"help\" untuk mengecek akses anda.\n")   
            role = None
        else:
            print("\nPassword salah!\n")
    else:
        print("\nUsername tidak terdaftar!\n")