class Room:
    _exits = []
    _objects = []
    _characters = []
    _name = ""
    _description = ""
    
    def __init__(self, name, description):
        self._name = name
        self._description = description
    