# BasesAutomacao

Repositório de estudo para modelos de automações com Typebot e Python.

## Python: relatório de reposição de estoque

Primeiro projeto prático: ler um arquivo CSV, identificar produtos abaixo do estoque mínimo e gerar outro CSV com a quantidade necessária para atingir esse mínimo.

Os dados são fictícios, inspirados em uma loja de acessórios para celulares. Não há integração com um sistema de estoque nem envio de alertas. O script é executado manualmente; não há agendamento.

### Arquivos

- `python/estoque/reposicao.py`: código comentado em português.
- `python/estoque/estoque_exemplo.csv`: quatro produtos para experimentar.

### Como experimentar

Requer Python 3, sem instalar pacotes adicionais. Na pasta principal do repositório:

```sh
python python/estoque/reposicao.py
```

Em ambientes onde o comando é `python3`, use-o no lugar de `python`.

O relatório será criado em `python/estoque/reposicao.csv`. Para executar novamente, escolha outro nome de saída:

```sh
python python/estoque/reposicao.py --saida nova_reposicao.csv
```

Para usar outro CSV, informe `--entrada caminho/estoque.csv`. Ele deve ter as colunas `produto,quantidade,estoque_minimo`, separadas por vírgulas, com quantidades inteiras e não negativas. Arquivos existentes não são sobrescritos.

### Resultado esperado com o exemplo

| Produto | Quantidade atual | Estoque mínimo | Repor |
|---|---:|---:|---:|
| Capa vermelha | 2 | 5 | 3 |
| Carregador USB-C | 0 | 3 | 3 |

Produtos com estoque igual ou superior ao mínimo ficam fora da lista. Se nenhum produto precisar de reposição, o relatório terá somente o cabeçalho.

### Conceitos praticados

Variáveis, listas, funções (`def`), repetição (`for`), condições (`if`), leitura e escrita de arquivos e tratamento de erros. `csv` trabalha com tabelas em texto; `pathlib` representa caminhos de arquivos; `argparse` recebe opções pelo terminal. São módulos da biblioteca padrão do Python.

## Typebot

Espaço reservado para fluxos editáveis de automação com Typebot.
