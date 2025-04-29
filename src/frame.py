class Frame:
    def __init__(self, curr: tuple[int, int], parent: tuple[int, int], deadend: bool=False):
        self.coords = curr
        self.parent_coords = parent
        self.deadend = deadend
