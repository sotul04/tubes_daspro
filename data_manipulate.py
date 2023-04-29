from typing import Type,List,Tuple,Any
from data_type import *
from undo import tabCandi

def split(s:str,char:str)->list:
# function split(s : string, char : char) -> array of string
# mengubah data yang dibaca dari file .csv kemudian mengembalikan sebuah array
# yang berisi string dari pemisahan yang ditandai dengan char

# KAMUS LOKAL
# sumofComma, index, i, j : int
# list_value : array of string
# temp : string
# ALGORITMA
    sumofComma = 0
    for i in range (len(s)):
        if s[i] == char:
            sumofComma += 1
    list_value = [0 for i in range (sumofComma+1)]
    index = 0
    temp = ''
    for j in range (len(s)):
        if s[j] == char or j == len(s)-1:
            if j == len(s)-1:
                if s[j] != "\n":
                    temp += s[j]
            list_value[index] = temp
            temp = ''
            index += 1
        else:
            temp += s[j]
    return list_value

def read_user(path:str)->Tuple[int,list]:
# function list_csv (path : string {alamat file .csv}) -> (int, list)
# mengembalikan sebuah array of array of string dari pemisahan yang ditandai semicolon (;)
# pada setiap line pada file .csv yang dibaca

# KAMUS LOKAL
# temp : array[1..200] of array of string
# index, i : int
# line : string
# ALGORITMA
    temp = [0 for i in range(200)]
    with open(path, "r") as file:
        index = 0
        for line in file:
            temp[index] = split(line,";")
            index += 1
    return index,temp

def read_candi(path:str)->Tuple[int,list]:
# function list_csv (path : string {alamat file .csv}) -> (int, list)
# mengembalikan sebuah array of array of string dari pemisahan yang ditandai semicolon (;)
# pada setiap line pada file .csv yang dibaca

# KAMUS LOKAL
# temp : array of [int, string, int, int, int]
# index, i : int
# tent : array
# line : string
# ALGORITMA
    temp = [0 for i in range(200)]
    with open(path, "r") as file:
        index = 0
        for line in file:
            tent = split(line,";")
            for i in range (5):
                if i != 1 and index != 0:
                    tent[i] = int(tent[i])
            temp[index] = tent
            index += 1
    return index,temp

def read_bahan(path:str)->Tuple[int,list]:
# function list_csv (path : string {alamat file .csv}) -> (int, list)
# mengembalikan sebuah array of array of string dari pemisahan yang ditandai semicolon (;)
# pada setiap line pada file .csv yang dibaca

# KAMUS LOKAL
# temp : array of [string, string, int]
# index : int
# line : string
# tent : array
# ALGORITMA
    temp = [0 for i in range(4)]
    with open(path, "r") as file:
        index = 0
        for line in file:
            tent = split(line,";")
            if index != 0:
                tent[2] = int(tent[2])
            temp[index] = tent
            index += 1
    return index,temp


def save_csv(tipe:Any, path:str)->None:
# procedure save_csv(input tipe : (user, candi, bahan), input path : string)
# prosedur untuk menyimpan data pada file eksternal saat dipanggil
# digunakan untuk menyimpan data user, candi, dan bahan bangunan

# KAMUS LOKAL
# temp, tent : string
# i, j : int
# ALGORITMA
    temp = ''
    for i in range(tipe.Neff):
        tent = ''
        for j in range(tipe.length):
            tent += str(tipe.detail[i][j])
            if j != tipe.length-1:
                tent += ';'
            if j == tipe.length-1 and i != tipe.Neff-1:
                tent += "\n"
        temp += tent
    with open(path, "w", encoding="utf-8") as file:
        file.write(temp)

def add_jin(data_jin:list, tipe:Type[user])->None:
# procedure add_jin(input data_jin : array of string, input/output tipe : user)
# fungsi yang akan menambah data tambahan pada variabel yang menyimpan data
# saat program berjalan

# KAMUS LOKAL
# i : int
# ALGORITMA
    for i in range(1,201):
        if tipe.detail[i] == 0:
            tipe.detail[i] = data_jin
            break
    tipe.Neff += 1

def remove_jin(username:str, tipe:Type[user])->None:
# procedure remove_jin(input username : string, input/output tipe : user)
# prosedur yang akan menghapus data jin yang dicari dari data user

# KAMUS LOKAL
# temp, i : int
# ALGORITMA
    temp = tipe.Neff
    for i in range (1,tipe.Neff):
        if username == tipe.detail[i][0]:
            temp = i
    for i in range (temp,tipe.Neff+1):
        tipe.detail[i] = tipe.detail[i+1]
    if temp != tipe.Neff:
        tipe.Neff -= 1

def remove_candi(username:str, tipe:Type[candi], tabcandi:Type[tabCandi])->None:
# procedure remove_candi(input username : string, input/output tipe : candi, input/ouput tabcandi : tabCandi)
# prosedur yang akan menghapus semua candi yang dibangun jin yang 
# pembuatnya bernama username yang diinput

# KAMUS LOKAL
# count, j, i : int
# found : bool
# temp : array of [int, string, int, int, int]
# ALGORITMA
    count = 0
    for j in range(1,tipe.Neff):
        if username == tipe.detail[j][1]:
            count += 1
            tabcandi.Neff += 1
            temp = [0 for i in range(tabcandi.Neff)]
            for i in range (tabcandi.Neff-1):
                temp[i] = tabcandi.detail[i]
            temp[tabcandi.Neff-1] = tipe.detail[j]
            tabcandi.detail = temp
    for j in range(count):
        found = False
        for i in range (1,tipe.Neff+1):
            if i < tipe.Neff:
                if username == tipe.detail[i][1] or found:
                    found = True
                    tipe.detail[i] = tipe.detail[i+1]
            else:
                if found:
                    tipe.detail[i] = tipe.detail[i+1]
        tipe.Neff -= 1

def add_candi(username:str, racikan:list, tipe:Type[candi], count:List[int] = [0])->None:
# procedure add_candi(input username : string, input racikan : array of int, input/output tipe : candi, input/output count : array of integer)
# add_candi akan menambah data candi dengan nomor id terkecil yang bisa disisipi

# KAMUS LOKAL
# min, i, index, idx : int
# temp : array of [int, string, int, int, int]
# ALGORITMA
    if tipe.Neff < 101:
        count[0] += 1
        min = 0
        index = tipe.Neff
        for i in range(1,tipe.Neff):
            if min < tipe.detail[i][0]:
                index = i
                break
            else:
                min += 1
        temp = [tipe.detail[i] for i in range (index, tipe.Neff)]
        tipe.detail[index] = [min,username,racikan[0],racikan[1],racikan[2]]
        tipe.Neff += 1
        idx = 0
        for i in range(index+1,tipe.Neff):
            tipe.detail[i] = temp[idx]
            idx += 1

def delete_candi(id_candi:int, tipe:Type[candi])->None:
# procedure delete_candi(input id : int, input/output tipe : candi)
# delete_candi akan menghapus data candi dengan id = id_candi dari variabel global yang berisi data candi

# KAMUS LOKAL
# index, i : int
# ALGORITMA
    index = tipe.Neff
    for i in range (1,tipe.Neff):
        if id_candi == tipe.detail[i][0]:
            index = i
            break
    if index < tipe.Neff:
        for i in range (index,tipe.Neff):
            tipe.detail[i] = tipe.detail[i+1]
        tipe.Neff -= 1
            
def update_bahan(list:list, tipe:Type[bahan])->None:
# procedure update_bahan(input list : array of integer, input/output tipe : bahan)
# meng-update bahan saat dipanggil sesuai isi dari list

# KAMUS LOKAL
# i : int
# ALGORITMA
    for i in range (1,tipe.Neff):
        tipe.detail[i][2] += list[i-1]