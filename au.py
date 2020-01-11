import xlrd

au = xlrd.open_workbook('au.xlsx')

pruebaing = au.sheet_by_index(0)
pruebaesp = au.sheet_by_index(1)
rowing = 708

txtes = open(r'wronglinkses.txt', 'a' )
txteng = open(r'wronglinkseng.txt', 'a' )
linklist = []
badlinkseng = []
badlinksesp = []
x = 'https://es'

def eng():
    for y in range(rowing):
        a = pruebaing.cell_value(y, 7)
        if x in a:
            txteng.writelines(a)
        if x not in a:
            linklist.append(a)

def esp():
    for y in range(rowing):
        a = pruebaesp.cell_value(y, 7)
        if x in a:
            txtes.writelines(a)
        if x not in a:
            linklist.append(a)



v = input('ESP or ENG?').lower()
if v == 'esp':
    esp()
    print('done, check the text file for the ESP wrong links')
elif v == 'eng':
    eng()
    print('done, check the text file for the ENG wrong links')
else:
    print('please, state your desired language for link checking')
