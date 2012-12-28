class Config(object):

    @staticmethod
    def get(key, attr=None):
        config = {
            "game": {
                "window-size": (1024, 768),
                "fps": 10,
                "version": "0.01a"
            },
            "population": {
                "first-percentage": 0.2
            }
        }

        try:
            if attr is None:
                return config[key]

            else:
                return config[key][attr]

        except KeyError:
            return None
