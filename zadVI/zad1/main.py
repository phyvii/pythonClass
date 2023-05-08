
class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = ""
        current = self.head
        while current:
            elements += str(current.data)+" - "
            current = current.nextE

        return elements

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        if not self.head:
            return None

        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return None

        current = self.head
        while current.nextE:
            if current.nextE.data == e:
                current.nextE = current.nextE.nextE
                self.size -= 1
                if not current.nextE:
                    self.tail = current
                return
            current = current.nextE

    def append(self, e):
        new = Element(e)


        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            current = self.head
            previous = None

            while current is not None and current.data <= e:
                previous = current
                current = current.nextE

            if previous is None:
                self.head = new
                new.nextE = current
            else:
                previous.nextE = new
                new.nextE = current

            # If the new element is added at the end, set it as the new tail
            if current is None:
                self.tail = new

        self.size += 1


lista = MyLinkedList()


lista.append(5)
lista.append(2)
lista.append(7)
lista.append(1)
lista.append(9)

print(lista)

element = lista.get(5)

print(element.data)

lista.delete(2)

print(lista)

print(lista.get(1).data)
