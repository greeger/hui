from datetime import datetime, date
import os

filename = 'C:/Users/79371/Desktop/hui-project/garbage.txt'
with open(filename) as f_input:
    list_data = f_input.readlines()
    f_input.close

startdate = date(2022, 11, 28)
today = date.today()
delta = (today - startdate).days

if delta > (int)(list_data[0]):
    with open(filename, 'w', encoding='utf-8') as f_output:
        f_output.write((str)(delta))
        f_output.close
    
    print('done')


os.system('cd C:/Users/79371/Desktop/hui-project')