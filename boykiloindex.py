
class Height:
    boy = 0
    index = 0
    kilo = 0

    def ideal_kg(self):
        if self.boy > 100:
            self.boy=(self.boy / 100 )
            self.index = (self.kilo / (self.boy * self.boy))
            if self.index < 18:
                print('Olması Gerekenden Az Kilo Almalısın')
            elif 18 <= self.index <= 24.9:
                print('Olması Gerektiği Gibi')
            else:
                print('Obezitelik Var, Kilo Vermelisin ve Spor Yap')
            print(self.index)
        else:
            self.index = (self.kilo / (self.boy * self.boy))
            if self.index < 18:
                print('Olması Gerekenden Az Kilo Almalısın')
            elif 18 <= self.index <= 24.9:
                print('Olması Gerektiği Gibi')
            else:
                print('Obezitelik Var, Kilo Vermelisin ve Spor Yap')
            print(self.index)

birey = Height()
birey.boy = int(input('Boyunuz Nedir? '))
birey.kilo = int(input('Kilonuz Nedir? '))

birey.ideal_kg()
