pedidos = []


def adiciona_pedido(nome, sabor):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor

    pedidos.append(pedido)


print(pedidos)
adiciona_pedido('Willian', 'Peperone')
adiciona_pedido('Teste', 'Carne seca')
print(pedidos)
