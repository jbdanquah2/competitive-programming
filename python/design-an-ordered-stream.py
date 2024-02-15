class OrderedStream(object):

    def __init__(self, n: int):
        """
        :type n: int
        """

        self.stream = [None] * (n + 1)
        self.pointer = 1
        

    def insert(self, idKey: int, value: str) -> list[str]:
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """

        self.stream[idKey] = value

        if idKey != self.pointer:
            return []
        else:
            chunk = []

            while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:

                chunk.append(self.stream[self.pointer])
                self.pointer += 1

            return chunk
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
        