class OAK:
    def __init__(self, name, nick, limit_low, minimum_reference, maximum_reference, limit_high, units):
        self.name = name
        self.nick = nick
        self.limit_low = limit_low
        self.minimum_reference = minimum_reference
        self.maximum_reference = maximum_reference
        self.limit_high = limit_high
        self.units = units

    def show(self, value):
        if self.limit_low < value < self.minimum_reference:
            print("\033[33m{}".format(f'{self.name} понижены!'))
        elif self.minimum_reference <= value <= self.maximum_reference:
            print("\033[32m{}".format(f'{self.name} в норме!'))
        elif self.maximum_reference < value <= self.limit_high:
            print("\033[31m{}".format(f'{self.name} повышены!'))
        elif value == 0:
            print("\033[31m{}".format(f'Показатель {self.name} не может быть равен нулю!'))
        elif value < 0:
            print("\033[31m{}".format(f'Показатель {self.name} не может быть отрицательный!'))
        else:
            print("\033[31m{}".format(f'Введены некорректные данные уровня {self.name}!'))


""" БЛОК АНАЛИЗОВ КРОВИ: ОАК """
wbc = OAK('Лейкоциты', '(WBC)', 0, 4, 9.5, 30, '[10^9 клеток\л]: ')
rbc = OAK('Эритроциты', '(RBC)', 0, 3.6, 5.1, 30, '[10^9 клеток\л]: ')
hgb = OAK('Гемоглобин', '(HGB)', 30, 130, 160, 300, '[г/л]: ')
hct = OAK('Гематокрит', '(HCT)', 25, 39, 49, 80, '[%]: ')
plt = OAK('Тромбоциты', '(PLT)', 0, 150, 450, 1000, '[10^9 клеток\л]: ')
neut = OAK('Нейтрофильные гранулоциты', '(NEUT)', 0, 45, 70, 100, '[%]: ')
neut_p = OAK('Палочкоядерные нейтрофилы', '(NEUT P)', 0, 1, 5, 20, '[%]: ')
neut_s = OAK('Сегментоядерные нейтрофилы', '(NEUT S)', 0, 1, 5, 20, '[%]: ')
lymph = OAK('Лимфоциты', '(LYMPH)', 0, 22, 46, 100, '[%]: ')
mono = OAK('Моноциты', '(MONO)', 0, 2, 9, 30, '[%]: ')
eos = OAK('Эозинофилы', '(EOS)', 0, 1, 5, 20, '[%]: ')
basso = OAK('Базофилы', '(BASSO)', 0, 0.01, 1, 20, '[%]: ')
esr = OAK('СОЭ', '(ESR)', 0, 2, 8, 30, '[мм/час]: ')

print("\033[01;4m{}".format(" ВВЕДИТЕ ЗНАЧЕНИЯ ОБЩЕГО АНАЛИЗА КРОВИ: "))
list_item_blood = [wbc, rbc, hgb, hct, plt, neut, neut_p, neut_s, lymph, mono, eos, basso, esr]
for i in list_item_blood:
    try:
        i.str_show = input("\033[0m{}".format(f'{i.name} {i.nick} в ед.изм.{i.units}'))
        i.show(value=(float(i.str_show.replace(',', '.'))))
    except ValueError:
        print("\033[31m{}".format(f'Введены некорректные данные уровня {i.name}!'))
