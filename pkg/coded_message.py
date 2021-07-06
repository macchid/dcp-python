from string import ascii_lowercase
import sys

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Decrypter:
    def __init__(self):
        self._root = Node("")
        self._code = list(ascii_lowercase)
        self._clear = []
        self._ciphered = ""

    def decrypt(self, msg):
        if len(msg) > 500:
            sys.setrecursionlimit(10**6)

        self._ciphered = msg
        self._root.left = self._read(msg, 1)
        self._root.right = self._read(msg, 2)

        return self.interpret()


    def _read(self, msg, ce):
        if ce > len(msg):
            return None

        code = int(msg[:ce])
        if code > len(self._code):
            return None

        node = Node(self._decode(code))
        node.left = self._read(msg[ce:], 1)
        node.right = self._read(msg[ce:], 2)

        return node
        
    def _decode(self, code):
        return self._code[int(code)-1]
    
    def _encode(self, clear):
        return self._code.index(clear) + 1

    def interpret(self):
        self._write(self._root, "")
        return self._clear

    def _write(self, node, msg):
        if node.left is None and node.right is None:
            if self._is_complete(msg):
                self._clear.append(msg)
            return 

        if node.left:
            self._write(node.left, msg + node.left.val)
        
        if node.right:
            self._write(node.right, msg + node.right.val)

    def _is_complete(self, msg):
        c = ""
        for a in list(msg):
            c += str(self._encode(a))

        return c == self._ciphered

        

if __name__ == "__main__":
    d = Decrypter()
    print(d.decrypt("111"))



