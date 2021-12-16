class Packet:
    def __init__(self, transmission):
        self.transmission = transmission
        self.bits = iter()