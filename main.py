from spesification import *
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
    numbers = number_colc(1, candi_data.detail[candi_data.Neff-1][4])
else:
    numbers = number_colc(1, user_data.Neff)

#print(user_data.detail[:user_data.Neff])
#print(candi_data.detail[:candi_data.Neff])
#print(bahan_data.detail[:bahan_data.Neff])

#save(user_data, candi_data, bahan_data)
#while True:
#    islogin = False
#    command = input()
#    pass