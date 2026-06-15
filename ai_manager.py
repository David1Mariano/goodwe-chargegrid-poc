from datetime import datetime

class AIManager:

    @staticmethod
    def horario_pico():
        hora = datetime.now().hour

        # Simulação de horário de pico
        if 18 <= hora <= 22:
            return True

        return False

    @staticmethod
    def ajustar_limite(limite):
        if AIManager.horario_pico():
            return limite * 0.8

        return limite