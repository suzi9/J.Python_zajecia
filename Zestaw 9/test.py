from singlelist import *
import unittest

class TestSingleList(unittest.TestCase):
    def test__inserthead__(self):
        lista = SingleList()
        lista.insert_head(Node(4))
        lista.insert_head(Node(5))
        lista.insert_head(Node(7))
     
        self.assertEqual(lista.head.data, 7)
        self.assertEqual(lista.head.next.data, 5)
        self.assertEqual(lista.head.next.next.data, 4)
        self.assertEqual(lista.tail.data, 4)
        self.assertEqual(lista.tail.next, None)
        self.assertEqual(lista.length, 3)

    def test__inserttail__(self):
        lista = SingleList()
        lista.insert_tail(Node(23))
        lista.insert_tail(Node(24))
        lista.insert_tail(Node(25))

        self.assertEqual(lista.head.data, 23)
        self.assertEqual(lista.head.next.data, 24)
        self.assertEqual(lista.head.next.next.data, 25)
        self.assertEqual(lista.tail.data, 25)
        self.assertEqual(lista.tail.next, None)
        self.assertEqual(lista.length, 3)

    def test__removehead__(self):
        lista = SingleList()
        lista.insert_head(Node(2))
        lista.insert_head(Node(6))
        lista.insert_head(Node(10))

        self.assertEqual(lista.remove_head().data, 10)
        self.assertEqual(lista.length, 2)
        self.assertEqual(lista.remove_head().data, 6)
        self.assertEqual(lista.length, 1)
        self.assertEqual(lista.remove_head().data, 2)
        self.assertEqual(lista.head, None)
        self.assertEqual(lista.tail, None)
        self.assertEqual(lista.length, 0)
        with self.assertRaises(ValueError):
            lista.remove_head()

    def test__removetail__(self):
        lista = SingleList()
        lista.insert_head(Node(3))
        lista.insert_head(Node(33))
        lista.insert_head(Node(333))

        self.assertEqual(lista.remove_tail().data, 3)
        self.assertEqual(lista.length, 2)
        self.assertEqual(lista.remove_tail().data, 33)
        self.assertEqual(lista.length, 1)
        self.assertEqual(lista.remove_tail().data, 333)
        self.assertEqual(lista.head, None)
        self.assertEqual(lista.tail, None)
        self.assertEqual(lista.length, 0)
        with self.assertRaises(ValueError):
            lista.remove_tail()

    def test__join__(self):
        lista1 = SingleList()
        lista1.insert_head(Node(4))
        lista1.insert_head(Node(9))
        lista1.insert_head(Node(11))

        lista2 = SingleList()
        lista2.insert_head(Node(10))
        lista2.insert_head(Node(33))
        lista2.insert_head(Node(2))

        lista1.join(lista2)

        self.assertEqual(lista1.head.data, 11)
        self.assertEqual(lista1.head.next.data, 9)
        self.assertEqual(lista1.head.next.next.data, 4)
        self.assertEqual(lista1.tail.data, 10)
        self.assertEqual(lista1.tail.next, None)
        self.assertEqual(lista1.length, 6)
        self.assertEqual(lista2.head, None)
        self.assertEqual(lista2.tail, None)
        self.assertEqual(lista2.length, 0)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy