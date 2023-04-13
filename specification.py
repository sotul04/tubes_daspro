from argparse import *
from time import sleep
import os
from data_manipulate import *

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

