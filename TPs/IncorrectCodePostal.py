class IncorrectCodePostal(Exception):
    def __init__(self, value):
        super().__init__(f"le code postale {value} doit contenir exactement 5 chiffres")


