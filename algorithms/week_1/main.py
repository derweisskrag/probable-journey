"""Entry point"""

from implementation.linked_list import LinkedList, Node

def main():
    """Main function"""
    linked_list = LinkedList(Node(1))
    print(linked_list.has_head())

if __name__ == "__main__":
    main()
