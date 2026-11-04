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

### 1.4. Próximas etapas
*Next Steps*

- Análise e tratamento de valores ausentes.
- Verificação da integridade e dos relacionamentos entre os datasets.
- Avaliação da relevância das informações disponíveis para o atendimento ao cliente.
- Desenvolvimento das funções responsáveis pela consulta aos dados.

---

**Observação:** Os arquivos CSV originais são mantidos como referência, enquanto as alterações são realizadas durante o processo de preparação dos dados.
