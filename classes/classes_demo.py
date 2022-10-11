
class LruCacheDemo:
    """
        Implementation of LRU cache without using any in-build module
    """
    def __init__(self, capacity: int):
        self.lru_queue = []
        self.lru_dict = {}
        self.lru_capacity = capacity

    def pop_first_element(self) -> int:
        return self.lru_queue.pop(0)

    def pop_given_element(self, key: int) -> None:
        self.lru_queue.remove(key)

    def re_balance_queue(self, key: int) -> None:
        self.pop_given_element(key)
        self.lru_queue.append(key)

    def get(self, key: int) -> int:
        if key in self.lru_dict:
            ret_val = self.lru_dict.get(key)
            self.re_balance_queue(key)
            return ret_val
        return -1

    def append_element(self, key: int):
        self.lru_queue.append(key)

    def put(self, key: int, value: int) -> None:
        if key not in self.lru_dict:
            if len(self.lru_queue) == self.lru_capacity:
                evicted_elem = self.pop_first_element()
                del self.lru_dict[evicted_elem]
            self.append_element(key)
            self.lru_dict[key] = value
        else:
            self.re_balance_queue(key)
            self.lru_dict[key] = value




c = 2
obj = LruCacheDemo(c)

ops = ["put","put","get","put","get","put","get","get","get"]
values = [[1, 0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

result = []

for i in range(len(ops)):
    x = values[i]
    if ops[i] == "put":
        obj.put(x[0], x[1])
        result.append(None)
    else:
        re = obj.get(x[0])
        result.append(re)

print(result)