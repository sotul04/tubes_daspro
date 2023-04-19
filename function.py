from data_type import *
from typing import Type,Tuple,Any

def search_log(input:str,user:Type[user])->Any:
# function searh_log(input : string, user : user) -> bool {if username (input) does not exist}
# function searh_log(input : string, user : user) -> list {if username exists}
# return seluruh data pada array yang memuat username yang dicari

# KAMUS LOKAL
# found : bool
# found : array of string
# ALGORITMA
    found = False
    for i in range(1,user.Neff):
        if input == user.detail[i][0]:
            found = user.detail[i]
            break
    return found

def search_position(input:str,user:Type[user])->int:
# function search_position(input : string, user : user) -> int
# return integer -> posisi dari username yang dicari pada detail data user
# return 0 jika tidak ditemukan

# KAMUS LOKAL
# found : int
# ALGORITMA
    found = 0
    for i in range(1,user.Neff):
        if input == user.detail[i][0]:
            found = i
            break
    return found

def path_counter(path:str)->int:
# function path_counter(path : string) -> int
# fungsi yang digunakan untuk menghitung jumlah folder di dalam sebuah alamat path

# KAMUS LOKAL
# count : int
# ALGORITMA
    count = 1
    for i in range(len(path)):
        if path[i] == "/" and i != len(path)-1:
            count += 1
    return count

def acakbangun(number:Type[number_colc],neff:int)->None:
# procedure acakbangun(input/output number : number_colc, input neff : int)
# prosedur ini akan mengubah data ANGKA ACAK saat dipanggil

# KAMUS LOKAL
# a, c, m, i : int
# temp : array of int
# ALGORITMA
    a = 11103515245
    c = 12345
    m = 2**31
    temp = [0 for i in range(number.Neff+neff)]
    for i in range(number.Neff):
        temp[i] = number.array[i]
    for i in range(number.Neff,number.Neff+neff):
        temp[i] = (temp[i-1]*a+c)%m
    number.array = temp
    number.Neff += neff

def acakkumpul(number:Type[number_colc],neff:int)->None:
# procedure acakkumpul(input/output number : nnumber_colc, input neff : int)
# prosedur ini akan mengubah data ANGKA ACAK saat dipanggil

# KAMUS LOKAL
# a, c, m, i : int
# temp : array of int
# ALGORITMA
    a = 11103515245
    c = 12347
    m = 2**30
    temp = [0 for i in range(number.Neff+neff)]
    for i in range(number.Neff):
        temp[i] = number.array[i]
    for i in range(number.Neff,number.Neff+neff):
        temp[i] = (temp[i-1]*a+c)%m
    number.array = temp
    number.Neff += neff

def acak_bangun(number:Type[number_colc])->int:
# function acak_bangun(number : number_colc) -> int
# mengembalikan sebuah integer yang digunakan pada spesifikasi F06 dan F08

# KAMUS LOKAL
# result : int
# ALGORITMA
    acakbangun(number,1)
    result = number.array[number.Neff-1]%5
    if result == 0:
        result = 5
    return result

def acak_kumpul(number:Type[number_colc])->int:
# function acak_kumpul(number : number_colc) -> int
# mengembalikan sebuah integer yang digunakan pada spesifikasi F07 dan F08

# KAMUS LOKAL
# result : int
# ALGORITMA
    acakkumpul(number,1)
    result = number.array[number.Neff-1]%6
    return result

def list_jin(role:str,user:Type[user])->Tuple[int,list]:
# function list_jin(role : string, user : user) -> (int, list)
# mengembalikan list yang berisi username jin bertipe role

# KAMUS LOKAL
# count, i, index : int
# temp : array of string
# ALGORITMA
    count = 0
    for i in range (1,user.Neff):
        if user.detail[i][2] == role:
            count += 1
    temp = [0 for i in range(count)]
    index = 0
    for i in range (1,user.Neff):
        if user.detail[i][2] == role:
            temp[index] = user.detail[i][0]
            index += 1
    return count,temp

def count_jin(user:Type[user])->Tuple[int]:
# function count_jin(user : user) -> (int, int, int)
# menghitung total jin, jumlah jin pengumpul, dan jin pembangun

# KAMUS LOKAL
# total_jin, jin_kumpul, jin_bangun, i : int
# ALGORITMA
    total_jin = user.Neff-3
    jin_kumpul = 0
    for i in range (3,user.Neff):
        if user.detail[i][2] == "jin_pengumpul":
            jin_kumpul += 1
    jin_bangun = total_jin - jin_kumpul
    return total_jin,jin_kumpul,jin_bangun

def list_candi(user:Type[user],candi:Type[candi])->Tuple[int,List[list]]:
# function list_candi(user : user, candi : candi) -> (int, list)
# mengembalikan jumlah permbuat candi pada data candi dan list yang berisi nama pembuat dan jumlah candinya

# KAMUS LOKAL
# count, index, i, j : int
# found : bool
# temp, tent : array of [string, int]
# ALGORITMA
    count = count_jin(user)[2]
    temp = [[0,0] for i in range (count)]
    index = 0
    for i in range (3,user.Neff):
        if user.detail[i][2] == "jin_pembangun":
            temp[index][0] = user.detail[i][0]
            index += 1
    for i in range (1,candi.Neff):
        found = False
        for j in range(count):
            if candi.detail[i][1] == temp[j][0]:
                found = True
                temp[j][1] += 1
                break
        if not found:
            tent = [[0,0] for j in range (count +1)]
            count += 1
            for j in range(count-1):
                tent[j] = temp[j]
            temp = tent
            temp[count-1] = [candi.detail[i][1],1]
    return count,temp

def urut_abjad(list:List[str],count:int)->None:
# procedure urut_abjad(input/output list : array of string, input count : int)
# mengurutkan list berisi string secara menaik dengan 

# KAMUS LOKAL
# i, idx : int
# min : string
# ALGORITMA
    for i in range(1,count):
        min = list[i]
        idx = i-1
        while idx >= 0 and min < list[idx]:
            list[idx+1],list[idx] = list[idx],list[idx+1]
            idx -= 1

def ribuan_parse(nominal:int)->str:
# function ribuan_parse(nominal : int) -> string
# mengubah data integer menjadi string yang diformat ke dalam format Rupiah

# KAMUS LOKAL
# string, temp : string
# count, i : int
# ALGORITMA
    string = str(nominal)
    temp = ''
    count = 0
    for i in range(len(string)-1,-1,-1):
        count += 1
        temp = string[i] + temp
        if count == 3 and i != 0:
            temp = '.' + temp
            count = 0
    temp = 'Rp ' + temp
    return temp

def isRequired(string:str)->bool:
# function isRequired(string : string) -> bool
# fungsi untuk memvalidasi username dan password agar tidak konflik dengan tipe data

# KAMUS LOKAL
# char : string
# required, ada : bool
# ALGORITMA
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#_/\\?()[]{}"
    required = True
    for i in range(len(string)):
        ada = False
        for j in range(len(char)):
            if string[i] == char[j]:
                ada = True
                break
        if ada == False:
            required = False
            break
    return required