class Interface:
    def __init__(self, name, config, description, mtu):
        self.name = name
        self.config = config
        self.description = description
        self.mtu = mtu

    def attributes(self):
        return self.name, self.config, self.description, self.mtu
