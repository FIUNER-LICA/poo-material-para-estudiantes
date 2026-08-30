class AgenteTemperatura:
    def __init__(self):
        self.creencias = {}
        self.objetivo = "mantener_temperatura_segura"

    # Percepción
    def percibir(self, temperatura):
        self.creencias["temperatura"] = temperatura

    # Decisión
    def decidir(self):
        temperatura = self.creencias["temperatura"]

        if temperatura > 30:
            return "enfriar"
        elif temperatura < 18:
            return "calentar"
        else:
            return "mantener"

    # Capacidades del agente
    def accion_enfriar(self):
        print("Activo el sistema de refrigeración.")

    def accion_calentar(self):
        print("Activo el sistema de calefacción.")

    def accion_mantener(self):
        print("La temperatura es adecuada.")

    # Introspección
    def capacidades(self):
        return [
            nombre.removeprefix("accion_")
            for nombre in dir(self)
            if nombre.startswith("accion_")
        ]

    # Ejecución reflexiva
    def actuar(self, decision):
        nombre_metodo = f"accion_{decision}"

        if not hasattr(self, nombre_metodo):
            raise ValueError(f"No poseo la capacidad: {decision}")

        accion = getattr(self, nombre_metodo)
        accion()

    def ejecutar(self, temperatura):
        self.percibir(temperatura)

        print("Objetivo:", self.objetivo)
        print("Creencias:", self.creencias)
        print("Capacidades:", self.capacidades())

        decision = self.decidir()
        print("Decisión:", decision)

        self.actuar(decision)


agente = AgenteTemperatura()
agente.ejecutar(34)