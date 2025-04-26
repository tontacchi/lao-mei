class Point:
    '''
    a vertical & horizontal offset from the upper-left corner of the screen
    - x -> horizontal pixel offset
    - y -> vertical pixel offset
    '''
    def __init__(self, x: int=0, y: int=0) -> None:
        '''
        - x -> horizontal pixel offset
        - y -> vertical pixel offset
        '''
        self.x = x
        self.y = y
