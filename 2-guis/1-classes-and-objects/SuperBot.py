from Bot import Bot

class SuperBot(Bot):
    def __init__ (self):
        self.__super_power_level = 0

    def get_super_power_level(self):
        return self.__super_power_level

    def set_super_power_level(self,super_power_level):
        self.__super_power_level = super_power_level

