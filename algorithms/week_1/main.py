"""The entry point"""

from implementation.linked_list import LinkedList, Node

def main():
    """The main function"""
    linked_list = LinkedList(Node(2))
    print(linked_list.has_head())

if __name__ == "__main__":
    main()
