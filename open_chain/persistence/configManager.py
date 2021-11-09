from fileManager import fileManager
from uuid import uuid4
DEFAULT_PATH = '/config.json'

class ConfigManager:
  def __init__(self):
    self.filemanager = fileManager(DEFAULT_PATH)

  def load(self):
    if self.filemanager.file_exists():
      config_data = self.filemanager.read()
      return Config(conf=config_data)
    return self.__default()

  def __default(self):
    default_config = Config()
    self.filemanager.write(default_config.to_dict())
    return default_config

class Config:
  '''
    PARAMS:
    * A dict of k:v to map to attributes on the conf obj
  '''
  def __init__(self, conf=None):
    if conf:
      self.__attribute_setter(conf)
    else:
      self.__default()

  def __iter__(self):
    return self.__dict__.iteritems()

  def to_dict(self):
    return dict(self)
  
  def __attribute_setter(self, kvs):
    for key in kvs:
      setattr(self, key, kvs[key])

  def __default(self):
    default_conf = {
      "node": uuid4(),
      "chain_path": '/bl.chain'
    }

    self.__attribute_setter(default_conf)
