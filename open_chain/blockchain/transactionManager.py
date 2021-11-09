# this will take in new transactions and send them t

MAX_BLOCK_SIZE = 100

class TransactionManager:
  def __init__(self):
    self.size = 0
    self.transactions = []

  def add_transaction(self, transaction):
    self.transactions.append(transaction)
    self.size += 1

  def check_under_threshold(self):
    return self.size <= MAX_BLOCK_SIZE

  def cut_trans(self):
    try:
      transactions = self.transactions[0:MAX_BLOCK_SIZE]
      self.size -= MAX_BLOCK_SIZE
      return transactions

    except IndexError as err:
      raise RuntimeError from err
