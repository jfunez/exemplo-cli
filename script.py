# -*- coding: utf-8 -*-

from catalog_manager.catalog import Catalog
from catalog_manager.utils import read_input


class AppCommand(object):

    menu_options = {
        'help': 'mostar esta ajuda',
        'list': 'lista todos produtos',
        'clear': 'esvazia a lista produtos',
        'add': 'adicionar um produto no catálogo',
        'get': 'mostra um produto do catálogo',
        'update': 'atualiza o preço do produto',
        'delete': 'remove um produto do catálogo',
        'quit': 'finalizar este programa',
    }

    catalog = Catalog()

    def print_help(self):
        print('-' * 40)
        for k, v in self.menu_options.items():
            print('| %s\t->\t%s' % (k, v))
        print('-' * 40)

    def print_list(self):
        print('-' * 10, 'Catálogo de produtos', '-' * 10)
        if len(self.catalog) == 0:
            print('| O catálog esta vazio!')
        else:
            for prod in self.catalog:
                print('* \t', prod)
        print('-' * 10, 'Catálogo de produtos', '-' * 10)

    def process_clear(self):
        self.catalog.clear_product_list()
        print('\u2757  O catalogo agora esta vazio!')

    def process_add(self):
        name = read_input('insira o nome do produto')
        price = read_input('insira o preço do produto')

        try:
            self.catalog.add_product(name, price)
        except ValueError as e:
            print('Ocorreu um erro adicionando o produto:\n\t\t', str(e))
        else:
            print('Produto adicionado com sucesso!')

    def process_get(self):
        name = read_input('insira o nome do produto')

        target_product = self.catalog.get_product(name)
        if target_product is None:
            print('O producto com nome: %s não existe!' % name)
        else:
            print('-' * 10, 'Descrição do produto:', '-' * 10)
            print('-' * 40)
            print('*\t', target_product)
            print('-' * 40)

    def process_update(self):
        name = read_input('insira o nome do produto')
        new_price = read_input('insira o preço do produto')

        try:
            self.catalog.update_price(name, new_price)
        except ValueError as e:
            print('Ocorreu um erro atualizando o produto:\n\t\t', str(e))
        else:
            print('Produto atualizado com sucesso!')

    def process_delete(self):
        name = read_input('insira o nome do produto')

        try:
            self.catalog.remove_product(name)
        except ValueError as e:
            print('Ocorreu um erro removendo o produto:\n\t\t', str(e))
        else:
            print('Produto com nome: %s, foi removido com sucesso!' % name)

    def print_quit():
        print('\n\nFinalizando script!')


def main():
    app_cmd = AppCommand()
    app_cmd.print_help()
    while True:

        try:
            option = input('Escolha uma opção: ')
            option = option.strip().lower()
        except KeyboardInterrupt:
            app_cmd.print_quit()
            break
        else:

            if option not in app_cmd.menu_options.keys():
                print('opção inválida. Escolha uma das seguintes opções:')
                app_cmd.print_help()
            elif option == 'help':
                app_cmd.print_help()
            elif option == 'list':
                app_cmd.print_list()
            elif option == 'clear':
                app_cmd.process_clear()
            elif option == 'add':
                app_cmd.process_add()
            elif option == 'get':
                app_cmd.process_get()
            elif option == 'update':
                app_cmd.process_update()
            elif option == 'delete':
                app_cmd.process_delete()
            elif option == 'quit':
                break
            else:
                print('finalizando script!')
                break

if __name__ == '__main__':
    main()
