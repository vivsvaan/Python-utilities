# reverse_dictionary.py

# can inherit from [InsensitiveDict]()
# class ReverseDict(InsensitiveDict):
# in __init__, self.rev = InsensitiveDict()


class ReverseDict(dict):
    def __init__(self, mappings):
        self.rev = {}
        for key, val in mappings.items():
            self[key] = val
            self.rev[val] = key
    

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.rev.__setitem__(value, key)
    
    def __delitem__(self, key):
        super().__delitem__(self.__getitem__(key))
        self.rev.__delitem__(key)
    
    def __getitem__(self, key):
        try:
            return super.__getitem__(key)
        except KeyError:
            return self.rev.__getitem__(key)
    
    def get_reverse_dict(self):
        """
        Returns the reversed dictionary
        """
        return self.rev
    
    def get_two_way_dict(self):
        """
        Returns the two-way dictionary by appending
        the normal dictionary with reversed dictionary
        """
        two_way_dict = {}
        two_way_dict.update(self)
        two_way_dict.update(self.rev)
        return two_way_dict
    
 
normal_dict = ReverseDict({'a':'b', 'c':'d'})
print("Normal Dict is: ", normal_dict)

reverse_dict = normal_dict.get_reverse_dict()
print("Reversed Dict is: ", reverse_dict)

two_way_dict = normal_dict.get_two_way_dict()
print("Two-way Dict is: ", two_way_dict)


"""
Output
Normal Dict is:  {'a': 'b', 'c': 'd'}
Reversed Dict is:  {'b': 'a', 'd': 'c'}
Two-way Dict is:  {'a': 'b', 'c': 'd', 'b': 'a', 'd': 'c'}
"""


