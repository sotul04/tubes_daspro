def search_log(input,tipe):
# return seluruh data pada array yang memuat username yang dicari
    found = False
    for i in range(1,tipe.Neff+1):
        if input == tipe.detail[i][0]:
            found = tipe.detail[i]
            break
    return found

def search_position(input,tipe):
# return integer -> posisi dari username yang dicari pada detail data user
    found = 0
    for i in range(1,tipe.Neff+1):
        if input == tipe.detail[i][0]:
            found = i
            break
    return found

def search_role(input,tipe):
# return string -> role dari username yang dicari
    found = False
    for i in range(1,tipe.Neff+1):
        if input == tipe.detail[i][0]:
            found = tipe.detail[i][2]
            break
    return found

def path_counter(path):
# fungsi yang digunakan untuk menghitung jumlah folder di dalam sebuah alamat path
    count = 1
    for i in range(len(path)):
        if path[i] == "/" and i != len(path)-1:
            count += 1
    return count

def acakbangun(tipe,neff):
# fungsi ini akan mengubah data ANGKA ACAK saat dipanggil
    a = 11103515245
    c = 12345
    m = 2**31
    temp = [0 for i in range(tipe.Neff+neff)]
    for i in range(tipe.Neff):
        temp[i] = tipe.array[i]
    for i in range(tipe.Neff,tipe.Neff+neff):
        temp[i] = (temp[i-1]*a+c)%m
    tipe.array = temp
    tipe.Neff += neff

def acakkumpul(tipe,neff):
# fungsi ini akan mengubah data ANGKA ACAK saat dipanggil
    a = 11103515245
    c = 12342
    m = 2**31
    temp = [0 for i in range(tipe.Neff+neff)]
    for i in range(tipe.Neff):
        temp[i] = tipe.array[i]
    for i in range(tipe.Neff,tipe.Neff+neff):
        temp[i] = (temp[i-1]*a+c)%m
    tipe.array = temp
    tipe.Neff += neff

def acak_bangun(tipe):
# mengembalikan sebuah integer yang digunakan pada spesifikasi F06 dan F08
    acakbangun(tipe,1)
    result = tipe.array[tipe.Neff-1]%5
    if result == 0:
        result = 5
    return result
def acak_kumpul(tipe):
# mengembalikan sebuah integer yang digunakan pada spesifikasi F07 dan F08
    acakbangun(tipe,1)
    acakkumpul(tipe,1)
    result = tipe.array[tipe.Neff-1]%6
    return result