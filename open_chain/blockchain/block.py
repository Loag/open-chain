from time import time
from uuid import uuid4

class Block:
  '''
    PARAMS:
    * index: the blocks index in the chain
    * transactions: the transactions for this block
  '''
  def __init__(self, index, transactions):
    self.index = index
    self.transactions = transactions
    
    self.id = uuid4()
    self.timestamp = time()
    self.status = BlockStatus()

  def __str__(self) -> str:
    return f'Block: \n Index: {self.index}\n Id: {self.id}\n TimeStamp: {self.timestamp}'
      
  def __bool__(self) -> bool:
    if self.transactions:
      return True
    return False

  def __eq__(self, other):
      return isinstance(other, Block) and self.id == other.id

  def __hash__(self) -> int:
    return hash(self.index, self.id, self.timestamp)

'''
  the current status of the block
  NEW, SIGNED
'''
class BlockStatus:
  def __init__(self):
    self.status = 'NEW'

  def status(self):
    return self.status
  
  def signed(self):
    self.status = 'SIGNED'
