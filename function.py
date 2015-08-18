pedidos = []


def cria_pedido(nome, sabor, obs=None):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor
    pedido['obs'] = obs
    return pedido

pedidos.append(cria_pedido('Willian', 'Peperone', 'Sem cebola'))
pedidos.append(cria_pedido('Teste', 'Tomate'))

for pedido in pedidos:
    template = 'Nome: {nome}\nSabor: {sabor}'
    print(template.format(**pedido))
    if pedido['obs']:
        print('Obs: {}'.format(pedido['obs']))

    print('-'*50)
