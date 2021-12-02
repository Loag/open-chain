from block import Block, Genesis

class Chain:
  def __init__(self, blocks=[]):
    self.blocks = blocks

  @property
  def size(self):
    return len(self.blocks)

  @property
  def last_block(self):
    if self.blocks:
      return self.blocks[self.size - 1]
    raise RuntimeError("There must be a block in the chain")

  @property
  def genesis_block(self):
    if self.blocks:
      return self.blocks[0]
    raise RuntimeError("There must be a block in the chain")

  def __instantiate(self):
    genesis = Genesis()

  # add a new block to the chain
  def new_block(self, transactions):
    ind = self.size + 1
    block = Block(ind, transactions)
    pass

  '''
    how is a block added to a chain?
  '''
  #TODO need to think about how this is going to work
  def __add_block(self):
    
    return self.size

    
