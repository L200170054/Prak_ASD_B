class data_buku(object):
    
    """class data untuk Buku"""
    
    def __init__(self, judul_buku, nama_penulis, tanggal_terbit):
        self.judul = judul_buku
        self.penulis = nama_penulis
        self.tanggal = tanggal_terbit

    def __repr__(self):
        info = self.judul + ', ' + self.penulis + ', ' + self.tanggal
        return info

    def __str__(self):
        info = self.judul + ', ' + self.penulis + ', ' + self.tanggal
        return info

class my_Array(object):
    
    """class untuk Array pada buku"""

    def __init__(self):
        self.index = 15 * [None]
        
    def __getitem__(self, item):
        getData = self.index[item]
        return getData
    
    def __setitem__(self, key, value):
        self.index[key] = value

#-------------------------------------------------------------------------------#

buku_1 = data_buku('Percy Jackson & the Olympians : The Lightning Thief',
                   'Rick Riordan',
                   '2005')
buku_2 = data_buku('Percy Jackson & the Olympians : The Sea of Monsters',
                   'Rick Riordan',
                   '2006')
buku_3 = data_buku('Percy Jackson & the Olympians : The Titan`s Curse',
                   'Rick Riordan',
                   '2007')
buku_4 = data_buku('Percy Jackson & the Olympians : The Battle of the Labyrith',
                   'Rick Riordan',
                   '2007')
buku_5 = data_buku('It',
                   'Stephen King',
                   '1986')
buku_6 = data_buku('Carrie',
                   'Stephen King',
                   '1974')
buku_7 = data_buku('The Shining',
                   'Stephen King',
                   '1977')
buku_8 = data_buku('Misery',
                   'Stephen King',
                   '1987')
buku_9 = data_buku('Pet Sematary',
                   'Stephen King',
                   '1983')
buku_10 = data_buku('The Inferno',
                   'Dan Brown',
                   '2013')
buku_11 = data_buku('Harry Potter and thePhilosopher`s Stone',
                   'J.K.Rowling',
                   '1997')
buku_12 = data_buku('Harry Potter and the Chamber of Secrets',
                   'J.K.Rowling',
                   '1998')
buku_13 = data_buku('Harry Potter and the Prisoner of Azkaban',
                   'J.K.Rowling',
                   '1999')
buku_14 = data_buku('Harry Potter and the Goblet of Fire',
                   'J.K.Rowling',
                   '2000')
buku_15 = data_buku('Harry Potter and the Order of the Phonix',
                   'J.K.Rowling',
                   '2003')
buku_16 = data_buku('Harry Potter and the Half-Blood Princes',
                   'J.K.Rowling',
                   '2005')
buku_17 = data_buku('Harry Potter and the Deathly Hallows',
                   'J.K.Rowling',
                   '2007')

#-------------------------------------------------------------------------------#

akumulasi_data = my_Array()

akumulasi_data[0] = buku_1
akumulasi_data[1] = buku_2
akumulasi_data[2] = buku_3
akumulasi_data[3] = buku_4
akumulasi_data[4] = buku_5
akumulasi_data[5] = buku_6
akumulasi_data[6] = buku_7
akumulasi_data[7] = buku_8
akumulasi_data[8] = buku_9
akumulasi_data[9] = buku_10
akumulasi_data[10] = buku_11
akumulasi_data[11] = buku_12
akumulasi_data[12] = buku_13
akumulasi_data[13] = buku_14
akumulasi_data[14] = buku_15

akumulasi_data_judul = my_Array()

akumulasi_data_judul[0] = buku_1.judul
akumulasi_data_judul[1] = buku_2.judul
akumulasi_data_judul[2] = buku_3.judul
akumulasi_data_judul[3] = buku_4.judul
akumulasi_data_judul[4] = buku_5.judul
akumulasi_data_judul[5] = buku_6.judul
akumulasi_data_judul[6] = buku_7.judul
akumulasi_data_judul[7] = buku_8.judul
akumulasi_data_judul[8] = buku_9.judul
akumulasi_data_judul[9] = buku_10.judul
akumulasi_data_judul[10] = buku_11.judul
akumulasi_data_judul[11] = buku_12.judul
akumulasi_data_judul[12] = buku_13.judul
akumulasi_data_judul[13] = buku_14.judul
akumulasi_data_judul[14] = buku_15.judul

akumulasi_data_penulis = my_Array()

akumulasi_data_penulis[0] = buku_1.penulis
akumulasi_data_penulis[1] = buku_2.penulis
akumulasi_data_penulis[2] = buku_3.penulis
akumulasi_data_penulis[3] = buku_4.penulis
akumulasi_data_penulis[4] = buku_5.penulis
akumulasi_data_penulis[5] = buku_6.penulis
akumulasi_data_penulis[6] = buku_7.penulis
akumulasi_data_penulis[7] = buku_8.penulis
akumulasi_data_penulis[8] = buku_9.penulis
akumulasi_data_penulis[9] = buku_10.penulis
akumulasi_data_penulis[10] = buku_11.penulis
akumulasi_data_penulis[11] = buku_12.penulis
akumulasi_data_penulis[12] = buku_13.penulis
akumulasi_data_penulis[13] = buku_14.penulis
akumulasi_data_penulis[14] = buku_15.penulis

akumulasi_data_tanggal = my_Array()

akumulasi_data_tanggal[0] = buku_1.tanggal
akumulasi_data_tanggal[1] = buku_2.tanggal
akumulasi_data_tanggal[2] = buku_3.tanggal
akumulasi_data_tanggal[3] = buku_4.tanggal
akumulasi_data_tanggal[4] = buku_5.tanggal
akumulasi_data_tanggal[5] = buku_6.tanggal
akumulasi_data_tanggal[6] = buku_7.tanggal
akumulasi_data_tanggal[7] = buku_8.tanggal
akumulasi_data_tanggal[8] = buku_9.tanggal
akumulasi_data_tanggal[9] = buku_10.tanggal
akumulasi_data_tanggal[10] = buku_11.tanggal
akumulasi_data_tanggal[11] = buku_12.tanggal
akumulasi_data_tanggal[12] = buku_13.tanggal
akumulasi_data_tanggal[13] = buku_14.tanggal
akumulasi_data_tanggal[14] = buku_15.tanggal

akumulasi_data_final = my_Array()

akumulasi_data_final[0] = [buku_1.judul, buku_1.penulis, buku_1.tanggal]
akumulasi_data_final[1] = [buku_2.judul, buku_2.penulis, buku_2.tanggal]
akumulasi_data_final[2] = [buku_3.judul, buku_3.penulis, buku_3.tanggal]
akumulasi_data_final[3] = [buku_4.judul, buku_4.penulis, buku_4.tanggal]
akumulasi_data_final[4] = [buku_5.judul, buku_5.penulis, buku_5.tanggal]
akumulasi_data_final[5] = [buku_6.judul, buku_6.penulis, buku_6.tanggal]
akumulasi_data_final[6] = [buku_7.judul, buku_7.penulis, buku_7.tanggal]
akumulasi_data_final[7] = [buku_8.judul, buku_8.penulis, buku_8.tanggal]
akumulasi_data_final[8] = [buku_9.judul, buku_9.penulis, buku_9.tanggal]
akumulasi_data_final[9] = [buku_10.judul, buku_10.penulis, buku_10.tanggal]
akumulasi_data_final[10] = [buku_11.judul, buku_11.penulis, buku_11.tanggal]
akumulasi_data_final[11] = [buku_12.judul, buku_12.penulis, buku_12.tanggal]
akumulasi_data_final[12] = [buku_13.judul, buku_13.penulis, buku_13.tanggal]
akumulasi_data_final[13] = [buku_14.judul, buku_14.penulis, buku_14.tanggal]
akumulasi_data_final[14] = [buku_15.judul, buku_15.penulis, buku_15.tanggal]

#-------------------------------------------------------------------------------#

data_semua = [akumulasi_data[0], akumulasi_data[1], akumulasi_data[2],
              akumulasi_data[3], akumulasi_data[4], akumulasi_data[5],
              akumulasi_data[6], akumulasi_data[7], akumulasi_data[8],
              akumulasi_data[9], akumulasi_data[10], akumulasi_data[11],
              akumulasi_data[12], akumulasi_data[13], akumulasi_data[14]]

data_final = [akumulasi_data_final[0], akumulasi_data_final[1],
              akumulasi_data_final[2], akumulasi_data_final[3],
              akumulasi_data_final[4], akumulasi_data_final[5],
              akumulasi_data_final[6], akumulasi_data_final[7],
              akumulasi_data_final[8], akumulasi_data_final[9],
              akumulasi_data_final[10], akumulasi_data_final[11],
              akumulasi_data_final[12], akumulasi_data_final[13],
              akumulasi_data_final[14]]

data_ulti = [akumulasi_data_judul[0], akumulasi_data_penulis[0],
             akumulasi_data_tanggal[0], akumulasi_data_judul[1],
             akumulasi_data_penulis[1], akumulasi_data_tanggal[1],
             akumulasi_data_judul[2], akumulasi_data_penulis[2],
             akumulasi_data_tanggal[2], akumulasi_data_judul[3],
             akumulasi_data_penulis[3], akumulasi_data_tanggal[3],
             akumulasi_data_judul[4], akumulasi_data_penulis[4],
             akumulasi_data_tanggal[4], akumulasi_data_judul[5],
             akumulasi_data_penulis[5], akumulasi_data_tanggal[5],
             akumulasi_data_judul[6], akumulasi_data_penulis[6],
             akumulasi_data_tanggal[6], akumulasi_data_judul[7],
             akumulasi_data_penulis[7], akumulasi_data_tanggal[7],
             akumulasi_data_judul[8], akumulasi_data_penulis[8],
             akumulasi_data_tanggal[8], akumulasi_data_judul[9],
             akumulasi_data_penulis[9], akumulasi_data_tanggal[9],
             akumulasi_data_judul[10], akumulasi_data_penulis[10],
             akumulasi_data_tanggal[10], akumulasi_data_judul[11],
             akumulasi_data_penulis[11], akumulasi_data_tanggal[11],
             akumulasi_data_judul[12], akumulasi_data_penulis[12],
             akumulasi_data_tanggal[12], akumulasi_data_judul[13],
             akumulasi_data_penulis[13], akumulasi_data_tanggal[13],
             akumulasi_data_judul[14], akumulasi_data_penulis[14],
             akumulasi_data_tanggal[14]]

data_judul = [akumulasi_data_judul[0], akumulasi_data_judul[1],
              akumulasi_data_judul[2], akumulasi_data_judul[3],
              akumulasi_data_judul[4], akumulasi_data_judul[5],
              akumulasi_data_judul[6], akumulasi_data_judul[7],
              akumulasi_data_judul[8], akumulasi_data_judul[9],
              akumulasi_data_judul[10], akumulasi_data_judul[11],
              akumulasi_data_judul[12], akumulasi_data_judul[13],
              akumulasi_data_judul[14]]

data_penulis = [akumulasi_data_penulis[0], akumulasi_data_penulis[1],
                akumulasi_data_penulis[2], akumulasi_data_penulis[3],
                akumulasi_data_penulis[4], akumulasi_data_penulis[5],
                akumulasi_data_penulis[6], akumulasi_data_penulis[7],
                akumulasi_data_penulis[8], akumulasi_data_penulis[9],
                akumulasi_data_penulis[10], akumulasi_data_penulis[11],
                akumulasi_data_penulis[12], akumulasi_data_penulis[13],
                akumulasi_data_penulis[14]]

data_tanggal = [akumulasi_data_tanggal[0], akumulasi_data_tanggal[1],
                akumulasi_data_tanggal[2], akumulasi_data_tanggal[3],
                akumulasi_data_tanggal[4], akumulasi_data_tanggal[5],
                akumulasi_data_tanggal[6], akumulasi_data_tanggal[7],
                akumulasi_data_tanggal[8], akumulasi_data_tanggal[9],
                akumulasi_data_tanggal[10], akumulasi_data_tanggal[11],
                akumulasi_data_tanggal[12], akumulasi_data_tanggal[13],
                akumulasi_data_tanggal[14]]

print(data_final)
