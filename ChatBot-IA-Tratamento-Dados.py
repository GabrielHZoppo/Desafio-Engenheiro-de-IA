import numpy as np
import pandas as pd

# ler os datasets e analizar o que temos nele

categorias = pd.read_csv("/content/desafio_tecnico_ai_eng - categories.csv")
#display(categorias)

clientes = pd.read_csv("/content/desafio_tecnico_ai_eng - customers.csv")
#display(clientes)

itens_pedidos = pd.read_csv("/content/desafio_tecnico_ai_eng - order_items.csv")
#display(itens_pedidos)

pedidos = pd.read_csv("/content/desafio_tecnico_ai_eng - orders.csv")
#display(pedidos)
# precisa de tratamentos muitos valores Nan

produtos = pd.read_csv("/content/desafio_tecnico_ai_eng - products.csv")
#display(produtos)

promocoes = pd.read_csv("/content/desafio_tecnico_ai_eng - promotions.csv")
#display(promocoes)


# ## Análise inicial indica que tem muitos dados misturados entre inglês e portugues,
#  ## próxima etapa seria fazer a padronização desses dados

categorias.rename(columns={
    'category_id': 'id_categoria',
    'name': 'nome',
    'description': 'descricao'
}, inplace=True)

clientes.rename(columns={
   'customer_id': 'id_cliente',
   'name': 'nome',
   'phone': 'telefone',
   'city': 'cidade'
                         
}, inplace=True)

itens_pedidos.rename(columns={
   'order_id':'id_pedido',
   'quantity': 'quantidade',
   'product_id': 'id_produto'                      
}, inplace=True)

pedidos.rename(columns={
    'order_id': 'id_pedido',
    'customer_id': 'id_cliente',
    'order_date': 'data_pedido',
    'payment_method': 'metodo_pagamento',
    'tracking_code': 'codigo_monitoramento',
    'estimated_delivery':'estimativa_entrega',
}, inplace=True)

pedidos['status'] = pedidos['status'].replace({
    'delivered':'entregue',
    'shipped':'enviado',
    'confirmed':'confirmado',
   'cancelled':'cancelado',
    'pending':'pendente' 
    })


pedidos = pedidos.drop(columns='notes')

produtos.rename(columns={
   'product_id': 'id_produto',
   'price_brl': 'preco',
   'name': 'nome',
   'category_id': 'id_categoria',
   'description': 'descricao',
   'stock_quantity': 'quantidade_estoque',
   'specs': 'especificacoes',
   'created_at': 'criado_em'                      
}, inplace=True)

promocoes.rename(columns={
   'promotion_id':'id_promocao',
   'product_id': 'id_produto',
   'discount_percent': 'disconto_porcentual',
   'description': 'descricao',
   'is_active': 'esta_ativo'                      
}, inplace=True)

## Verificação da integridade e dos relacionamentos entre os datasets

print('--- Produtos → Categorias ---')
print('Referências sem correspondência:',
      (~produtos['id_categoria'].isin(categorias['id_categoria'])).sum())

print('\n--- Pedidos → Clientes ---')
print('Referências sem correspondência:',
      (~pedidos['id_cliente'].isin(clientes['id_cliente'])).sum())

print('\n--- Itens → Produtos ---')
print('Referências sem correspondência:',
      (~itens_pedidos['id_produto'].isin(produtos['id_produto'])).sum())

print('\n--- Itens → Pedidos ---')
print('Referências sem correspondência:',
      (~itens_pedidos['id_pedido'].isin(pedidos['id_pedido'])).sum())

print('\n--- Promoções → Produtos ---')
print('Referências sem correspondência:',
      (~promocoes['id_produto'].isin(produtos['id_produto'])).sum())

## Verificação de valores duplicados e nulos

print('--- Categorias ---')
print('Duplicados:', categorias.duplicated().sum())
print('Valores nulos:')
print(categorias.isna().sum())

print('\n--- Clientes ---')
print('Duplicados:', clientes.duplicated().sum())
print('Valores nulos:')
print(clientes.isna().sum())

print('\n--- Itens dos pedidos ---')
print('Duplicados:', itens_pedidos.duplicated().sum())
print('Valores nulos:')
print(itens_pedidos.isna().sum())

print('\n--- Pedidos ---')
print('Duplicados:', pedidos.duplicated().sum())
print('Valores nulos:')
print(pedidos.isna().sum())

print('\n--- Produtos ---')
print('Duplicados:', produtos.duplicated().sum())
print('Valores nulos:')
print(produtos.isna().sum())

print('\n--- Promoções ---')
print('Duplicados:', promocoes.duplicated().sum())
print('Valores nulos:')
print(promocoes.isna().sum())
