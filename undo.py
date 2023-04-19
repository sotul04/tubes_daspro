from typing import Type, List
from function import search_log
from data_type import user, candi

""" ====================================== UNDO PACK ============================================ """

class tabCandi:
# tipe bentukan
# type tabCandi : < Neff : integer;
#                   detail : array of array {data candi, yaitu id, pembuat, pasir, batu, dan air} >
    def __init__(self,Neff:int,detail:List[list] = []):
        self.Neff = Neff
        self.detail = detail

class stack:
# tipe bentukan
# type stack : < pos : integer; {nilai indeks terbesar data efektif}
#                users : array of array of string; {menyimpan data user yang disimpan ke stack untuk prosedur undo}
#                candi : array of tabCandi {data beberapa candi} >
    def __init__(self,pos:int,users:List[List[str]] = [],candi:Type[List[tabCandi]] = []):
        self.pos = pos
        self.users = users
        self.candi = candi

def update_stack(stack:Type[stack],user_dat:List[str],tabcandi:Type[tabCandi])->None:
# procedure update_stack(input/output stack : stack, input user_dat : array of string, input tabcandi : tabCandi)
# fungsi ini menambah data pada stack setiap kali ada jin pembangun yang dihapus

# KAMUS LOKAL
# i : int
# temp_u : array of string
# temp_c : array of tabCandi
# ALGORITMA
    stack.pos += 1
    temp_u = [0 for i in range(stack.pos)]
    temp_c = [0 for i in range(stack.pos)]
    for i in range (stack.pos-1):
        temp_u[i] = stack.users[i]
        temp_c[i] = stack.candi[i]
    temp_u[stack.pos-1] = user_dat
    temp_c[stack.pos-1] = tabcandi
    stack.users = temp_u
    stack.candi = temp_c

def undo(stack:Type[stack],user:Type[user],candi:Type[candi])->None:
# procedure undo(input/output stack : stack, input/output user : user, input/output candi : candi)
# mengembalikan data candi dan jin pembangun yang sebelumnya telah dihapus

# KAMUS LOKAL
# user_data = array of string
# i : int
# dcandi : array of string
# temp_u : array of array of string
# temp_c : array of array of [int, string, int, int, int]
# ALGORITMA
    from data_manipulate import add_jin,add_candi
    if stack.pos == 0:
        print("Tidak ada jin dan candi yang bisa dikembalikan.\n")
    else:
        stack.pos -= 1
        user_data = stack.users[stack.pos]
        if search_log(user_data[0], user) == False:
            add_jin(user_data, user)
        for i in range (stack.candi[stack.pos].Neff):
            dcandi = stack.candi[stack.pos].detail[i]
            add_candi(dcandi[1], [dcandi[2],dcandi[3],dcandi[4]], candi)
        # menghapus data terakhir setiap data
        temp_u = [stack.users[i] for i in range(stack.pos)]
        temp_c = [stack.candi[i] for i in range(stack.pos)]
        stack.users,stack.candi = temp_u,temp_c
        print(f"Jin \"{user_data[0]}\" dan candi yang dia bangun berhasil dikembalikan.\n")