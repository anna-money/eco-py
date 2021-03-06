from ecogame.handler.common_handler import CommonHandler
from ecogame.version import version


class LandingPageHandler(CommonHandler):
    def get(self):
        """
        Возвращает стартовую страницу
        """
        self.render("index.html")


class StatusHandler(CommonHandler):
    def get(self):
        """
        Возвращает версию текующего приложения в JSON
        """
        self.send_json({'version': version})
