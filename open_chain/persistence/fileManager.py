from pathlib import Path
import json

class fileManager:
  def __init__(self, file_path):
    self.file_path = Path(r"{input_path}".format(input_path=file_path))

  def write(self, input_data):
    with open (self.file_path, 'w') as data_file:
      file_obj = FileFactory.get_file_type(self.file_path, data_file)
      file_obj.write()

  def read(self):
    with open (self.file_path, 'r') as data_file:
      file_obj = FileFactory.get_file_type(self.file_path, data_file)
      return file_obj.read()

  def file_exists(self, file_path):
    if file_path.exists() and file_path.is_file():
        return True
    return False

class FileFactory:

  @staticmethod
  def get_file_type(input_path, file_wrapper):
    if 'json' in input_path:
      return JsonFile(file_wrapper)
    return ChainFile(file_wrapper)
  

class BaseFile:
  def read(self):
    pass
  def write(self):
    pass

class JsonFile(BaseFile):
  def __init__(self, file_wrapper):
    self.file_wrapper = file_wrapper

  def read(self):
    return json.load(self.file_wrapper)

  def write(self, data):
    json.dump(data, self.file_wrapper, indent=4)

class ChainFile(BaseFile):
  def __init__(self, file_wrapper):
    self.file_wrapper = file_wrapper

  def read(self):
    pass
  def write(self):
    pass
