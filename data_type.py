"""Memuat classs untuk tipe bentukan"""
from typing import List
# tipe bentukan yang menyimpan data dari FILE EKSTERNAL
class user:
# tipe bentukan
# type user : <Neff : integer {jumlah efektif};
#              detail : array [1..200] of array [1..length] of string;
#              length : integer  = 3 {jumlah string yang disimpan} >
    def __init__(self, Neff:int, detail:List[list], length:int = 3):
        self.Neff = Neff
        self.detail = detail
        self.length = 3

class candi:
# tipe bentukan
# type candi : <Neff : integer {jumlah efektif};
#               detail : array [1..200] of array [1..length] of string;
#               length : integer = 5 {jumlah string yang termuat} >
    def __init__(self, Neff:int, detail:List[list], length:int = 5):
        self.Neff = Neff
        self.detail = detail
        self.length = 5

class bahan:
# tipe bentukan
# type candi : <Neff : integer {jumlah efektif};
#               detail : array [1..200] of array [1..length] of string;
#               length : integer = 3 {jumlah string yang termuat} >
    def __init__(self, Neff:int, detail:List[list], length:int = 3):
        self.Neff = Neff
        self.detail = detail
        self.length = 3
        

# tipe bentukan yang menyimpan data log angka hasil RANDOMISASI
class number_colc:
# tipe bantukan
# type number_colc : <Neff : integer {jumlah efektif};
#                     array : array of integer {menyimpan log data random} >
    def __init__(self,Neff:int,array:list):
        self.Neff = Neff
        self.array = array