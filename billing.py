class Billing:

    PRECO_KWH = 0.90

    @staticmethod
    def calcular_custo(consumo):
        return round(consumo * Billing.PRECO_KWH, 2)