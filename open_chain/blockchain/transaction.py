from uuid import uuid4

class Transaction:
  def __init__(self, trans_type, item, amount):
    self.id = uuid4()
    self.trans_type = TransactionType(trans_type)
    self.item = item
    self.amount = amount

  def to_str(self):
    return f"{self.id}|{self.trans_type}|{self.item}|{self.amount}"

  def to_dict(self):
    return {
      "id": self.id,
      "trans_type": self.trans_type,
      "item": self.item,
      "amount": self.amount
    }
  
# can be in or out
class TransactionType:
  def __init__(self, trans_type):
    pass
  
  
  