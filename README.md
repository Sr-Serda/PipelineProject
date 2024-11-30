# Documentação do Projeto: Manipulação de Dados CSV e JSON

Este projeto fornece classes e funções para manipulação e processamento de dados em formatos CSV e JSON. Inclui funcionalidades como leitura de arquivos, renomeação de colunas, fusão de datasets e exportação de dados processados. 

---

## Estrutura do Projeto

### Classes

#### `Dados`
Uma classe orientada a objetos para gerenciar e transformar datasets.

##### Métodos
- **`__init__(self, dados)`**  
  Inicializa a classe com dados fornecidos.
  - `dados`: Lista de dicionários representando os dados.

- **`__leitura_json(path)`** *(Privado, método estático)*  
  Lê dados de um arquivo JSON e os retorna como uma lista de dicionários.

- **`__leitura_csv(path)`** *(Privado, método estático)*  
  Lê dados de um arquivo CSV e os retorna como uma lista de dicionários.

- **`leitura_dados(cls, path, tipo_dados)`** *(Método de classe)*  
  Cria uma instância da classe `Dados` a partir de um arquivo CSV ou JSON.
  - `path`: Caminho para o arquivo.
  - `tipo_dados`: Tipo do arquivo (`'csv'` ou `'json'`).

- **`rename_columns(self, key_mapping)`**  
  Renomeia as colunas do dataset com base em um mapeamento fornecido.
  - `key_mapping`: Dicionário contendo os nomes antigos como chave e os novos nomes como valor.

- **`join(dadosA, dadosB)`** *(Método estático)*  
  Combina dois objetos da classe `Dados` em um único.
  - `dadosA`: Instância da classe `Dados`.
  - `dadosB`: Instância da classe `Dados`.

- **`salvando_dados(self, path)`**  
  Exporta os dados processados para um arquivo CSV no caminho especificado.
  - `path`: Caminho para salvar o arquivo.

---

### Funções Independentes

#### Funções para Leitura de Dados
- **`read_file_json(path_json)`**  
  Lê dados de um arquivo JSON.
  
- **`read_file_csv(path_csv)`**  
  Lê dados de um arquivo CSV.
  
- **`read_file(path, file__type)`**  
  Retorna dados lidos de um arquivo, identificando automaticamente o tipo (`json` ou `csv`).

#### Funções para Processamento
- **`get_columns(data)`**  
  Retorna os nomes das colunas de um dataset.

- **`renaming_columns(data, key_mapping)`**  
  Renomeia colunas em uma lista de dicionários com base em um mapeamento.

- **`join_data(dataA, dataB)`**  
  Combina dois datasets em uma única lista de dicionários.

- **`transform_data_table(data, name_column)`**  
  Transforma os dados em uma tabela adequada para exportação (inclui cabeçalhos e valores).

#### Função para Exportação
- **`saving_data(data, path)`**  
  Salva dados processados em um arquivo CSV.

---

## Exemplo de Uso

```python
from dados import Dados

# Caminhos dos arquivos
path_json = "raw_data/dados_empresaA.json"
path_csv = "raw_data/dados_empresaB.csv"

# Lendo dados de arquivos
dadosA = Dados.leitura_dados(path_json, 'json')
dadosB = Dados.leitura_dados(path_csv, 'csv')

# Renomeando colunas
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}
dadosB.rename_columns(key_mapping)

# Combinando datasets
dados_combinados = Dados.join(dadosA, dadosB)

# Exportando dados combinados
path_combined_data = 'data_processed/combined_data.csv'
dados_combinados.salvando_dados(path_combined_data)
print(f"Dados combinados salvos em: {path_combined_data}")
```

---

## Estrutura de Arquivos

```plaintext
├── raw_data/
│   ├── dados_empresaA.json
│   ├── dados_empresaB.csv
├── data_processed/
│   └── combined_data.csv
├── dados.py
├── README.md
```

---

## Pré-requisitos

- Python 3.7+
- Bibliotecas padrão: `json`, `csv`

---

## Como Executar

1. Clone o repositório.
2. Certifique-se de que os arquivos CSV e JSON estejam no diretório `raw_data`.
3. Execute o script principal para processar os dados:
   ```bash
   python dados.py
   ```

4. O arquivo combinado será gerado no diretório `data_processed`.



