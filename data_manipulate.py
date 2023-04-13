import os
def split(s,char):
# mengubah data yang dibaca dari file .csv kemudian mengembalikan sebuah array
# yang berisi string dari pemisahan yang ditandai dengan semicolon (;)
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

def read_user(path):
# function list_csv (path : string {alamat file .csv}) -> array of array of string
# mengembalikan sebuah array of array of string dari pemisahan yang ditandai semicolon (;)
# pada setiap line pada file .csv yang dibaca
    temp = [0 for i in range(200)]
    with open(path, "r") as file:
        index = 0
        for line in file:
            temp[index] = split(line,";")
            index += 1
    return index,temp

def read_candi(path):
# function list_csv (path : string {alamat file .csv}) -> array of array of string
# mengembalikan sebuah array of array of string dari pemisahan yang ditandai semicolon (;)
# pada setiap line pada file .csv yang dibaca
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

def read_bahan(path):
# function list_csv (path : string {alamat file .csv}) -> array of array of string
# mengembalikan sebuah array of array of string dari pemisahan yang ditandai semicolon (;)
# pada setiap line pada file .csv yang dibaca
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


def save_csv(tipe, path):
#prosedur untuk menyimpan data pada file eksternal saat dipanggil
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

def add_jin(data_jin, tipe):
# fungsi yang akan menambah data tambahan pada variabel yang menyimpan data
# saat program berjalan
    for i in range(1,201):
        if tipe.detail[i] == 0:
            tipe.detail[i] = data_jin
            break
    tipe.Neff += 1
    return tipe

def remove_jin(username, tipe):
# fungsi yang akan menghapus data jin yang dicari dari data user
    temp = tipe.Neff
    for i in range (1,tipe.Neff):
        if username == tipe.detail[i][0]:
            temp = i
    for i in range (temp,tipe.Neff+1):
        tipe.detail[i] = tipe.detail[i+1]
    if temp != tipe.Neff:
        tipe.Neff -= 1

def remove_candi(username, tipe):
# fungsi yang akan menghapus semua candi yang dibangun jin yang 
# pembuatnya bernama username yang diinput
    count = 0
    for i in range(1,tipe.Neff):
        if username == tipe.detail[i][1]:
            count += 1
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

def add_candi(username, racikan, tipe):
# add_candi akan menambah data candi dengan nomor id terkecil yang bisa disisipi
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

def delete_candi(id_candi, tipe):
# delete_candi akan menghapus data candi dengan id = id_candi dari variabel global yang berisi data candi
    index = tipe.Neff
    for i in range (1,tipe.Neff):
        if id_candi == tipe.detail[i][0]:
            index = i
            break
    if index < tipe.Neff:
        for i in range (index,tipe.Neff):
            tipe.detail[i] = tipe.detail[i+1]
        tipe.Neff -= 1
            
def update_bahan(list, tipe):
# meng-update bahan saat dipanggil sesuai isi dari list
    for i in range (1,tipe.Neff):
        tipe.detail[i][2] += list[i-1]
    return tipe