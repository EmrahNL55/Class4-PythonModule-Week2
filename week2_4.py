woord=input("lutfen bir kelime giriniz: ")
woord_2=input("lutfen bir kelime giriniz: ")    #kullanicidan iki giris alinir,
woord_2=woord_2.strip(',.!*')                   #(',.!*') isaretleri varsa silinir,
woord=woord.strip(',.!*')
woord_2=woord_2.lower()                         #tum harfler kucuk yapilir,
woord=woord.lower()
woord_2=[i for i in woord_2]                    #string liseye alinir,
woord=[i for i in woord]
woord_2.sort()                                  #listedeki harfler siralanir,
woord.sort()
both=""                                         #bos bir degisken her ikis kelimede bulunan harfleri tutmak icin,
letters_1=""                                    #sadece 1. kelimede olan harfler tutmak icin,
letters_2=""                                    #sadece 2.kelimede olan harfleri tutmak icin,
list_result=[]                                  #olusturulan kelime ya da harflerin eklenmesi icin bos liste,

for i in woord:                                 #woord listesindeki harfler i ye atanir,
    if i in woord_2:                            #sirayla woord_2 deki harfler ile karsilastirilir eger ayni ise,
        both+=i                                 #both isimli degiskene eklenir(+)

    elif i not in woord_2:                      #ayni degilse,
        letters_1+=i                            #letters_1 e eklenir(+)
        
for i in woord_2:                               #woord_2 deki harfler sirayla i ye atanir,
    if i not in woord:                          #sirayla woord deki harfler ile karsilastirilir eger yok (not in) ise,
        letters_2+=i                            # letters_2 ye eklenir(+)  
list_result.append(both)                        #.append ile both degiskenindeki kelime list_result a eklenir

list_result.append(letters_1)                   #.append ile letters_1 degiskenindeki kelime list_result a eklenir

list_result.append(letters_2)                   #.append ile lettrs_2 degiskenindeki kelime list_result a eklenir

print(list_result)


