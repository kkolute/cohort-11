class BinarySearch(list):
    # constructor that creates list of elements
    def __init__(self, a, b, *args):
        # Init list
        list.__init__(self, *args)
        self.list_length = a
        self.step = b
        end = self.list_length * self.step
        for i in range(self.step, end + 1, self.step):
            self.append(i)

    @property
    def length(self):  # returns the length of the list
        return len(self)

    #  binary search algorithm using recursion that returns a dictionary showing index and  loop count
    def search(self, element, bottom=0, top=None, count=0):
        if not top:
            top = self.length - 1
        if element == self[bottom]:
            return {'count': count , 'index': bottom}
        elif element == self[top]:
            return { 'count': count,'index': top}
        mid = (bottom + top) // 2
        if element == self[mid]:
            return { 'count': count ,'index': mid}
        elif element > self[mid]:
            bottom = mid + 1
        elif element < self[mid]:
            top = mid - 1
        if bottom >= top:
            return { 'count': count,'index': -1}
        count += 1
        return self.search(element, bottom, top, count)