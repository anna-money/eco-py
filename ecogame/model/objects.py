from ecogame.model.model import ModelManager, ModelObject


class Quest(ModelObject):
    """
    Объект описывающий квест.

    В награду за выполнение квеста игрок получает эко-кристалы
    """
    db_collection_name = 'quest'

    def __init__(self, loader):
        super().__init__(loader)
        self.description = None
        self.reward = 1


class QuestManager(ModelManager):
    model_type = Quest


class Pollution(ModelObject):
    """
    Загрязнение.

    Точка на карте с загрязнением
    """
    db_collection_name = 'pollution'

    def __init__(self, loader):
        super().__init__(loader)
        self.cords = None


class PollutionManager(ModelManager):
    model_type = Pollution


class Zombie(ModelObject):
    """
    Создаются на базе друзей пользователя из социальных сетей.

    Виден только пользователям, у которых находится в соц. сетях.
    """

    db_collection_name = 'zombie'

    def __init__(self, loader):
        super().__init__(loader)
        self.users = []
        self.name = None
        self.cords = None
        self.social = None


class ZombieManager(ModelManager):
    model_type = Zombie


class Robot(ModelObject):
    db_collection_name = 'robot'

    def __init__(self, loader):
        super().__init__(loader)
        self.user = None


class RobotManager(ModelManager):
    model_type = Quest
