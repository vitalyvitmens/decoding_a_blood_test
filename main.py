class OAK:
    def __init__(self, name: str, nick: str, limit_low: float, minimum_reference: float, maximum_reference: float,
                 limit_high: float, units: str):
        """
        Класс OAK (общего анализа крови), включает в себя, для каждого общего анализа крови следующие параметры:
        name: название анализа
        nick: сокращенное название анализа
        limit_low: минимально-реальный предел показаний анализа
        minimum_reference: минимальный референс анализа
        maximum_reference: максимальный референс анализа
        limit_high: максимально-реальный предел показаний анализа
        units: единица измерения анализа
        """
        self.name = name
        self.nick = nick
        self.limit_low = limit_low
        self.minimum_reference = minimum_reference
        self.maximum_reference = maximum_reference
        self.limit_high = limit_high
        self.units = units

    def show(self, value: float):
        """
        Метод show получает на вход параметр value, равный значению пользовательского ввода, какого то конкретного
        параметра из общего анализа крови, в заданных ему единицах измерения и возвращает интерпретацию значения
        (понижен, в норме, повышен) референса данного анализа
        """
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
list_of_blood_counts = [wbc, rbc, hgb, hct, plt, neut, neut_p, neut_s, lymph,
                        mono, eos, basso, esr]
for i in list_of_blood_counts:
    try:
        i.input_value = input("\033[0m{}".format(f'{i.name} {i.nick} в ед.изм.{i.units}'))
        i.str_show = i.input_value
        i.show(float(i.str_show.replace(',', '.')))
    except ValueError:
        print("\033[31m{}".format(f'Введены некорректные данные уровня {i.name}!'))

wbc_input = list_of_blood_counts[0].input_value
rbc_input = list_of_blood_counts[1].input_value
hgb_input = list_of_blood_counts[2].input_value
hct_input = list_of_blood_counts[3].input_value
plt_input = list_of_blood_counts[4].input_value
neut_input = list_of_blood_counts[5].input_value
neut_p_input = list_of_blood_counts[6].input_value
neut_s_input = list_of_blood_counts[7].input_value
lymph_input = list_of_blood_counts[8].input_value
mono_input = list_of_blood_counts[9].input_value
eos_input = list_of_blood_counts[10].input_value
basso_input = list_of_blood_counts[11].input_value
esr_input = list_of_blood_counts[12].input_value

list_of_blood_counts_input = [wbc_input, rbc_input, hgb_input, hct_input, plt_input, neut_input, neut_p_input,
                              neut_s_input,
                              lymph_input, mono_input, eos_input, basso_input, esr_input]

try:
    try:
        if 0 < float(list_of_blood_counts[0].input_value) < 4:
            print("\033[33m{}".format(
                f'{list_of_blood_counts[0].name} понижены, Вы переболели вирусной и/или '
                f'бактериальной инфекцией!'))
        if 9.5 < float(list_of_blood_counts[0].input_value) <= 30:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[0].name} повышены, Вы болеете вирусной и/или бактериальной инфекцией!'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[1].input_value) < 3.6:
            print("\033[33m{}".format(
                f'{list_of_blood_counts[1].name} понижены, у Вас острое или хроническое кровотечение!'))
        if 5.1 < float(list_of_blood_counts[1].input_value) <= 30:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[1].name} повышены, у Вас повышенная продукция эритроцитов!'))
    except ValueError:
        pass
    try:
        if 30 < float(list_of_blood_counts[2].input_value) < 130:
            print("\033[33m{}".format(f'{list_of_blood_counts[2].name} понижен, у Вас анемия!'))
        if 160 < float(list_of_blood_counts[2].input_value) <= 300:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[2].name} повышен, у Вас повышенная физическая нагрузка или '
                f'пребывание на больших высотах или ожирение!'))
    except ValueError:
        pass
except ValueError:
    pass

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
uric_acid = OAK('Мочевая кислота', '(Uric acid)', 0, 208, 428, 3000, '[μmol/L]: ')
total_protein = OAK('Общий белок', '(Total Protein)', 0, 55, 87, 200, '[g/L]: ')
albumin = OAK('Альбумин', '(Albumin)', 0, 35, 52, 200, '[g/L]: ')
srp = OAK('С-реактивный белок', '(SRP)', 0, 0.1, 5, 100, '[mg/L]: ')
srp_sensitive = OAK('СРБ высокочувствительный', '(CRP sensitive)', 0, 0.05, 1, 10, '[mg/L]: ')
alp = OAK('Щелочная фосфатаза', '(ALP)', 0, 40, 130, 3000, '[U/L]: ')
alpha_amylase = OAK('Альфа-Амилаза', '(Alpha-Amylase)', 0, 28, 100, 500, '[U/L]: ')
lipase = OAK('Липаза', '(Lipase)', 0, 13, 60, 1000, '[U/L]: ')

print("\033[37;4m{}".format("\n ВВЕДИТЕ ЗНАЧЕНИЯ БИОХИМИЧЕСКОГО ИССЛЕДОВАНИЯ: "))
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
