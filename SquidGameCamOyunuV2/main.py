import random
dizi=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
def randomdeger():
    for i in range(len(dizi)):
        rastgele = random.randint(0, 1)
        for j in range(2):
            if rastgele==1:
                dizi[i][0]=1
            else:
                dizi[i][1]=1
            print(dizi[i][j],end="")
        print()
def tercih(gelensecim,gelendongu):
    if gelendongu==7:
        print("Tebrikler Oyunu Geçtiniz") exit()
    else:
        if gelensecim=="l":
            if dizi[gelendongu][0]==1:
                print("Tebrikler!!! ",gelendongu+1,". aşamayı geçtiniz")
            else:
                print("ÖLDÜNÜZ!!!") return "dead"
        else:
            if dizi[gelendongu][1]==1:
                print("Tebrikler!!! ",gelendongu+1,". aşamayı geçtiniz")
            else:
                print("ÖLDÜNÜZ!!!") return "dead"
randomdeger()
for d in range(len(dizi)):
    secim=input("sola atlamak icin l, saga atlamak icin r yaziniz:")
    yarisma=tercih(secim,d)
    if yarisma=="dead":
        exit()