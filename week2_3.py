user=input("lutfen bir cumle giriniz: ")    #girdi alinir,
user=user.lower()                           # harfler kucuk harf yapilir,
user=user.strip(',.!*')                     # karakter iceren degisken olusuturulur,
user_letter=[i for i in user]               #cumle listeye cevrilir,
list_letter=[]                              #bos liste olusturullur harfler icin
list_count=[]                               # bos liste olusturrulr rakamlar icin

for i in user_letter:                       #liste i degiskenine sira ile atanir,
     if i not in list_letter:               # i liste de yoksa ayni har iki kere yazilmamasi icin,
         b=user_letter.count(i)             # harfleri say b ye at
         list_count.append(b)               # lis-count listesine b deki rakami ekle
         list_letter.append(i)              # i deki harfi list letter listesine ekle
                                            #ayni anda bir listeye harf digerine o harfin adedi atanmis oluyor,
result=list(zip(list_letter,list_count))     # zip ile iki liste birlestirilir ve resul listesine eklenir,
print(result)
