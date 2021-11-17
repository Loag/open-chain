from uuid import uuid4

class Transaction:
  def __init__(self, user, trans_type, item, amount):
    self.id = uuid4()
    self.user = user # who cerated the transaction
    self.trans_type = TransactionType(trans_type)
    self.state = TransactionState()
    self.item = item
    self.amount = amount

  # if the transaction was 
  def cleared(self):
    self.state.cleared()

  def to_str(self):
    return f"{self.id}|{self.trans_type}|{self.item}|{self.amount}"

  def to_dict(self):
    return {
      "id": self.id,
      "trans_type": self.trans_type,
      "item": self.item,
      "amount": self.amount
    }
  
# the type of 
class TransactionType:
  def __init__(self, trans_type):
    pass

# the state of the transaction
class TransactionState:
  class NEW_STATE:
    def __init__(self) -> None:
        pass
    def is_valid(self):
      return False

  class ACCEPTED_STATE:
    def __init__(self) -> None:
        pass

    def is_valid(self):
      return True

  def __init__(self, transaction):
    self.state = self.NEW_STATE()
    pass
  
  def cleared(self):
    self.state = self.ACCEPTED_STATE()
  
  
  