from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]]

def main() -> None:
    menu()

def menu() -> None:
    print('==================================')
    print('===Bem-Vindo(a)===')
    print('===Mercadinho===')
    print('==================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produtos')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Saindo do sistema...")
        sleep(3)
        exit
    else:
        print('Opção inválida, digite um valor correto')
        sleep(2)
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de produto: ')
    print('===================')

    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preco do produto: '))

    produto = Produto(nome, preco)

    produtos.append(Produto)

    print('Produto cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        contador: int = 1

        print('Lista de produtos:')
        print('=================')
        
        for produto in produtos:
            print(f'{contador} - {produto}')
            contador += 1
            sleep(0.7)
    else:
        print("Sem produtos cadastrados até o momento")
        sleep(2)
    
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('-------------------------------------------------------------')
        print('Produtos Disponíveis:')
        print('======================')

        for produto in produtos:
            print(produto)
            print('---------------------------------------')
            sleep(0.7)
        codigo = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                existe_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidade no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print('Produto adicioando ao carrinho!')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print('Produto adicionado ao carrinho!')
                sleep(2)
                menu()
        else:
            print(f"O produto com o código {codigo} não existe no sistema!")
            sleep(2)
            menu()
    else:
        print('Não existem produtos cadastrados para realizar uma compra!')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do carrinho: ')
        print('====================')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: dados[1]')
                print('-----------------------------------')
                sleep(0.7)
    else:
        print('Carrinho vazio!')
    
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: dados[1]')
                valor_total += dados[0].preco * dados[1]
                print('---------------------------------')
                sleep(1)
        print(f'Sua fatura é de {formata_float_str_moeda(valor_total)}')
        carrinho.clear()
        sleep(3)
    else:
        print('Não existem produtos no carrinho')

    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto

    return p

if __name__ == '__main__':
    main()
