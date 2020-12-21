boy=int(input("Boyunuzu giriniz(cm cinsinden): "))
kilo=float(input("Kilonuzu giriniz: "))
vki=kilo/((boy/100)**2)
print("Vücut kitle index'iniz {}".format(round(vki,2)))
print("Durumunuz: ")
if vki <=18.5:
    print("Zayıf -bir deri bir kemik kalmışsın kardeş-")
    print("{} kilogram almanız gerekiyor".format(round(18.5*((boy/100)**2)-kilo,2)))
elif vki <=24.9:
    print("So Normal")
elif vki<=29.9:
    print("Fazla kilolu eh işte")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
elif vki<=39.9:
    print("Obez haha biraz yavaşla")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
else:
    print("Dünyayı yedin dur artık -aşırı obez-")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
