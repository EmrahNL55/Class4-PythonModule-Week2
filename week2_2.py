user=int(input("lutfen bir sayi giriniz; "))
user_2=int(input("lutfen bir sayi giriniz :"))      #kullanicidan iki sayi alinir

a=[i for i in range(1,user+1)]
item=len(a)                                 #sayi for range ile 1 den baslayarak listeye alinir,
while item > 0:                           #liste eleman sayisi 0 dan buyuk ise donguye girilir,
    if user_2<0:                            #2. sayi 0 dan kucuk ise,
        user_2=user_2*-1                    #sayi pozitif yapilir
        user_2-=1                           # 1 eksiltilir (index isleminde kullanilacagi icin)
        b=a.pop(0)                          # a nin O. indexdeki degeri silinir b ye atanir,
        a.append(b)                         # silinen deger .append ile sona tekrar eklenir,
        user_2=user_2*-1                    # 2.sayi -1 ile carpirlip tekrar negatif yapilir(while dongusu icin)
        if user_2==0:                       # 2.sayi 0 a esitse 
            print(a)                        # print islemi,
            item-=item                      # donguden cikilmasi icin item sifira esitlenir,
                
    else:
        for i in range(user_2):             #sayi pozitif ise for ile 2. sayi i atanir,
            if i !=len(a)-1:                # i item sayisina esit degilse
                b=a.pop(len(a)-1)           # son item silinir ve b ye atanir,
                a.insert(0,b)               # insert ile tekrar a nin ilk index ne eklenir,
        print(a)                            #for bitince print yapilir 
        item-=item                          # while dan cikmak icin item sifira esitlenir,
             
        
        
            
