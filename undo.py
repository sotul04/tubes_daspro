from typing import Type, List
from function import search_log

class tabCandi:
    def __init__(self,Neff:int,detail:List[list] = []):
        self.Neff = Neff
        self.detail = detail

class stack:
    def __init__(self,pos:int,users:List[List[str]] = [],candi:Type[List[tabCandi]] = []):
        self.pos = pos
        self.users = users
        self.candi = candi

def update_stack(stack,user_dat,tabcandi):
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

def undo(stack,user,candi):
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

    

