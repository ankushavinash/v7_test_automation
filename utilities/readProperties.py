import configparser

# reading properties from config ini file
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    # static method to fetch application url from config.ini
    @staticmethod
    def get_application_url(environment):
        if environment == "mirror":
            return config.get('common info', 'mirror_url')
        elif environment == "prod":
            return config.get('common info', 'prod_url')
        else:
            return config.get('common info', 'mirror_url')
