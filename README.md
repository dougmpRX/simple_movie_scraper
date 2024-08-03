# Script de Extração e Exportação de Dados de Filmes

## Introdução

Este script é responsável por extrair informações de filmes de uma página web e exportá-las em um arquivo CSV.

### Dependências

- `requests` para fazer requisições HTTP
- `BeautifulSoup` para parsear HTML
- `csv` para exportar dados em formato CSV
- `dotenv` para carregar variáveis de ambiente

### Configuração

Para rodar esse script, você precisará criar um arquivo `.env` na raiz do projeto e definir as seguintes variáveis:

- `BASE_URL`: URL base da página web de filmes
- `MOVIES_URL`: URL específica para a lista de filmes

Exemplo:

```dotenv
BASE_URL=https://example.com/
MOVIES_URL=https://example.com/filmes/lista/index.html
```

Em seguida, você precisará instalar as dependências com o comando:

```bash
pip install -r requirements.txt
```

### Uso

Para gerar o arquivo CSV, basta rodar o script com Python:

```bash
python main.py
```

O script irá criar um arquivo CSV chamado `movies*<número_de_filmes>*<timestamp>.csv` na pasta `./output/`.

Estrutura do Arquivo CSV
O arquivo CSV terá as seguintes colunas:

- `code`: Código do filme
- `title`: Título do filme
- `releaseDate`: Data de lançamento do filme
- `movieUrl`: URL da página do filme
- `imageUrl`: URL da imagem do filme
- `thumbNailUrl`: URL da miniatura do filme
- `actorName`: Nome do ator

### Observações

O script supõe que a página web de filmes tenha uma estrutura HTML conhecida e que as informações dos filmes estejam em um formato que possa ser facilmente parseado.
