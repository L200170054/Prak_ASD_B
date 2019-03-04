def faktorPrima(x) : # x adalah bilangan yang diinputkan untuk di dicari faktor prima nya
    a = []  #untuk menyimpan bilangan prima
    b = []  #untuk menyimpan faktor prima dari bilangan yg diinputkan
    hasil = 0
    bil = x
    prima =True
    for i in range(2,x):
        prima = True
        for u in range(2, i) :
            if i % u == 0 :
               prima = False
        if prima :
            a.append(i)     #menambahkan bilangan prima ke variabel a
    idx = 0
    while bil > 1 :      
        try:    #try untuk mengatasi error ketika index out of range,msal list pnya 5 data maka ketika mengindex data ke6 akan error.
            if (bil%a[idx]) == 0 : # a[idx] untuk mengambil bilangan prima dari list a berdasarkan indexing nya
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])#memasukkan faktor primanya ke 'b'
            else :
                idx = idx + 1
        except IndexError :
            break
    print (b)
