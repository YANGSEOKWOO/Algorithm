class Node: # not Nxde ㅋㅋ
    def __init__(self, data):
        self.data = data
        self.next = None

# append(노드 끝에 추가)
# print_all (모든 노드 값 출력)
# get_node (인덱스에 있는 노드 알아내기)
# add_node ( 노드 삽입 (위치에))
# delete_node (노드 삭제)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(data)
    
    def print_all(self):
        cur = self.head
        while cur.next != None:
            print(cur.data)
            cur = cur.next
    
    def get_node(self, index):
        cnt = 0
        cur = self.head
        while cnt < index:
            cnt += 1
            cur = cur.next
        return cur
    
    def add_node(self, data, index):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        ex_node = self.get_node(index-1)
        af_node = self.get_node(index)
        ex_node.next = node
        node.next = af_node
    
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next


