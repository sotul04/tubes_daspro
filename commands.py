from argparse import *
from time import sleep
import os
from data_manipulate import *
from function import *

#F13
def load(folder):
# Menjalankan load saat program pertama kali dijalankan dan mengubah nilai input/output
# folder menjadi path data eksternal yang digunakan jika tersedia, jika tidak program keluar
    parser = ArgumentParser()
    parser.add_argument("nama_folder",nargs="?",type=str,default="")
    args = parser.parse_args()
    foldr = args.nama_folder
    if foldr == "":
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: "+"\x1B[3m" + "python main.py" + "\x1B[0m" + " <nama_folder>")
        exit()
    elif os.path.isdir(foldr):
        print("\nSelamat datang di program \"Manajerial Candi\"")
        folder[0] = foldr
    else:
        print(f"\nFolder \"{folder}\" tidak ditemukan.")
        exit()
#F14
def save(user,candi,bahan):
# Menjalankan prosedur save untuk menyimpan data perubahan selama permainan dijalankan
    path = input("Masukkan nama folder: ")
    folder = "save"
    folder +="/"+path
    print("\nSaving...\n")
    repet = path_counter(folder)
    test = split(folder,"/")
    fold_temp = ''
    for i in range(repet):
        if i > 0:
            fold_temp += "/"
        fold_temp += test[i]
        if not (os.path.isdir(fold_temp)):
            os.mkdir(fold_temp)
            print(f"Membuat folder {fold_temp}...")
            sleep(1)
        if i == repet-1:
            save_csv(user, fold_temp+"/user.csv")
            save_csv(candi, fold_temp+"/candi.csv")
            save_csv(bahan, fold_temp+"/bahan_bangunan.csv")
            print(f"\nBerhasil menyimpan data di folder {fold_temp}!\n")


#F08
def batch_kumpul(user,bahan,numbers):
# melakukan fitur F08 - batchkumpul
    data = list_jin("jin_pengumpul", user)
    racikan = [0,0,0]
    if data[0] == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print(f"Mengerahkan {data[0]} jin untuk mengumpulkan bahan.")
        for i in range (data[0]):
            pasir = acak_kumpul(numbers)
            batu = acak_kumpul(numbers)
            air = acak_kumpul(numbers)
            racikan[0] += pasir
            racikan[1] += batu
            racikan[2] += air
        print(f"Jin menemukan total {racikan[0]} pasir, {racikan[1]} batu, {racikan[2]} air.")
        update_bahan(racikan, bahan)

def batch_bangun(user,candi,bahan,numbers):
# melakukan fitur F08 - batchbangun
    data = list_jin("jin_pembangun", user)
    bahan_total = [0,0,0]
    if data[0] == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
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
            print(f"Jin berhasil membangun total {data[0]} candi.")
        else:
            kurang = [0,0,0]
            for i in range (3):
                kurang[i] = bahan_total[i]-bahan.detail[i+1][2]
                if kurang[i] < 0:
                    kurang[i] = 0
            print(f"Bangun gagal. Kurang {kurang[0]} pasir, {kurang[1]} batu, {kurang[2]} air.")
            




