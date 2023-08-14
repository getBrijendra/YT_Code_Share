
class ListNode:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

	def IterativeReverseList(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def Push(self, d):
		new_ListNode = ListNode(d)
		new_ListNode.next = self.head
		self.head = new_ListNode

	def Display(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.Push(20)
    ll.Push(4)
    ll.Push(15)
    ll.Push(85)

    print ("Initial List: ")
    ll.Display()
    ll.ReverseList()
    print ("\n\nReversed Linked List")
    ll.Display()
