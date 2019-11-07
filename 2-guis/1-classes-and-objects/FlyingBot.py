from SuperBot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self):
        self.__hover = 0

    def get_hover_distane(self):
        return self.__hover

    def set_hover_distance(self,hover_distance):
        self.__hover = hover_distance


