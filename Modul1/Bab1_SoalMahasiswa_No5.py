from math import sqrt as sq
def apakahPrima(n):

        n = int(n)
        assert n >= 0
        primaKecil = [2, 3, 5 ,7, 11]
        bknPrimaKecil = [0, 1, 4, 6, 8, 9, 10]
        # mengecek bilangan prima selalu lebih besar dari 1
        if n in primaKecil:
                return True
        elif n in bknPrimaKecil:
                return False
        else:
                # mengecek faktor pembagi dengan operasi modulus
                for i in range(2,int(sq(n))+1):
                        if (n % i) == 0:
                                print (n,"bukan bilangan prima")
                                print ("karena", n,"dikalikan",n//n,"hasilnya adalah",n)
                                break
                else:
                        print (n,"adalah bilangan prima")

