from function import*

user = list_csv("user.csv")
eff = user[0]
for i in range(eff+1):
    print(user[i])

save_csv(user,"test.csv",3)