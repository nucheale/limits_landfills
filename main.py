import pandas as pd
import sqlite3
import sys
import os


# main_wb = pd.read_excel('excel/Лимиты полигонов.xlsm')

new_df = pd.DataFrame()
db = sqlite3.connect('reference_data.db')

files_to_open = os.listdir('excel/Реестры/')

landfills_count = db.execute('SELECT COUNT("landfill_name") as "CC" FROM Landfills').fetchone()
# print(landfillsCount[0])
objects = db.execute('SELECT old_name, new_name FROM Objects').fetchall()
# print(objects[0])
# print(len(objects))
landfill_titles = db.execute('SELECT landfill FROM Column_titles WHERE landfill IS NOT NULL').fetchall()
weight_1_titles = db.execute('SELECT w1 FROM Column_titles WHERE w1 IS NOT NULL').fetchall()
weight_2_titles = db.execute('SELECT w2 FROM Column_titles WHERE w2 IS NOT NULL').fetchall()

# sys.exit(0)

file_index = 1
for file in files_to_open:
    df_object = pd.read_excel(f'excel/Реестры/{file}', sheet_name='Вывоз')
    current_object = None
    #  'текущий объект по названию файла
    for i in range(0, len(objects)):
        if objects[i][0] in file:
            current_object = objects[i][1]
            # print(current_object)

    # 'определение МСС/МПС
    sort = True if 'Обработка' in file else False

    last_column_object = df_object.shape[1]
    # print(last_column_object)
    landfill_title_column = None
    weight_object_title_column = None
    weight_landfill_title_column = None
    merged_title_columns = ''  # 'для проверки нашлись ли названия столбцов или нет

    for e in landfill_titles:
        if df_object.columns.isin([e[0]]).any():
            landfill_title_column = df_object.columns.get_loc(e[0])
            merged_title_columns = f'{merged_title_columns}{str(landfill_title_column)[0]}'
            break

    for e in weight_1_titles:
        if df_object.columns.isin([e[0]]).any():
            weight_object_title_column = df_object.columns.get_loc(e[0])
            merged_title_columns = f'{merged_title_columns}{str(weight_object_title_column)[0]}'
            break

    for e in weight_2_titles:
        if df_object.columns.isin([e[0]]).any():
            weight_landfill_title_column = df_object.columns.get_loc(e[0])
            merged_title_columns = f'{merged_title_columns}{str(weight_landfill_title_column)[0]}'
            break

    # здесь надо писать в каком файле какой столбец не нашелся

    last_row_object = df_object.shape[0]
    # здесь проверка что last_row_object > 2
    dates_of_object = df_object.iloc[:, 0]
    landfills_of_object = df_object.iloc[:, landfill_title_column]
    weights_1_object = df_object.iloc[:, weight_object_title_column]
    weights_2_object = df_object.iloc[:, weight_landfill_title_column]

