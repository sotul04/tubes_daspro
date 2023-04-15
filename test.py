from data_manipulate import *
from function import *
from commands import *
from data_type import *

path = "data_eksternal/user.csv"
user_data = user(read_user(path)[0],read_user(path)[1])
#a = list_jin("jin_pengumpul", user_data)
#print(a)

numbers = number_colc(1, [1])
bahan_data = bahan(read_bahan("data_eksternal/bahan_bangunan.csv")[0],read_bahan("data_eksternal/bahan_bangunan.csv")[1])
candi_data = bahan(read_candi("data_eksternal/candi.csv")[0],read_candi("data_eksternal/candi.csv")[1])
#print(candi_data.detail[1:candi_data.Neff])
#print(bahan_data.detail[1:4])
#batch_kumpul(user_data, bahan_data, numbers)
#print("\n",bahan_data.detail[1:4], "\n")
#batch_bangun(user_data, candi_data, bahan_data, numbers)
#print(bahan_data.detail[1:4])
#print(candi_data.detail[1:candi_data.Neff])
#a = list_candi(user_data, candi_data)
#print(count_jin(user_data))
#print(a)
laporanjin(user_data, candi_data, bahan_data)