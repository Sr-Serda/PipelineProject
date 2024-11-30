import json
import csv

path_json = "raw_data/dados_empresaA.json"
path_csv = "raw_data/dados_empresaB.csv"

def read_file_json(path_json):
    data_json = []
    with open(path_json, 'r') as file:
        data_json = json.load(file)
    return data_json



data_csv = []
def read_file_csv(path_csv):
    with open(path_csv, "r") as file:
        spamreader = csv.DictReader(file, delimiter= ",")
        for row in spamreader:
            data_csv.append(row)
        return data_csv



def read_file(path, file__type):
    data = []
    if file__type == 'json':
        data = read_file_json(path)
    elif file__type == 'csv':
        data = read_file_csv(path)
    return data


def get_columns(data):
    return list(data[0].keys())

data_json = read_file(path_json, 'json')
column_name_json = get_columns(data_json)

data_csv = read_file(path_csv, 'csv')
column_name_csv = get_columns(data_csv)



key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}


def renaming_columns(data, key_mapping):
    new_data_csv = []
    for old_dict in data:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_data_csv.append(dict_temp)
    return new_data_csv

new_data_csv = renaming_columns(data_csv, key_mapping)
column_name_csv = get_columns(new_data_csv)

def join_data(dataA, dataB):
    combined_list = []
    combined_list.extend(dataA)
    combined_list.extend(dataB)
    return combined_list

def saving_data(data, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def transform_data_table(data, name_column):
    
    data_combined_table = [name_column]

    for row in data:
        line = []
        for column in name_column:
            line.append(row.get(column, 'Indisponivel'))
        data_combined_table.append(line)
    
    return data_combined_table

combined_data = join_data(data_json, new_data_csv)
name_columns_fusion = get_columns(combined_data)



data_combined_table = transform_data_table(combined_data, name_columns_fusion)

path_combined_data = 'data_processed/combined_data.csv'

saving_data(data_combined_table, path_combined_data)

print(path_combined_data)