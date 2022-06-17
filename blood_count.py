from tkinter import *
import random
import time


def Quit(ev):
    global root
    root.destroy()


root = Tk()
root.geometry('1000x667')
root.title('Blood Count')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file=('iconka.png')))
font = PhotoImage(file=('holst.png'))

panelFrame = Frame(root, height=100, bg="white")
textFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='bottom', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

Label(root, font=200, text='ПРОГРАММА АНАЛИЗА КРОВИ: BLOOD COUNT 2.0').pack()

quitBtn = Button(panelFrame, bg="red", fg="white", font=200, text='Выход')

quitBtn.bind("<Button-1>", Quit)

quitBtn.place(x=100, y=0, width=800, height=100)

root.mainloop()

print("\033[01;4m{}".format(" ВВЕДИТЕ ЗНАЧЕНИЯ ОБЩЕГО АНАЛИЗА КРОВИ: "))
wbc = input("\033[0m{}".format('Лейкоциты (WBC): '))
rbc = input('Эритроциты (RBC): ')
hgb = input('Гемоглобин (HGB): ')
hct = input('Гематокрит (HCT): ')
plt = input('Тромбоциты (PLT): ')
neut = input('Нейтрофильные гранулоциты (NEUT): ')
neut_p = input('Палочкоядерные нейтрофилы (NEUT P): ')
neut_s = input('Сегментоядерные нейтрофилы (NEUT S): ')
lymp = input('Лимфоциты (LYMP): ')
mono = input('Моноциты (NONO): ')
eos = input('Эозинофилы (EOS): ')
baso = input('Базофилы (BASO): ')
esr = input('СОЭ (ESR): ')

print("\033[01;4m{}".format(" ВВЕДИТЕ ЗНАЧЕНИЯ БИОХИМИЧЕСКОГО ИССЛЕДОВАНИЯ: "))
glucose = input("\033[0m{}".format('Глюкоза (Glucose): '))
cholesterol = input('Холестерин (Cholesterol): ')
hdl = input('ЛПВП (HDL-cholesterol): ')
ldl = input('ЛПНП (LDL-cholesterol): ')
triglyceride = input('Триглицериды (Triglyceride): ')
gpt = input('АЛТ (GPT): ')
got = input('АСТ (GOT): ')
ggt = input('ГГТ (GGT): ')
total_bilirubin = input('Билирубин общий (Total bilirubin): ')
direct_bilirubin = input('Билирубин прямой (Direct bilirubin): ')
creatinine = input('Креатинин (Creatinine): ')
urea = input('Мочевина (Urea): ')
uric_acid = input('Мочевая кислота (Uric acid): ')
total_protein = input('Общий белок (Total Protein): ')
albumin = input('Альбумин (Albumin): ')
srp = input('С-реактивный белок (SRP): ')
srp_sensitive = input('СРБ высокочувствительный (CRP sensitive): ')
alp = input('Щелочная фосфатаза (ALP): ')
alpha_amylase = input('Альфа-Амилаза (Alpha-Amylase): ')
lipase = input('Липаза (Lipase): ')

# ОАК
wbc = float(wbc)  # Лейкоциты (10^9 клеток\л)
if 0 <= wbc < 4:
    print("\033[33m{}".format('Лейкоциты понижены!'))
elif 4 <= wbc <= 9.5:
    print("\033[32m{}".format('Лейкоциты в норме!'))
else:
    print("\033[31m{}".format('Лейкоциты повышены!'))

rbc = float(rbc)  # Эритроциты (10^9 клеток\л)
if 0 <= rbc < 3.6:
    print("\033[33m{}".format('Эритроциты понижены!'))
elif 3.6 <= rbc <= 5.1:
    print("\033[32m{}".format('Эритроциты в норме!'))
else:
    print("\033[31m{}".format('Эритроциты повышены!'))

hgb = float(hgb)  # Гемоглобин (г/л)
if 0 <= rbc < 130:
    print("\033[33m{}".format('Гемоглобин понижен!'))
elif 130 <= rbc <= 160:
    print("\033[32m{}".format('Гемоглобин в норме!'))
else:
    print("\033[31m{}".format('Гемоглобин повышен!'))

hct = float(hct)  # Гематокрит (%)
if 0 <= hct < 39:
    print("\033[33m{}".format('Гематокрит понижен!'))
elif 39 <= hct <= 49:
    print("\033[32m{}".format('Гематокрит в норме!'))
else:
    print("\033[31m{}".format('Гематокрит повышен!'))

plt = float(plt)  # Тромбоциты (10^9 клеток\л)
if 0 <= plt < 150:
    print("\033[33m{}".format('Тромбоциты понижены!'))
elif 150 <= plt <= 450:
    print("\033[32m{}".format('Тромбоциты в норме!'))
else:
    print("\033[31m{}".format('Тромбоциты повышены!'))

neut = float(neut)  # Нейтрофильные гранулоциты (%)
if 0 <= neut < 45:
    print("\033[33m{}".format('Нейтрофильные гранулоциты понижены!'))
elif 45 <= neut <= 70:
    print("\033[32m{}".format('Нейтрофильные гранулоциты в норме!'))
else:
    print("\033[31m{}".format('Нейтрофильные гранулоциты повышены!'))

neut_p = float(neut_p)  # Палочкоядерные нейтрофилы (%)
if 0 <= neut_p < 1:
    print("\033[33m{}".format('Палочкоядерные нейтрофилы понижены!'))
elif 1 <= neut_p <= 5:
    print("\033[32m{}".format('Палочкоядерные нейтрофилы в норме!'))
else:
    print("\033[31m{}".format('Палочкоядерные нейтрофилы повышены!'))

neut_s = float(neut_s)  # Сегментоядерные нейтрофилы (%)
if 0 <= neut_s < 1:
    print("\033[33m{}".format('Сегментоядерные нейтрофилы понижены!'))
elif 1 <= neut_s <= 5:
    print("\033[32m{}".format('Сегментоядерные нейтрофилы в норме!'))
else:
    print("\033[31m{}".format('Сегментоядерные нейтрофилы повышены!'))

lymp = float(lymp)  # Лимфоциты (%)
if 0 <= lymp < 22:
    print("\033[33m{}".format('Лимфоциты понижены!'))
elif 22 <= lymp <= 46:
    print("\033[32m{}".format('Лимфоциты в норме!'))
else:
    print("\033[31m{}".format('Лимфоциты повышены!'))

mono = float(mono)  # Моноциты (%)
if 0 <= mono < 2:
    print("\033[33m{}".format('Моноциты понижены!'))
elif 2 <= mono <= 9:
    print("\033[32m{}".format('Моноциты в норме!'))
else:
    print("\033[31m{}".format('Моноциты повышены!'))

eos = float(eos)  # Эозинофилы (%)
if 0 <= eos < 1:
    print("\033[33m{}".format('Эозинофилы понижены!'))
elif 1 <= eos <= 5:
    print("\033[32m{}".format('Эозинофилы в норме!'))
else:
    print("\033[31m{}".format('Эозинофилы повышены!'))

baso = float(baso)  # Базофилы (%)
if baso <= 0:
    print("\033[33m{}".format('Базофилы понижены!'))
elif 0 < baso <= 1:
    print("\033[32m{}".format('Базофилы в норме!'))
else:
    print("\033[31m{}".format('Базофилы повышены!'))

esr = float(esr)  # СОЭ (мм/час)
if 0 <= esr < 2:
    print("\033[33m{}".format('СОЭ понижена!'))
elif 2 <= esr <= 6:
    print("\033[32m{}".format('СОЭ в норме!'))
else:
    print("\033[31m{}".format('СОЭ повышена!'))

# БИОХИМИЯ
glucose = float(glucose)  # Глюкоза (mmol/L)
if 0 <= glucose < 3.9:
    print("\033[33m{}".format('Глюкоза понижена!'))
elif 3.9 <= glucose <= 5.6:
    print("\033[32m{}".format('Глюкоза в норме!'))
else:
    print("\033[31m{}".format('Глюкоза повышена!'))

cholesterol = float(cholesterol)  # Холестерин (mmol/L)
if 0 <= cholesterol < 3.2:
    print("\033[33m{}".format('Холестерин понижен!'))
elif 3.2 <= cholesterol <= 5.2:
    print("\033[32m{}".format('Холестерин в норме!'))
else:
    print("\033[31m{}".format('Холестерин повышен!'))

hdl = float(hdl)  # ЛПВП (mmol/L)
if 0 <= hdl < 1.03:
    print("\033[33m{}".format('ЛПВП понижены!'))
elif 1.03 <= hdl <= 2.1:
    print("\033[32m{}".format('ЛПВП в норме!'))
else:
    print("\033[31m{}".format('ЛПВП повышены!'))

ldl = float(ldl)  # ЛПНП (mmol/L)
if 0 <= ldl < 1:
    print("\033[33m{}".format('ЛПНП понижены!'))
elif 1 <= ldl <= 4.12:
    print("\033[32m{}".format('ЛПНП в норме!'))
else:
    print("\033[31m{}".format('ЛПНП повышены!'))

triglyceride = float(triglyceride)  # Триглицериды (mmol/L)
if 0 <= triglyceride < 0.25:
    print("\033[33m{}".format('Триглицериды понижены!'))
elif 0.25 <= triglyceride <= 1.7:
    print("\033[32m{}".format('Триглицериды в норме!'))
else:
    print("\033[31m{}".format('Триглицериды повышены!'))

gpt = float(gpt)  # АЛТ (U/L)
if 0 <= gpt < 5:
    print("\033[33m{}".format('АЛТ понижена!'))
elif 5 <= gpt <= 45:
    print("\033[32m{}".format('АЛТ в норме!'))
else:
    print("\033[31m{}".format('АЛТ повышена!'))

got = float(got)  # АСТ (U/L)
if 0 <= got < 5:
    print("\033[33m{}".format('АСТ понижена!'))
elif 5 <= got <= 35:
    print("\033[32m{}".format('АСТ в норме!'))
else:
    print("\033[31m{}".format('АСТ повышена!'))

ggt = float(ggt)  # ГГТ (U/L)
if 0 <= ggt < 10:
    print("\033[33m{}".format('ГГТ понижена!'))
elif 10 <= ggt <= 55:
    print("\033[32m{}".format('ГГТ в норме!'))
else:
    print("\033[31m{}".format('ГГТ повышена!'))

total_bilirubin = float(total_bilirubin)  # Билирубин общий (μmol/L)
if 0 <= total_bilirubin < 5:
    print("\033[33m{}".format('Билирубин общий понижен!'))
elif 5 <= total_bilirubin <= 21:
    print("\033[32m{}".format('Билирубин общий в норме!'))
else:
    print("\033[31m{}".format('Билирубин общий повышен!'))

direct_bilirubin = float(direct_bilirubin)  # Билирубин прямой (μmol/L)
if 0 <= direct_bilirubin < 0.5:
    print("\033[33m{}".format('Билирубин прямой понижен!'))
elif 0.5 <= direct_bilirubin <= 5:
    print("\033[32m{}".format('Билирубин прямой в норме!'))
else:
    print("\033[31m{}".format('Билирубин прямой повышен!'))

creatinine = float(creatinine)  # Креатинин (μmol/L)
if 0 <= creatinine < 80:
    print("\033[33m{}".format('Креатинин понижен!'))
elif 80 <= creatinine <= 115:
    print("\033[32m{}".format('Креатинин в норме!'))
else:
    print("\033[31m{}".format('Креатинин повышен!'))

urea = float(urea)  # Мочевина (mmol/L)
if 0 <= urea < 2.8:
    print("\033[33m{}".format('Мочевина понижена!'))
elif 2.8 <= urea <= 7.2:
    print("\033[32m{}".format('Мочевина в норме!'))
else:
    print("\033[31m{}".format('Мочевина повышена!'))

uric_acid = float(uric_acid)  # Мочевая кислота (μmol/L)
if 0 <= uric_acid < 208:
    print("\033[33m{}".format('Мочевая кислота понижена!'))
elif 208 <= uric_acid <= 428:
    print("\033[32m{}".format('Мочевая кислота в норме!'))
else:
    print("\033[31m{}".format('Мочевая кислота повышена!'))

total_protein = float(total_protein)  # Общий белок (g/L)
if 0 <= total_protein < 66:
    print("\033[33m{}".format('Общий белок понижен!'))
elif 66 <= total_protein <= 87:
    print("\033[32m{}".format('Общий белок в норме!'))
else:
    print("\033[31m{}".format('Общий белок повышен!'))

albumin = float(albumin)  # Альбумин (g/L)
if 0 <= albumin < 35:
    print("\033[33m{}".format('Альбумин понижен!'))
elif 35 <= albumin <= 52:
    print("\033[32m{}".format('Альбумин в норме!'))
else:
    print("\033[31m{}".format('Альбумин повышен!'))

srp = float(srp)  # С-реактивный белок (mg/L)
if 0 <= srp < 0.1:
    print("\033[33m{}".format('С-реактивный белок понижен!'))
elif 0.1 <= srp <= 5:
    print("\033[32m{}".format('С-реактивный белок в норме!'))
else:
    print("\033[31m{}".format('С-реактивный белок повышен!'))

srp_sensitive = float(srp_sensitive)  # СРБ высокочувствительный (mg/L)
if 0 <= srp_sensitive < 0.05:
    print("\033[33m{}".format('СРБ высокочувствительный понижен!'))
elif 0.05 <= srp_sensitive <= 1:
    print("\033[32m{}".format('СРБ высокочувствительный в норме!'))
else:
    print("\033[31m{}".format('СРБ высокочувствительный повышен!'))

alp = float(alp)  # Щелочная фосфатаза (U/L)
if 0 <= alp < 40:
    print("\033[33m{}".format('Щелочная фосфатаза понижена!'))
elif 40 <= alp <= 130:
    print("\033[32m{}".format('Щелочная фосфатаза в норме!'))
else:
    print("\033[31m{}".format('Щелочная фосфатаза повышена!'))

alpha_amylase = float(alpha_amylase)  # Альфа-Амилаза (U/L)
if 0 <= alpha_amylase < 28:
    print("\033[33m{}".format('Альфа-Амилаза понижена!'))
elif 28 <= alpha_amylase <= 100:
    print("\033[32m{}".format('Альфа-Амилаза в норме!'))
else:
    print("\033[31m{}".format('Альфа-Амилаза повышена!'))

lipase = float(lipase)  # Липаза (U/L)
if 0 <= lipase < 13:
    print("\033[33m{}".format('Липаза понижена!'))
elif 13 <= lipase <= 60:
    print("\033[32m{}".format('Липаза в норме!'))
else:
    print("\033[31m{}".format('Липаза повышена!'))
