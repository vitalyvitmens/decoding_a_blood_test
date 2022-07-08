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
neut_s = OAK('Сегментоядерные нейтрофилы', '(NEUT S)', 0, 45, 70, 100, '[%]: ')
lymph = OAK('Лимфоциты', '(LYMPH)', 0, 22, 46, 100, '[%]: ')
mono = OAK('Моноциты', '(MONO)', 0, 2, 9, 30, '[%]: ')
eos = OAK('Эозинофилы', '(EOS)', 0, 1, 5, 20, '[%]: ')
basso = OAK('Базофилы', '(BASSO)', 0, 0.01, 1, 20, '[%]: ')
esr = OAK('СОЭ', '(ESR)', 0, 2, 8, 90, '[мм/час]: ')

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
                              neut_s_input, lymph_input, mono_input, eos_input, basso_input, esr_input]

try:
    try:
        if 0 < float(list_of_blood_counts[0].input_value) < 4:
            print("\033[33m{}".format(
                f'{list_of_blood_counts[0].name} понижены возможные причины: переболели вирусной и/или '
                f'бактериальной инфекцией.'))
        if 9.5 < float(list_of_blood_counts[0].input_value) <= 30:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[0].name} повышены возможные причины: болеете вирусной и/или '
                f'бактериальной инфекцией.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[1].input_value) < 3.6:
            print("\033[33m{}".format(
                f'{list_of_blood_counts[1].name} понижены возможные причины: острое или хроническое кровотечение.'))
        if 5.1 < float(list_of_blood_counts[1].input_value) <= 30:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[1].name} повышены возможные причины: повышенная продукция эритроцитов.'))
    except ValueError:
        pass
    try:
        if 30 < float(list_of_blood_counts[2].input_value) < 130:
            print("\033[33m{}".format(f'{list_of_blood_counts[2].name} понижен возможные причины: анемия, '
                                      f'кровоточащая язва, онкология - Вам необходимы дополнительные исследования '
                                      f'(УЗИ или КТ внутренних органов, колоноскопия.'))
        if 160 < float(list_of_blood_counts[2].input_value) <= 300:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[2].name} повышен возможные причины: повышенная физическая нагрузка или '
                f'пребывание\nна больших высотах или ожирение.'))
    except ValueError:
        pass
    try:
        if 25 < float(list_of_blood_counts[3].input_value) < 39:
            print("\033[33m{}".format(f'{list_of_blood_counts[3].name} понижен возможные причины: дефицит железа либо '
                                      f'острая или хроническая кровопотеря.'))
        if 49 < float(list_of_blood_counts[3].input_value) <= 80:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[3].name} повышен возможные причины: густая кровь в следствии недостаточного '
                f'потребления жидкости\nили дегидратации, гипоксии или повышенной физической нагрузки.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[4].input_value) < 150:
            print("\033[33m{}".format(f'{list_of_blood_counts[4].name} понижены возможные причины: повышенное '
                                      f'разрушение тромбоцитов\nв следствии иммунологических факторов (аутоиммунные) '
                                      f'или неиммунологических факторов\n(тромбоцитические микроангиопатии, повреждения '
                                      f'тромбоцитов при аномальных\nповерхностях сосудов, инфекционные заболевания '
                                      f'различной вирусно-бактериальной этиологии.'))
        if 450 < float(list_of_blood_counts[4].input_value) <= 1000:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[4].name} повышены возможные причины: инфекционные заболевания, '
                f'воспалительные заболевания,\nзлокачественные заболевания, быстрое восстановление после '
                f'геморрагии/гемолитической анемии,\nвозобновление симптомов после выздоровления при тромбоцитопении, '
                f'\nанатомическая аспления, железодефицит, после оперативного вмешательства.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[5].input_value) < 45:
            print("\033[33m{}".format(f'{list_of_blood_counts[5].name} понижены возможные причины: бактериальные '
                                      f'инфекции (тиф, паратиф, туляремия, \nбруцеллёз, подострый бактериальный '
                                      f'эндокардит), вирусные инфекции (инфекционный гепатит, грипп, корь, краснуха), '
                                      f'\nионизирующее излучение, химические агенты, дефицит витамина В12 и фолиевой '
                                      f'кислоты, аутоиммунный агранулоцитоз (СКВ, РА, АИТ), анафилактический шок.'))
        if 70 < float(list_of_blood_counts[5].input_value) <= 100:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[5].name} повышены возможные причины: острые бактериальные инфекции (абсцессы, '
                f'отит,\nпневмония, острый пиелонефрит, ангина, острый холецистит, тромбофлебит, сепсис, перитонит '
                f'и др.),\nинтоксикации экзогенные (яды, вакцины, бактериальные токсины), интоксикации эндогенные '
                f'(уремия, диабетический ацидоз, подагра, эклампсия, синдром Кушинга.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[6].input_value) < 1:
            print("\033[33m{}".format(f'{list_of_blood_counts[6].name} понижены возможные причины: нейтропения.'))
        if 5 < float(list_of_blood_counts[6].input_value) <= 20:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[6].name} повышены возможные причины: нейтрофилёз.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[7].input_value) < 45:
            print("\033[33m{}".format(f'{list_of_blood_counts[7].name} понижены это говорит об угнетении работы '
                                      f'костного мозга,\nзаражении гельминтами, патологиях вирусного, бактериального '
                                      f'и грибкового происхождения,\nсердечно-сосудистых и прочих заболеваниях.'))
        if 70 < float(list_of_blood_counts[7].input_value) <= 100:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[7].name} может указывать на присутствие в организме острого инфекционного '
                f'заболевания, наличие злокачественной опухоли\nили интоксикации, для которых характерно накапливание '
                f'микробов и продуктов их деятельности.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[8].input_value) < 22:
            print("\033[33m{}".format(f'{list_of_blood_counts[8].name} понижены возможные причины: тяжёлые вирусные '
                                      f'заболевания (грипп), острые бактериальные инфекции,\nсистемная красная '
                                      f'волчанка, при интоксикации тяжелыми металлами, ионизирующим излучением,'
                                      f'\nпервичные и вторичные (гранулемы, метастазы) заболевания костного мозга, '
                                      f'апластическая анемия, почечная недостаточность,\nнедостаточность '
                                      f'кровообращения, злокачественные новообразования.'))
        if 46 < float(list_of_blood_counts[8].input_value) <= 100:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[8].name} повышены возможные причины: вирусные инфекции (инфекционный '
                f'мононуклеоз, цитомегаловирус, краснуха, ветряная оспа),\nтоксоплазмоз, некоторые бактериальные '
                f'инфекции (туберкулёз, коклюш), онкологические заболевания костного мозга (хронический лимфолейкоз)\nи '
                f'лимфоузлов (неходжкинская лимфома), острый вирусный гепатит, травматические повреждения тканей, '
                f'злокачественные опухоли (особенно карцинома бронхов),\nуремия, эклампсия, заболевания щитовидной '
                f'железы, острое кровотечение.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[9].input_value) < 2:
            print("\033[33m{}".format(f'{list_of_blood_counts[9].name} понижены может указывать на ВИЧ-инфекцию, '
                                      f'иммунодефицит, включая синдром Мономака,\nСПИД, аплазию '
                                      f'(атрофическое заболевание) костного мозга, лейкоз или следствие\nхимио - и '
                                      f'лучевой терапии, сильный стресс, прием некоторых лекарств.'))
        if 9 < float(list_of_blood_counts[9].input_value) <= 30:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[9].name} повышены возможные причины: инфекции: подострый бактериальный '
                f'эндокардит, период выздоровления после острых инфекций,\nвирусные (мононуклеоз), грибковые, '
                f'риккетсиозы и протозойные инфекции (малярия, лейшманиоз), гранулематозы: туберкулёз, особенно'
                f'\nактивный, сифилис, бруцеллёз, саркоидоз, язвенный колит, болезни крови - острый монобластный и '
                f'миеломоноцитарный лейкозы, хронический моноцитарный,\nмиеломоноцитарный и миелолейкоз, '
                f'лимфогранулематоз, коллагенозы - СКВ, ревматоидный артрит, узелковый полиартериит.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[10].input_value) < 1:
            print("\033[33m{}".format(f'{list_of_blood_counts[10].name} понижены возможные причины: начальная фаза '
                                      f'инфекционно-токсического процесса,\nхарактерно для тяжёлых пациентов в '
                                      f'послеоперационном периоде.'))
        if 5 < float(list_of_blood_counts[10].input_value) <= 20:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[10].name} повышены возможные причины: аллергические заболевания '
                f'(бронхиальная астма, сенная лихорадка,\nаллергический дерматит, лекарственная аллергия), инвазии '
                f'паразитов (аскаридоз, токсокароз, трихинеллез, эхинококкоз, шистосомоз, филяриоз,\nстронгилоидоз, '
                f'описторхоз, лямблиоз, анкилостомидоз), опухоли - гемобластозы (острый лейкоз, хронический '
                f'миелолейкоз, эритремия, лимфомы,\nлимфогранулематоз), другие опухоли, особенно с метастазами или '
                f'некрозом, болезни соединительной ткани (узелковый полиартериит, ревматоидный артрит),\nэозинофильный '
                f'эзофагит, эозинофильный гастроэнтерит, эозинофильный колит, инфекционные заболевания на стадии'
                f'\nвыздоровления при других инфекциях, наследственная эозинофилия, неаллергический '
                f'эозинофильный ринит.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[11].input_value) < 0.01:
            print("\033[33m{}".format(f'{list_of_blood_counts[11].name} понижены возможные причины: острая фаза '
                                      f'инфекционных заболеваний, реакция на стресс, инфаркт миокарда,\nпосле '
                                      f'длительного лечения стероидами, химиотерапии, облучения, врожденное отсутствие '
                                      f'базофилов, гипертиреоз, крапивница, бронхиальная астма, анафилактический шок,'
                                      f'\nсистемный мастоцитоз, пигментная крапивница, мастоцитарная лейкемия, '
                                      f'макроглобулинемия, лимфомы с медуллярной инвазией, кортикосупраренальная '
                                      f'недостаточность,\nхронические заболевания печени и почек, остеопороз.'))
        if 1 < float(list_of_blood_counts[11].input_value) <= 20:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[11].name} повышены возможные причины: аллергические заболевания '
                f'(аллергический ринит, назальные полипы, хронический синусит,\nбронхиальная астма, атопический '
                f'дерматит, лекарственная аллергия), системный мастоцитоз, пигментная крапивница (педиатрическая\n'
                f'форма ограниченной мастоцитарной пролиферации, с кожной локализацией), базофильная лейкемия, '
                f'болезнь Ходжкина, хроническая гемолитическая анемия,\nпостспленэктомия, после ионизирующего '
                f'облучения, инфекции различной этиологии (туберкулез, ветряная оспа, грипп), гипотиреоз.'))
    except ValueError:
        pass
    try:
        if 0 < float(list_of_blood_counts[12].input_value) < 2:
            print("\033[33m{}".format(f'{list_of_blood_counts[12].name} понижены возможные причины: эритремия и '
                                      f'реактивные эритроцитозы, выраженные явления недостаточности кровообращения, '
                                      f'\nэпилепсия, серповидноклеточная анемия, гемоглобинопатия С, гиперпротеинемия, '
                                      f'гипофибриногенемия, вирусный гепатит и механические желтухи\n(предположительно '
                                      f'в связи с накоплением в крови желчных кислот).'))
        if 8 < float(list_of_blood_counts[12].input_value) <= 90:
            print("\033[31m{}".format(
                f'{list_of_blood_counts[12].name} повышены возможные причины: воспалительные заболевания различной '
                f'этиологии, парапротеинемия, опухолевые заболевания\n(карцинома, саркома, острый лейкоз, '
                f'лимфогранулематоз, лимфомы), болезни соединительной ткани, гломерулонефрит, амилоидоз почек,\n'
                f'протекающие с нефротическим синдромом, уремия, тяжёлые инфекции, инфаркт миокарда, гипопротеинемия, '
                f'анемии, гипо и гипертиреоз, внутренние кровотечения,\nгиперфибриногенемия, гиперхолестеринемия, '
                f'геморрагический васкулит, ревматоидный артрит.'))
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
