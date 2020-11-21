class BinaryTree:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def insert_left(self, val):
    if self.left == None:
      self.left == BinaryTree(val)
    else:
      new = BinaryTree(val)
      new.left = self.left 
      self.left = new


t = BinaryTree('a')
