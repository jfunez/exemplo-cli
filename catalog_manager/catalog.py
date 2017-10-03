# -*- coding: utf-8 -*-
from six import string_types
from .utils import Singleton


class Product(object):
    name = ''
    price = 0

    def __init__(self, name, price=None):
        self.name = self.sanitize_name(name)

        if price:
            self.price = self.sanitize_price(price)

    @staticmethod
    def sanitize_name(raw_name):
        if isinstance(raw_name, string_types):
            raw_name = raw_name.strip()
            if len(raw_name) > 0:
                return raw_name
            else:
                raise ValueError('O nome não pode ser vazio')
        else:
            raise ValueError('O nome deve ser um string')

    @staticmethod
    def sanitize_price(raw_price):
        if isinstance(raw_price, string_types):
            try:
                return float(raw_price)
            except ValueError:
                # não é possível converter o valor de 'raw_price' para float
                raise ValueError('O preço deve ser conversível para o tipo: "float"')
        elif type(raw_price) != float and type(raw_price) != int:
            raise ValueError('O preço deve ser do tipo: "float" ou "int"')
        else:
            return float(raw_price)

    def __str__(self):
        return "%s (R$ %s)" % (self.name, self.price)


class Catalog(Singleton):
    _product_list = []

    def __len__(self):
        return len(self._product_list)

    def __iter__(self):
        for p in self._product_list:
            yield p

    def clear_product_list(self):
        """
        Limpa a lista de produtos do catálogo
        """
        self._product_list = []

    def add_product(self, name, price=None):
        """
        addiciona um produto no catalogo
        :param: name: (string) nome do produto
        :param: price: (float - opcional) nome do produto
        """

        target_product = self.get_product(name)
        if target_product is None:
            # produto não existe:
            new_product = Product(name, price)
            self._product_list.append(new_product)
        else:
            # produto com esse nome já existe
            raise ValueError('Já existe um produto com esse nome: %s' % str(target_product))

    def update_price(self, name, new_price):
        """
        define um preço para um producto.
        se o produto não foi cadastrado, levanta um ValueError

        :param: name: (string) nome do produto
        :param: price: (int) nome do produto
        """
        target_product = self.get_product(name)
        if target_product is not None:
            target_product.price = Product.sanitize_price(new_price)
        else:
            raise ValueError('o produto com nome %s não existe!' % name)

    def get_product(self, name):
        """
        retorna o produto indicado pelo nome
        caso o produto não existe, retorna None

        :param: name: (string) nome do produto
        """

        for product in self._product_list:
            if product.name == name:
                return product

        # terminou o loop sem fazer return -> produto não existe
        return None

    def remove_product(self, name):
        """
        remove o produto indicado pelo nome
        caso o produto não existe, levanta ValueError

        :param: name: (string) nome do produto
        """

        target_product = self.get_product(name)
        if target_product is None:
            raise ValueError('o produto com nome %s não existe!' % name)
        else:
            # o produto existe na lista de produtos
            self._product_list.remove(target_product)
