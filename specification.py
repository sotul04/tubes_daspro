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


    
