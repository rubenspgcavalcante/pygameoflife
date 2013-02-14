from helpers.singleton import singleton

@singleton
class Config(object):

    def __init__(self):
        self.config = {
            "game": {
                "window-size": (1024, 768),
                "version": "0.01a",
                "install-dir": "/usr/share/pygameoflife",
            },
            "population": {
                "first-percentage": 0.2,
            },
            "setup": {
                "resolutions": [
                    (400, 300),
                    (800, 600),
                    (1024, 768),
                ],
                "speed": {
                    "slow": 100,
                    "medium": 50,
                    "fast": 25,
                }
            }
        }

    def get(self, key, attr=None):
        try:
            if attr is None:
                return self.config[key]

            else:
                return self.config[key][attr]

        except KeyError:
            return None

    def set(self, key, attr, value):
        try:
            if attr is None:
                self.config[key] = value

            else:
                 self.config[key][attr] = value

        except KeyError:
            return None