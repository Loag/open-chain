from chainManager import ChainManager
from configManager import ConfigManager

'''
  this object will make sure that the chain is flushed to disk
  and that the current chain doesn't drift far from the disk chain
'''
class PersistenceManager:
  def __init__(self):
    pass