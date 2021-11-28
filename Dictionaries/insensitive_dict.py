class InsensitiveDict(dict):
    """
    A Subclass of dictionary and compares key in a case insensitive fashion
    """

    def __setitem__(self, key, value):
        try:
            super().__setitem__(key.lower(), value)
        except AttributeError:
            super().setitem__(key, value)\
    
    def __getitem__(self, key):
        try:
            return super().__getitem__(key.lower())
        except AttributeError:
            return super().__getitem__(key)
 
