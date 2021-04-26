# two_way_dict.py

# can inherit from [InsensitiveDict]()
# class TwoWayDict(InsensitiveDict):
# in __init__, self.rev = InsensitiveDict()


class TwoWayDict:
    def __init__(self, mappings):
        self.rev = {}
        for key, val in mappings.items():
            self[key] = val
            self.rev[val] = key
    
 

        
        
