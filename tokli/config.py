import yaml
from os.path import expanduser
from tokli.exceptions import ConfigNameUnknown


class Config():

    @staticmethod
    def get_apis():
        with open("%s/.config/tokli/apis.yaml" % expanduser("~"), 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def get_config_api(name):
        apis = Config.get_apis()['apis']
        try:
            config = apis[name]
        except KeyError:
            raise ConfigNameUnknown
        return config
