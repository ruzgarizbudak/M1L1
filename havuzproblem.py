class Pool:
    kapasite = 0
    musluk_kapasite = 0
    musluk_sayisi = 0
    time = 0

    def havuz_doldurma(self):
        self.time = int(self.kapasite / ((self.musluk_kapasite / 1000) * self.musluk_sayisi))
        print(f'Sizin havuzunuz istediğiniz şeylere göre {self.time} dakikada dolar')


m1 = Pool()
m1.kapasite = int(input('Havuzunuz kaç litrelik?'))
m1.musluk_kapasite = int(input('Dakika başına kaç mililitre dolduran musluğa sahipsiniz?'))
m1.musluk_sayisi = int(input('kaç tane musluğunuz var?'))

m1.havuz_doldurma()




        




