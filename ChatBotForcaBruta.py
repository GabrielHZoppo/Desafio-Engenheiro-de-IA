import unicodedata

# Respostas cadastradas a partir do PDF
respostas = [

    {
        'assunto': 'horario',
        'palavras_chave': [
            'horario', 'funcionamento', 'aberto', 'fechado'
        ],
        'resposta': (
            'Nosso horário de funcionamento é de segunda a sexta, '
            'das 09h às 18h, e aos sábados, das 09h às 13h. '
            'Domingos e feriados estamos fechados.'
        )
    },

    {
        'assunto': 'pagamento',
        'palavras_chave': [
            'pagamento', 'pagar', 'pix', 'cartao', 'boleto'
        ],
        'resposta': (
            'Aceitamos PIX, cartão de débito, cartão de crédito '
            'e boleto bancário. O PIX oferece 5% de desconto. '
            'O cartão de crédito permite parcelamento em até 12 vezes sem juros.'
        )
    },

    {
        'assunto': 'entrega',
        'palavras_chave': [
            'entrega', 'frete', 'prazo', 'receber', 'envio'
        ],
        'resposta': (
            'Na região metropolitana de Campo Grande, o prazo de entrega '
            'é de 1 a 3 dias úteis. Pedidos acima de R$ 500 têm frete grátis; '
            'abaixo desse valor, a taxa é de R$ 35. Para outras cidades, '
            'o frete é calculado conforme o CEP de destino.'
        )
    },

    {
        'assunto': 'troca',
        'palavras_chave': [
            'troca', 'trocar', 'devolucao', 'devolver', 'defeito'
        ],
        'resposta': (
            'Para compras online, você pode solicitar a devolução em até '
            '7 dias corridos após o recebimento. Produtos com defeito de '
            'fabricação podem ser trocados em até 30 dias corridos após a compra.'
        )
    },

    {
        'assunto': 'acessorios',
        'palavras_chave': [
            'acessorio', 'acessorios', 'corda', 'palheta',
            'cabo', 'pedal', 'amplificador', 'case'
        ],
        'resposta': (
            'Trabalhamos exclusivamente com instrumentos musicais. '
            'Não comercializamos acessórios como cordas, palhetas, '
            'cabos, cases, pedais ou amplificadores.'
        )
    }

]


# Função para remover acentos e padronizar o texto
def normalizar(texto):

    texto = texto.lower()

    texto = unicodedata.normalize('NFD', texto)

    texto = ''.join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != 'Mn'
    )

    return texto


# Função para identificar o assunto e retornar a resposta
def buscar_resposta(pergunta):

    pergunta = normalizar(pergunta)

    for item in respostas:

        for palavra in item['palavras_chave']:

            if palavra in pergunta:

                return item['resposta']

    return 'Desculpe, não encontrei uma resposta para sua pergunta.'


# Interação com o usuário
print('Empório da Música - Atendimento Virtual')
print('Digite "sair" para encerrar o atendimento.')

while True:

    pergunta = input('\nVocê: ')

    if pergunta.lower().strip() == 'sair':

        print('Chatbot: Obrigado pelo contato. Até mais!')
        break

    resposta = buscar_resposta(pergunta)

    print('\nChatbot:', resposta)
