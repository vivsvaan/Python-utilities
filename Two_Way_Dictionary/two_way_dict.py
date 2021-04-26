# two_way_dict.py

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
        return self.rev
    
 
