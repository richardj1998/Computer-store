class laptop:

    def __init__(self, brand, ram, cpu, price):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.price = price

    def comparison_ram(self):
        if self.ram >= 8:
            print("Your RAM is sufficient")
        else:
            print("Your computer RAM is not sufficient, please upgrade your laptop")


class mobiles:
    def __init__(self, brand, storage, network, price):
        self.brand = brand
        self.storage = storage
        self.network = network
        self.price = price

    def comparison_storage(self):
        if self.storage >= 64:
            print("Your storage is sufficient")
        else:
            print("Your mobile storage is not sufficient, please upgrade your cloud storage")



class headphones:
    def __init__(self, brand, loudness, price ):
        self.brand = brand
        self.loudness = loudness
        self.price = price


