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
    c = 12347
    m = 2**30
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
    acakkumpul(tipe,1)
    result = tipe.array[tipe.Neff-1]%6
    return result

def list_jin(role,user):
# mengembalikan list yang berisi username jini bertipe role
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

def count_jin(user):
# menghitung total jin, jumlah jin pengumpul, dan jin pembangun
    total_jin = user.Neff-3
    jin_kumpul = 0
    for i in range (3,user.Neff):
        if user.detail[i][2] == "jin_pengumpul":
            jin_kumpul += 1
    jin_bangun = total_jin - jin_kumpul
    return total_jin,jin_kumpul,jin_bangun

def list_candi(user,candi):
# mengembalikan jumlah permbuat candi pada data candi dan list yang berisi nama pembuat dan jumlah candinya
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

def urut_abjad(list,count):
# mengurutkan list berisi string secara menaik dengan 
    for i in range(1,count):
        min = list[i]
        idx = i-1
        while idx >= 0 and min < list[idx]:
            list[idx+1],list[idx] = list[idx],list[idx+1]
            idx -= 1