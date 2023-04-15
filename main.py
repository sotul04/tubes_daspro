from commands import *
from data_manipulate import *
from function import *
from data_type import *

folder = [0]
# [F13] melakukan load {memanggil file eksternal}
load(folder)
folder = folder[0]
u_path = folder+"/user.csv"
c_path = folder+"/candi.csv"
b_path = folder+"/bahan_bangunan.csv"
# memuat semua data dari file eksternal dan disimpan untuk dilakukan permainan game
user_data = user(read_user(u_path)[0],read_user(u_path)[1])
candi_data = candi(read_candi(c_path)[0],read_candi(c_path)[1])
bahan_data = bahan(read_bahan(b_path)[0],read_bahan(b_path)[1])
# memuat numbers {variabel yang menyimpan angka random selama permainan}
if candi_data.Neff > 1:
    numbers = number_colc(1, [candi_data.detail[candi_data.Neff-1][4]])
else:
    numbers = number_colc(1, [user_data.Neff])

role = None
while True:
    command = input(">>> ")
    if command == "login":
        login(user_data, candi_data, bahan_data, numbers, role)
    elif command == "save":
        save(user_data, candi_data, bahan_data)
    elif command == "exit":
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        while simpan != "y" and simpan != "Y" and simpan != "n" and simpan != "N":
            simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if simpan == "y" or simpan == "Y":
            save(user_data, candi_data, bahan_data)
        exit()
    elif command == "logout":
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.\n")
    else:
        print("Anda tidak bisa melakukan command tersebut karena Anda belum login atau akun Anda tidak memiliki akses.")