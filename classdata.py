class Interface:
    def __init__(self, name, config, description=None, mtu=None):
        self.name = name
        self.config = config
        self.description = description
        self.mtu = mtu

    def attributes(self):
        return self.name, self.description, self.config, self.mtu