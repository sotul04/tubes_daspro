from data_manipulate import *
from data_type import *
from function import *

folder = "data_eksternal\\"
u = folder+"user.csv"
c = folder+"candi.csv"
b = folder+"bahan_bangunan.csv"

data_candi = candi(read_candi(c)[0], read_candi(c)[1])
#remove_candi("chiko", data_candi)
#add_candi("filbert", [3,1,5], data_candi)
#add_candi("mattheuw", [1,4,5], data_candi)
#add_candi("chiko", [5,5,5], data_candi)

for i in range (1,data_candi.Neff):
    print(data_candi.detail[i])