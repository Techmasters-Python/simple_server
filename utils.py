from configparser import ConfigParser


def read_configuration():
    config = ConfigParser()
    config.read('configuration.ini')
    r = config['RUNTIME']
    return dict(r.items())
