from block import Block 
class Chain:
  def __init__(self, blocks=[], size=0):
    self.size = size
    self.blocks = blocks

  def new_block(self, transactions):
    ind = self.size + 1
    block = Block(ind, transactions)
    
    pass

  def prev_block(self):
    if self.blocks:
      return self.blocks[self.size - 1]
    raise RuntimeError("There must be a block in the chain")
