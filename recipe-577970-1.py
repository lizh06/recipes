class LRU_Cache:

    def __init__(self, original_function, maxsize=1000):
        self.original_function = original_function
        self.maxsize = maxsize
        self.mapping = {}
        self.root = []
        self.root[:] = self.root, self.root, None, None

    def __call__(self, *key):
        PREV, NEXT = 0, 1
        mapping, root = self.mapping, self.root

        link = mapping.get(key, root)
        if link is root:
            value = self.original_function(*key)
            if len(mapping) >= self.maxsize:
                old_prev, old_next, old_key, old_value = root[NEXT]
                root[NEXT] = old_next
                old_next[PREV] = root
                del mapping[old_key]
            last = root[PREV]
            link = [last, root, key, value]
            mapping[key] = last[NEXT] = root[PREV] = link
        else:
            link_prev, link_next, key, value = link
            link_prev[NEXT] = link_next
            link_next[PREV] = link_prev
            last = root[PREV]
            last[NEXT] = root[PREV] = link
            link[PREV] = last
            link[NEXT] = root
        return value


if __name__ == '__main__':
    p = LRU_Cache(pow, maxsize=3)
    for i in [1,2,3,4,5,3,1,5,1,1]:
        print(i, p(i, 2))
