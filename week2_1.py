user=int(input('Lutfen bir sayi giriniz: '))        #kullanicidan girdi alinir,

a=[i for i in range(1,user)]                        # a isimli listye atanir,

step=0
start=0
last=(len(a)+1)                                     #girdinin eleman sayisi

while last>step+start:
        start+=1  
        step+=1        
             
        for i in range(start,last,step):            #... dan baslayip ...adim gider ve ... last da durur, 
                                                    #liste her silindiginde sola kaydigi icin bir adimla baslanir,
            b=[i for i in range(1,last-2)]              #dongu index tespitinde kullanmak icin liste olusturulur.
             
            if i in b:                              #b listesinde i varsa 
                del a[i]                            #a listesinde i nci indekste bulunan elemani sil
                last=(len(a)+2)                     #last i 2 artir
        
        if last<=step+start:                        #elemanlar azaldikca adimlar arttigi icin
                print(f"lucky numbers...{a}")                
        else:
            print(a)
            last-=1
                            
                 
        
                   
        