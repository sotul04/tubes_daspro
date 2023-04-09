def split_csv(s):
# mengubah data yang dibaca dari file .csv kemudian mengembalikan sebuah array
# yang berisi string dari pemisahan yang ditandai dengan semicolon (;)
    sumofComma = 0
    for i in range (len(s)):
        if s[i] == ';':
            sumofComma += 1
    list_value = [0 for i in range (sumofComma+1)]
    index = 0
    temp = ''
    for j in range (len(s)):
        if s[j] == ';' or j == len(s)-1:
            if j == len(s)-1:
                if s[j] != "\n":
                    temp += s[j]
            list_value[index] = temp
            temp = ''
            index += 1
        else:
            temp += s[j]
    return list_value

def list_csv(m):
# mengubah data semicolon pada file .csv menjadi sebuah list yang
# berstruktur [Neff, [identitas kolom (baris 1)], [baris 2], [baris 3], ... dst]
    temp = [0 for i in range(1000)]
    with open(m, "r") as file:
        index = 1
        for line in file:
            temp[index] = split_csv(line)
            temp[0] = index
            index += 1
    return temp

def save_csv(list,file_name,len):
    temp = ''
    for i in range(1,list[0]+1):
        tent = ''
        for j in range(len):
            tent += list[i][j]
            if j != len-1:
                tent += ';'
            if j == len-1 and i != list[0]:
                tent += "\n"
        temp += tent
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(temp)
