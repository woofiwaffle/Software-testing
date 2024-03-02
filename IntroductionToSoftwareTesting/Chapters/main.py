class MyList(list):
    def __init__(self):
        super(MyList, self).__init__()

    def __str__(self):
        return ";".join(list(map(str, self)))

    def __len__(self):
        return len(list(filter(lambda i: 1 % 2, self)))

    def append(self, item):
        if type(item) is int:
            super().append(item)
        else:
            raise TypeError("Unsupported list")

L = MyList()
L.append(1)
L.append(2)
L.append(3)
L.append(5)
print(L)
print(len(L))
try:
  L.append([1, 2, 3])
  print(L)
except TypeError as error:
  print(error)