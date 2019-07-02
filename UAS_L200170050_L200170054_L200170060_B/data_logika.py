from data_buku import *

def pengurut_judul(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_judul(mid_Kiri)
        pengurut_judul(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][0] < mid_Kanan[j][0]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A

def pengurut_penulis(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_penulis(mid_Kiri)
        pengurut_penulis(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][1] < mid_Kanan[j][1]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A

def pengurut_tanggal(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_tanggal(mid_Kiri)
        pengurut_tanggal(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][2] < mid_Kanan[j][2]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A

def lompat(data, target):
    for i in range(len(data)):
        if target in data[i][0]:
            if data[i][0] == target:
                print('yes 1')
        if target in data[i][1]:
            if data[i][1] == target:
                print('yes 2')
        if target in data[i][2]:
            if data[i][2] == target:
                print('yes 3')
