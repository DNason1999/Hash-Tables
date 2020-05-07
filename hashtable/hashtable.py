class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return (f"(key = {self.key}, value = {self.value})")


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, minimum_size=128):
        self.capacity = capacity
        self.storage = [None] * self.capacity 
        self.minimum_size = minimum_size
        self.size = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        total = 0
        for b in key.encode():
            total += b
            total &= 0xffffffffffffffff
        
        return total

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        total = 0
        for b in key.encode():
            total += b
            total &= 0xffffffff
        
        return total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            self.storage[index] = HashTableEntry(key=key, value=value)
            self.size += 1
        else:
            n = self.storage[index]
            if n.key == key:
                    n.value = value
                    return
            while n.next is not None:
                if n.key == key:
                    n.value = value
                    return
                n = n.next
            
            n.next = HashTableEntry(key=key, value=value)
            self.size += 1

        # Check load factor if greater than 0.7 (70% full)
        if (self.size / self.capacity) <= 0.2:
            # If load factor less than 0.2 and capacity is greater
            # than minimum_size (default 128), half the table size
            if not self.capacity <= self.minimum_size:
                self.resize(multiplier=0.5)
        elif (self.size / self.capacity) >= 0.7:
                # If load factor greater than 0.7, double size
                self.resize(multiplier=2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key=key)
        if self.storage[index] is None:
            return None
        else:
            # previous node
            p = None
            # current node
            n = self.storage[index]
            # while n has a next node
            while n.next is not None:
                # if the current node key is the hashed key we 
                # are looking for, break the while loop
                if n.key == key:
                    if p is None:
                        self.storage[index] = n.next
                    else:
                        p.next = n.next
                    self.size -= 1
                    break
                # else set previous = current node
                # and current node = next node
                else:
                    p = n
                    n = n.next
            
            # If p is not none (i.e. there is more than 1 node in linked list)
            # Set p.next to n.next (skipping n)
            if p is None and n.key == key:
                self.storage[index] = None
                self.size -= 1
        
        if (self.size / self.capacity) <= 0.2:
            # If load factor less than 0.2 and capacity is greater
            # than minimum_size (default 128), halve the table size
            if not self.capacity <= self.minimum_size:
                self.resize(multiplier=0.5)
        elif (self.size / self.capacity) >= 0.7:
                # If load factor greater than 0.7, double size
                self.resize(multiplier=2)

        # return the value from the node when it is found
        return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key=key)
        if self.storage[index] is not None:
            n = self.storage[index]
            while n.next is not None:
                if n.key == key:
                    return n.value
                n = n.next
            return n.value
        
        return None

    def resize(self, multiplier=2):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        key_values = {}
        for head in self.storage:
            if head is None:
                pass
            else:
                n = head
                key_values[n.key] = n.value
                while n.next is not None:
                    key_values[n.key] = n.value
                    n = n.next
        
        new_capacity = int(self.capacity*multiplier)
        t_ht = HashTable(new_capacity)
        for key,value in key_values.items():
            t_ht.put(key, value)
        
        self.capacity = t_ht.capacity
        del(self.storage)
        self.storage = t_ht.storage

if __name__ == "__main__":
    ht = HashTable(2)

    print((len(ht.storage),ht.size, ht.capacity))

    ht.put("line_1", "Tiny hash table")
    print((len(ht.storage),ht.size, ht.capacity, '1'))
    ht.put("line_2", "Filled beyond capacity")
    print((len(ht.storage),ht.size, ht.capacity, '2'))
    ht.put("line_3", "Filled beyond capacity")
    print((len(ht.storage),ht.size, ht.capacity, '3'))
    ht.put("line_4", "Filled beyond capacity")
    print((len(ht.storage),ht.size, ht.capacity, '4'))
    
    print(ht.storage)

    ht.delete("line_1")

    print(ht.storage)
