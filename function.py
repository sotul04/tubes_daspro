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
