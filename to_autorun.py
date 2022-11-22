from datetime import datetime, date
import os

filename = 'C:/Users/79371/Desktop/hui-project/garbage.txt'
with open(filename) as f_input:
    list_data = f_input.readlines()
    f_input.close

startdate = date(2022, 11, 27)
today = date.today()
delta = (today - startdate).days

huiBrightness = [4 , 3 , 0 , 0 , 0 , 3 , 4 , 0 , 4 , 3 , 0 , 3 , 4 , 1 , 0 , 0 , 4 , 4 , 4 , 1 , 0 , 0 , 0 , 4 , 4 , 3 , 0 , 0 ,
    3 , 4 , 3 , 3 , 4 , 2 , 0 , 4 , 3 , 0 , 0 , 2 , 4 , 1 , 0 , 0 , 0 , 0 , 0 , 3 , 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 4 , 4 , 2 , 0 ,
    0 , 0 , 2 , 0 , 2 , 4 , 1 , 0 , 3 , 4 , 0 , 0 , 3 , 4 , 4 , 4 , 1 , 2 , 3 , 4 , 4 , 3 , 0 , 0 , 4 , 3 , 2 , 0 , 0 , 0 , 0 , 0 ,
    0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 4 , 4 , 4 , 4 , 4 , 3 , 0 , 0 , 1 , 3 , 4 , 4 , 4 , 1 , 0 , 3 , 4 ,
    3 , 0 , 3 , 0 , 3 , 4 , 2 , 0 , 0 , 0 , 3 , 4 , 0 , 0 , 0 , 0 , 4 , 4 , 2 , 0 , 0 , 0 , 1 , 4 , 4 , 4 , 4 , 4 , 4 , 4 , 0 , 0 ,
    0 , 0 , 0 , 0 , 0]

if delta > (int)(list_data[0]) and delta >= 0:
    for i in range(huiBrightness[delta] * 2):
        with open(filename, 'w', encoding='utf-8') as f_output:
            f_output.write((str)(delta) + '\n' + (str)(i))
            f_output.close

        os.chdir('C:/Users/79371/Desktop/hui-project')
        os.system('git add garbage.txt')
        os.system('git commit -m "bruhable"')
        os.system('git push')

