#!/usr/bin/python


# This class creates a Linked List using recursion.  This is not the most efficient
#   way to create a linked list, as each node instantiates the class in it's entirety.
# It would be much more efficient to create a class for data nodes and class for
#   the Linked List, using iterative loops to traverse the list.
# I am creating this class to practice recursion and the Linked List data structure.
#   It is intended for learning purposes;
#       as such, it is commented to the point of being nearly unreadable as code.
#
# To begin using, instantiate the class, supplying the data you want in the first node:
#   myData = "world"
#   myInstance = recursiveLinkedList(myData)
#
# There are two methods for adding data to the list.
#   The first method is push(myData), which adds myData to the beginning of the list:
#       myData = "hello"
#       myInstance.push(myData)
#   This would create the list: "hello", "world"
#
#   The second method is append(myData):
#       myData = "it"
#       myInstance.append(myData)
#   This would create the list: "hello", "world", "it"
#
#   TODO: add methods for "insert_after()" and "insert_befor()"
#
# There are two methods for pulling data off the list.
#   The first method is pop(), which pops the first node off the list:
#       myInstance, popped = myInstance.pop()
#   This sets myInstance to either the Linked List following the first node
#       or to an empty node if there is only one node in the list.
#   It also sets "popped" to equal the data in the first node.
#
#   The second method is pull(), which pulls the last (tail) node off the list:
#       pulled = myInstance.pull()
#   This sets "pulled" to the data in the last (tail) node in the list and
#       sets the pointer to the last (tail) node to the next-to-last node.
#       If there is only one node, it empties the node.
#
#   TODO: add method to yank() an arbitrary node.
#
# There is one method to print the list, but there are two ways to use it.
#   The first method is to printList() without any arguments (or, printList(None) will work)
#       This prints the Linked List in order, first to last.
#   The second method is to printList("backwards") (or use printList(foobar),
#    with foobar being any argument except "None").
#       This prints the Linked List in reverse order, last to first.
#
#   TODO: Create search and sort capabilities, which will help with insert_before,
#       insert_after, and yank methods.

class recursiveLinkedList:

  ## __init__(self,inData) is the initialization routine.
  #     self is passed via python internals, and refers to this instance of the class.
  #     inData is provided by the calling function.
  #     Usage:
  #          myLinkedList = recursiveLinkedList("some data")
  #     Like python, inData is loosely typed.
  # This creates an end or "tail" node.
  # It sets self.data to inData
  # Since it is the tail node, there is no "next" node, so the "next" pointer is set to None.
  # Likewise, the "tail" pointer is set to itself.
  #
  #     I thought about passing a pointer to the first or "head" node, to make this a circular list,
  #         but decided that it was overkill and not necessary for adding or removing nodes
  #         from anywhere in the list.
  #     I also thought about returning self.tail to the calling function, but decided that
  #         it was easier to have the parent node keep track of the tail pointer through
  #         the parent's child node.
  def __init__(self, inData):
      self.data = inData
      self.next = None
      self.tail = self

  ## push(self, inData) is a function to push data onto the beginning of the list.
  #     self is passed via python internals and refers to this instance of the class.
  # This either puts data into the first "head" node (if it's empty) or it
  #     creates a new first "head" node with the old "head" node being the "next" node
  def push(self, inData):
      # if there is not a "next" node, then this is the first "head" node.
      if not self.next:
          # if there is not data, then this node is empty, so
          #   self.data is set to inData.
          # remembering that this is the "head" node, there is no next node.
          # and we set the tail pointer to point to itself.
          # NOTE: the Linked List will only function if it is not intended to hold None
          #   as a data value.  If a data value is set to "None", then the list cannot grow.
          #     If you're learning recursion, ask yourself "why not?"
          # TODO: figure out how to store "none" as a data value.
          if not self.data:
              self.data = inData
              self.next = None
              self.tail = self
          # if there is data, then this node is not empty, so
          #     remembering there is no "next" node,
          #     we create a "next" node with the data which exists in this node.
          #     and then set this node's data to inData
          #     and finally, we point the "tail" to the "tail" of the next node
          #         If you're learning recusrion, ask yourself what the next node's
          #             tail is.
          else:
              self.next = recursiveLinkedList(self.data)
              self.data = inData
              self.tail = self.next.tail
      # if there is a next node, then we need to push everything down
      #     we do this recursively by pushing this node's data onto
      #     the next node.
      #     then we set this node's data to inData.
      #     and finally, we point the "tail" to the next node's "tail"
      #         If you're learning recursion, ask yourself what the next node's
      #             tail is.  How does the next node know which node is the tail?
      else:
          self.next.push(self.data)
          self.data = inData
          self.tail = self.next.tail

  ##  append(self, inData) is a function to append data on the the end of the list.
  #     self is passed via python internals and refers to this instance of the class.
  #  This either sets the data in the "head" node (if it's empty) or it
  #     creates a new "tail" node which becomes the "next" node for the old "tail" node.
  def append(self, inData):
      # if self.tail points to this node, then this node is the "tail"
      #     so we set the "next" pointer to a new node (new instance of the class)
      #          with inData as the data for that new node.
      #     then we set this node's "tail" to point to the new "next" node's "tail"
      #         If you're learning recursion, ask yourself what node self.next.tail
      #             points to.  Where is it set?
      if self.tail == self:
          self.next = recursiveLinkedList(inData)
          self.tail = self.next.tail
      # if self.tail does not point to this node, then we need to pass inData
      #     down to the "next" node, which we do recursively.
      #     then we set this node's tail to then "tail" of the "next" node.
      #         If you're learning recursion, ask yourself what node self.next.tail
      #             points to.  Where is it set?
      else:
          self.next.append(inData)
          self.tail = self.next.tail

  ## pop(self) is a function to pop data off of the top "head" of the list.
  #     self is passed via python internals.
  #  This returns the data from the "head" node (myPop) and:
  #     if there is no "next" node, then it also returns itself as the "head" node.
  #         If you are learning recursion, ask yourself why it returns
  #             itself as the "head" node if there is no "Next" node?
  #             Why is it returning the new "head" node?  To where?
  #     if there is a "next" node:
  #         it also returns the "next" node to be the new "head" node.
  #  Usage:
  #     myNewLinkedList, myPoppedData = myOldLinkedList.pop()
  #     # myNewLinkedList == myOldLinkedList.next is true
  #     # myPoppedData = myOldLinkedList.data
  #  In practice, you would use it this way:
  #     myLinkedList, myPoppedData = myLinkedList.pop()
  #     # myLinkedList is now one node shorter (removed from the top)
  #
  #  If you are learning recursion, ask yourself why this can't be done using recursion in python.
  #     if you can figure out a way to do this recursively in python, by all means teach me.
  def pop(self):
      # if self.data does not exist, then the list is empty (unusable if None is
      #     a potential data point)
      #     we return self to be the new "head" (same as the old "head"), and None
      #         for popped data.
      if not self.data:
          return self, None
      # if self.data exists, then this is the "head" node
      #     If you are learning recursion, ask yourself "why?"
      #         hint: we don't use recursion in this function.
      else:
          # if there is not a "next" node, then this is also the "tail" node
          #     i.e., this is the only node.
          # so we return this node's data (myPop) and then set "data" and "next" to None.
          #     If you are learning recursion, ask yourself "why?"
          # and we set "tail" to "self"  This is probably redundant.  Might ask "why?"
          if not self.next:
              myPop = self.data
              self.data = None
              self.tail = None
              self.next = None
              return self, myPop
          # if there is a "next" node, then this is not the "tail node"
          #     i.e., there is more than one node.
          # so we return this node's data (myPop), set "data" and "tail" to None.
          #     this is redundant, but it's good to clean up a bit.
          # and we return this node's "next" to the calling function.
          #     If you're learning recursion, this is worth tracing back and figuring out why.
          else:
              myPop = self.data
              self.data = None
              self.tail = None
              return self.next, myPop

  ## pull(self) is a function to pull data off the end "tail" of the list.
  #     this returns data off the end end of the list (if the list isn't empty)
  #     the hard part here is moving the "tail" pointer.
  #         If you are learning recursion, try to follow the "tail" pointer through
  #             a list with several nodes.
  def pull(self):
      # if self.data is empty, then the list is empty and we return None.
      if not self.data:
          return None
      # if there is data in this node, then the list is not empty.
      else:
          # if there is not a "next" node, then this is the "tail" node
          #  and we return this node's data (myPull)
          #  we also set "data" and "tail" to None (which isn't necessary, but good to clean up.
          if not self.next:
              myPull = self.data
              self.data = None
              self.tail = None
              return myPull
          # if there is a "next" node, then this is not the tail node, so we return
          #  the output from the recursive use of pull() (myPull).
          else:
              myPull = self.next.pull()
              # if there is no data in the "next" node after pulling from it,
              #  then the "next" node was the tail, so we set "next" to None
              #   and "tail" to this node, making this node the new "tail".
              if not self.next.data:
                  self.next = None
                  self.tail = self
              # if there is data in the next node after pulling from it,
              #  then it was not the "tail" node, so we assume that it points
              #   to the "tail" (eventually), and set this node's "tail" to
              #   self.next.tail
              else:
                  self.tail = self.next.tail

              # don't forget to return myPull!
              return myPull

  ## printList(self, backwards = None) is a function to print the Linked List
  #     recursively either forwards (default) or backwards (if an argument is sent)
  #  This prints the data from each node (presuming the list isn't empty).
  #  This is a good way to see the recursion working.
  def printList(self, backwards = None):
    # if there is no data in this node, the list is empty, tell the user.
    if not self.data:
        print "Empty List"
    # if there is data in this node, and we'll have data to print.
    else:
        # if the backwards flag is None, then we'll print the list in order.
        if not backwards:
            # start by printing this node's data.
            print self.data
            # if there is a "next" node, recursively run printList on the "next" node.
            if self.next:
                self.next.printList()
            # why do we not do anything if there is not a "next" node?
        # if the backwards flag is set (to anything except None), then we'll reverse
        #   the print order.
        else:
            # if there is no "next" node, print this node's data.
            if not self.next:
                print self.data
            # if there is a "next" node, recursively run printList on the "next" node.
            # and then print this node's data.
            #   Ask yourself how this reverses the order.
            else:
                self.next.printList(backwards)
                print self.data

# sample test code.
if __name__ == "__main__":
    print "\n\nPlease enter a number to start a linked list:"
    myInput = input();
    myLL = recursiveLinkedList(myInput)
    myLL.printList()
    print "\n\nAnd another:"
    myInput = input();
    myLL.append(myInput)
    myLL.printList()
    print "\n\nAnd another:"
    myInput = input();
    myLL.append(myInput)
    myLL.printList()
    print "\n\nAnd another:"
    myInput = input();
    myLL.append(myInput)
    print "\n\n\n"
    myLL.printList()
    print "\n\n"

    myLL.printList()
    print "\n\n"
    myLL.printList("true")
    print "\n\n"
    print "\n\nEnter a number to push onto the linked list: "
    myInput = input();
    myLL.push(myInput)
    print "\n\nPushed: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to append to the linked list: "
    myInput = input();
    myLL.append(myInput)
    print "\n\nAppended: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to push onto the linked list: "
    myInput = input();
    myLL.push(myInput)
    print "\n\nPushed: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to append to the linked list: "
    myInput = input();
    myLL.append(myInput)
    print "\n\nAppended: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to push onto the linked list: "
    myInput = input();
    myLL.push(myInput)
    print "\n\nPushed: " + str(myInput) + "\n\n"


    myLL.printList()
    print "\n\n"

    pulled = myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"

    myLL.printList()
    myLL, popped = myLL.pop()
    print "\n\nPopped: " + str(popped) + "\n\n"

    myLL.printList()
    pulled =  myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"

    myLL.printList()
    myLL, popped = myLL.pop()
    print "\n\nPopped: " + str(popped) + "\n\n"

    myLL.printList()
    print "\n\n"
    myLL.printList("true")
    print "\n\n"

    pulled = myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"
    pulled = myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"
    pulled = myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"
    pulled = myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"
    pulled = myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"
    pulled = myLL.pull()
    print "\n\nPulled: " + str(pulled) + "\n\n"
    myLL,popped = myLL.pop()
    print "\n\nPopped: " + str(popped) + "\n\n"

    myLL.printList()
    print "\n\n"
    myLL.printList("true")
    print "\n\n"

    print "\n\nEnter a number to push onto the linked list: "
    myInput = input();
    myLL.push(myInput)
    print "\n\nPushed: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to append to the linked list: "
    myInput = input();
    myLL.append(myInput)
    print "\n\nAppended: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to push onto the linked list: "
    myInput = input();
    myLL.push(myInput)
    print "\n\nPushed: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to append to the linked list: "
    myInput = input();
    myLL.append(myInput)
    print "\n\nAppended: " + str(myInput) + "\n\n"

    myLL.printList()
    print "\n\nEnter a number to push onto the linked list: "
    myInput = input();
    myLL.push(myInput)
    print "\n\nPushed: " + str(myInput) + "\n\n"


    myLL.printList()
    print "\n\n"
