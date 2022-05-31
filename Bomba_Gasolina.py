class Bomba_combustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastercer: float):
        litros_abastecer = valor_abastercer / self.valor_litro
        self._calcula_quantidade(litros_abastecer, litros_abastecer * self.valor_litro)

    def abastecer_por_litro(self, quantidade_litros: float):
        valor_pagar = quantidade_litros * self.valor_litro
        self._calcula_quantidade(quantidade_litros, valor_pagar)

    def _calcula_quantidade(self, litros: float, valor_pagar: float):
        if (litros > self.quantidade_combustivel):
            print(f"\nNão é possivel abastecer, a bomba não tem {self.tipo_combustivel} suficiente.")
        else:
            self.quantidade_combustivel -= litros
            print(f"\n{litros:.2f} litros abastecidos, Valor a pagar: R${valor_pagar:.2f}")
            print(f"{self.quantidade_combustivel:.2f} Litros restantes na bomba de {self.tipo_combustivel}")

    def exibe_tipo(self):
        return print("\n", self.tipo_combustivel)

    def exibe_valor(self):
        return print(f"\nR${self.valor_litro:.2f}")

    def exibe_quantidade(self):
        return print(f"\n{self.quantidade_combustivel:.2f} Litros.")

    def altera_valor(self, valor: float):
        if(valor > 0):
            self.__valor_litro = valor
            print("Valor alterado!")
        else:
            print('Valor inválido.')

    def altera_tipo(self, tipo):
        self.valor_litro = tipo

    def altera_quantidade(self, quantidade: float):
        if(quantidade > 0):
            self.quantidade_combustivel += quantidade
            print(f"\nBomba reabastecida!")
            print(f"Quantidade de combustível na bomba: {self.quantidade_combustivel:.2f} Litros.")
        else:
            print("Valor inválido.")

bomba = Bomba_combustivel('Gasolina', 4.55, 100.0)

bomba.abastecer_por_valor(100)

bomba.abastecer_por_litro(70)

bomba.abastecer_por_litro(10)

bomba.altera_quantidade(100)