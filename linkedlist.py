class node:
  def __init__(self, data):
    self.data = data
    self.next = None
class linkedlist:
  def __init__(self):
    self.head = None
  def display(self):
    temp=self.head
    while temp:
      result.append(temp.data)
      temp=temp.next
    print(result)