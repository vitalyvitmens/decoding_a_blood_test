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
list_item_blood = [wbc, rbc, hgb, hct, plt, neut, neut_p, neut_s, lymph,
                   mono, eos, basso, esr]
for i in list_item_blood:
    try:
        i.str_show = input("\033[0m{}".format(f'{i.name} {i.nick} в ед.изм.{i.units}'))
        i.show(value=(float(i.str_show.replace(',', '.'))))
    except ValueError:
        print("\033[31m{}".format(f'Введены некорректные данные уровня {i.name}!'))

""" БЛОК АНАЛИЗОВ КРОВИ: БИОХИМИЯ """
glucose = OAK('Глюкоза', '(Glucose)', 0, 3.9, 5.6, 50, '[mmol/L]: ')
cholesterol = OAK('Холестерин', '(Cholesterol)', 0, 3.2, 5.2, 30, '[mmol/L]: ')
hdl = OAK('ЛПВП', '(HDL-cholesterol)', 0, 1.03, 2.1, 20, '[mmol/L]: ')
ldl = OAK('ЛПНП', '(LDL-cholesterol)', 0, 1, 4.12, 20, '[mmol/L]: ')
triglyceride = OAK('Триглицериды', '(Triglyceride)', 0, 0.25, 1.7, 20, '[mmol/L]: ')
gpt = OAK('АЛТ', '(GPT)', 0, 5, 45, 1000, '[U/L]: ')
got = OAK('АСТ', '(GOT)', 0, 5, 35, 1000, '[U/L]: ')
ggt = OAK('ГГТ', '(GGT)', 0, 10, 55, 1000, '[U/L]: ')
total_bilirubin = OAK('Билирубин общий', '(Total bilirubin)', 0, 5, 21, 300, '[μmol/L]: ')
direct_bilirubin = OAK('Билирубин прямой', '(Direct bilirubin)', 0, 0.5, 5, 300, '[μmol/L]: ')
creatinine = OAK('Креатинин', '(Creatinine)', 0, 80, 115, 1000, '[μmol/L]: ')
urea = OAK('Мочевина', '(Urea)', 0, 2.8, 7.2, 100, '[mmol/L]: ')
uric_acid = OAK('Мочевая кислота', 0, 208, 428, 3000, '(Uric acid)', '[μmol/L]: ')
total_protein = OAK('Общий белок', '(Total Protein)', 0, 55, 87, 200, '[g/L]: ')
albumin = OAK('Альбумин', '(Albumin)', 0, 35, 52, 200, '[g/L]: ')
srp = OAK('С-реактивный белок', '(SRP)', 0, 0.1, 5, 100, '[mg/L]: ')
srp_sensitive = OAK('СРБ высокочувствительный', '(CRP sensitive)', 0, 0.05, 1, 10, '[mg/L]: ')
alp = OAK('Щелочная фосфатаза', '(ALP)', 0, 40, 130, 3000, '[U/L]: ')
alpha_amylase = OAK('Альфа-Амилаза', '(Alpha-Amylase)', 0, 28, 100, 500, '[U/L]: ')
lipase = OAK('Липаза', '(Lipase)', 0, 13, 60, 1000, '[U/L]: ')

print("\033[01;4m{}".format(" ВВЕДИТЕ ЗНАЧЕНИЯ БИОХИМИЧЕСКОГО ИССЛЕДОВАНИЯ: "))
list_item_blood_biochemistry = [glucose, cholesterol, hdl, ldl, triglyceride,
                                gpt, got, ggt, total_bilirubin, direct_bilirubin,
                                creatinine, urea, uric_acid, total_protein, albumin,
                                srp, srp_sensitive, alp, alpha_amylase, lipase]
for i in list_item_blood_biochemistry:
    try:
        i.str_show = input("\033[0m{}".format(f'{i.name} {i.nick} в ед.изм.{i.units}'))
        i.show(value=(float(i.str_show.replace(',', '.'))))
    except ValueError:
        print("\033[31m{}".format(f'Введены некорректные данные уровня {i.name}!'))
