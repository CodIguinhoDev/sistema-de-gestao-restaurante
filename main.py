"""
Produto: Para representar os itens do menu, como comidas e bebidas
Pedido: Para gerenciar os itens pedidos pelos clientes
Restaurante: Para gerenciar o menu e os pedidos
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_information(self):
        return f"Produto: {self.name} - R${self.price:.2f}"


class Commands:
    def __init__(self):
        self.notes = []

    def add_products(self, product):
        self.notes.append(product)

    def calculate_total(self):
        return sum(product.price for product in self.notes)

    def view_information(self):
        information = "Comanda:\n"
        for product in self.notes:
            information += f"{product.show_information()}\n"
        information += f"Total: R${self.calculate_total():.2f}"
        return information


class Restaurant:
    def __init__(self):
        self.menu = []

    def add_product_to_menu(self, product):
        self.menu.append(product)

    def show_menu(self):
        print("\n--- MENU ---")
        for product in self.menu:
            print(product.show_information())

    def find_product(self, name):
        for product in self.menu:
            if product.name.lower() == name.lower():
                return product
        return None

    def create_order(self):
        return Commands()


def main():
    restaurant = Restaurant()

    restaurant.add_product_to_menu(Product("Hambúrguer", 25.00))
    restaurant.add_product_to_menu(Product("Pizza", 40.60))
    restaurant.add_product_to_menu(Product("Refrigerante", 8.00))
    restaurant.add_product_to_menu(Product("Café", 5.00))

    order = restaurant.create_order()

    def command_user():
        restaurant.show_menu()

        while True:
            user_input = input("\nDigite o nome do produto (ou 'fim' para encerrar): ")

            if user_input.lower() == "fim":
                break

            product = restaurant.find_product(user_input)

            if product:
                order.add_products(product)
                print(f"{product.name} adicionado!")
            else:
                print("Produto não encontrado. Tente novamente.")

        print("\n--- PEDIDO FINAL ---")
        print(order.view_information())

    command_user()


main()
