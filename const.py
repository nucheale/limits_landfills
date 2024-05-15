import pandas as pd
import sqlite3
import sys


def excel_to_sql(xls_file, db_file, sql_table_name, columns_list_old, columns_list_new):
    df_excel = pd.read_excel(xls_file, sheet_name='Справочник')
    df_sql = pd.DataFrame()
    if len(columns_list_old) == len(columns_list_new):
        for i in range(0, len(columns_list_new)):
            df_sql[columns_list_new[i]] = df_excel[columns_list_old[i]]
            db = sqlite3.connect(db_file)
            df_sql.to_sql(sql_table_name, db, if_exists='replace', index=False)
            db.close()
        result = 'Выполнено'
    else:
        result = 'В массивах разное количество столбцов'
    print(result)


columns_old = ['Наименование перевозчиков', 'Правильное наименование']
columns_new = ['old_name', 'new_name']
# excel_to_sql('excel/Лимиты полигонов.xlsm', 'reference_data.db', 'Objects', columns_old, columns_new)


