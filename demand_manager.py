class DemandManager:
    def __init__(self, limite_energia):
        self.limite_energia = limite_energia

    def distribuir_energia(self, demandas):
        total_demanda = sum(demandas)

        # Se a demanda estiver dentro do limite
        if total_demanda <= self.limite_energia:
            return demandas

        # Distribuição proporcional
        fator = self.limite_energia / total_demanda

        distribuicao = []
        for demanda in demandas:
            distribuicao.append(round(demanda * fator, 2))

        return distribuicao