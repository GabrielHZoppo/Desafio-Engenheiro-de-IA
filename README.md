# Desafio – Engenheiro de IA | Artefact

## 1. Exploração e preparação inicial dos dados
*Initial Data Exploration and Preparation*

### 1.1. Análise dos datasets
*Dataset Analysis*

A primeira etapa do desenvolvimento consistiu na análise dos seis arquivos CSV disponibilizados no desafio:

- `categories.csv` – Categorias de produtos.
- `customers.csv` – Informações dos clientes.
- `order_items.csv` – Itens associados aos pedidos.
- `orders.csv` – Informações e status dos pedidos.
- `products.csv` – Cadastro e características dos produtos.
- `promotions.csv` – Informações sobre promoções.

O objetivo dessa etapa foi compreender a estrutura dos dados, identificar as informações disponíveis e avaliar sua organização para utilização posterior pelo chatbot.

### 1.2. Padronização dos dados
*Data Standardization*

Durante a análise inicial, foi identificada a utilização de português e inglês nos nomes das colunas e nos valores de algumas informações.

Para facilitar a interpretação e utilização dos dados pelo chatbot, foi iniciada a padronização dos nomes das colunas para português, adotando um padrão de nomenclatura consistente.

Também foram padronizados alguns valores categóricos, como os status dos pedidos:

| Valor original | Valor padronizado |
|---|---|
| delivered | entregue |
| shipped | enviado |
| confirmed | confirmado |
| cancelled | cancelado |
| pending | pendente |

### 1.3. Seleção inicial de informações
*Initial Data Selection*

Foi realizada uma avaliação inicial das colunas disponíveis, considerando sua relevância para as funcionalidades previstas para o chatbot.

A coluna `notes`, presente no dataset de pedidos, foi removida inicialmente por conter observações relacionadas aos motivos de cancelamento, informação que não foi considerada necessária para o escopo inicial do atendimento.

Outras colunas e informações ainda poderão passar por avaliação durante as próximas etapas do desenvolvimento.

### 1.4. Verificação da qualidade e integridade dos dados
*Data Quality and Integrity Validation*

Foram realizadas verificações iniciais nos seis datasets utilizando Pandas, com o objetivo de identificar possíveis inconsistências antes da implementação das funcionalidades do chatbot.

As verificações incluíram:

- **Valores duplicados:** identificação de registros integralmente duplicados e verificação de duplicidade nos identificadores principais das tabelas.
- **Valores ausentes:** identificação da quantidade de valores nulos por dataset e por coluna.
- **Integridade referencial:** verificação da correspondência entre os identificadores relacionados nas diferentes tabelas.

Os valores ausentes foram avaliados considerando o contexto de cada informação. Algumas ausências são esperadas, pois determinadas colunas dependem do status do pedido, como informações de cancelamento e entrega.

Também foram verificados os seguintes relacionamentos:

| Tabela de origem | Tabela relacionada | Identificador |
|---|---|---|
| Produtos | Categorias | `id_categoria` |
| Pedidos | Clientes | `id_cliente` |
| Itens dos pedidos | Produtos | `id_produto` |
| Itens dos pedidos | Pedidos | `id_pedido` |
| Promoções | Produtos | `id_produto` |

### 1.5. Próximas etapas
*Next Steps*

- Avaliação de eventuais inconsistências identificadas nas verificações.
- Análise e tratamento dos valores ausentes que realmente necessitem de correção.
- Avaliação da relevância das informações disponíveis para o atendimento ao cliente.
- Desenvolvimento das funções responsáveis pela consulta aos dados.

---

**Observação:** Os arquivos CSV originais são mantidos como referência, enquanto as alterações são realizadas durante o processo de preparação dos dados.
