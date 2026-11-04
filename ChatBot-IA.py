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

