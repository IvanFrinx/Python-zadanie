class Interface:
    def __init__(self, name, description, config, mtu):
        self.name = name
        self.description = description
        self.config = config
        self.mtu = mtu

    def attributes(self):
        return self.name, self.description, self.config, self.mtu