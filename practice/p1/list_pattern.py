class MyList:

    def __init__(self, *data):
        self.capacity = len(data)
        self._size = self.capacity
        self._data = [None] * self.capacity
        for i in range(self._size):
            self._data[i] = data[i]

    def count(self):
        return self._size

    def get(self, index: int):
        if index >= self._size or index < 0:
            raise IndexError
        return self._data[index]

    def first(self):
        if self._size > 0:
            return self._data[0]
        raise IndexError

    def last(self):
        if self._size > 0:
            return self._data[self._size - 1]
        raise IndexError

    def includes(self, item):
        for i in range(self._size):
            if item == self._data[i]:
                return True, i
        return False, None

    def _up_capacity(self):
        self._data.extend([None] * self.capacity)
        self.capacity *= 2

    def append(self, item):
        if self.capacity == self._size:
            self._up_capacity()
        self._data[self._size + 1] = item
        self._size += 1

    def prepend(self, item):
        if self._size == self.capacity:
            self._up_capacity()
        self._data[1:self._size] = self._data[0:self._size]
        self._data[0] = item
        self._size += 1

    def remove(self, item):
        is_include, idx = self.includes(item)
        if is_include:
            self._data = self._data[0: idx] + self._data[idx + 1: self._size]
            self._size -= 1

    def remove_first(self):
        self.remove(self._data[0])

    def remove_last(self):
        if self._size > 0:
            self._data[self._size - 1] = None
            self._size -= 1

    def remove_all(self):
        self._data = [None] * self.capacity
        self._size = 0

class MyIterator:

    def __init__(self, iter_obj: MyList):
        self._obj = iter_obj
        self._pos = 0
        self._obj_len = self._obj.count()

    def first(self):
        self._pos = 0

    def next(self):
        self._pos += 1

    def is_done(self):
        return self._pos >= self._obj_len

    def cur_item(self):
        if self.is_done():
            raise StopIteration
        else:
            return self._obj.get(self._pos)

    def __iter__(self):
        return self

    def __next__(self):
        item = self.cur_item()
        self.next()
        return item


class MyListIterator(MyList):
    def __iter__(self):
        return iter(MyIterator(self))
