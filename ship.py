class Ship:
    def __init__(self, id, length):
        self.id = id
        self.length = length
        self.__hits = 0
        self.__sunken = False
        
        # Start <= end
        self.__start = None # (row, col)
        self.__end = None   # (row, col)

    def hit(self):
        if self.__hits < self.length:
            self.__hits += 1
            if self.__hits == self.length:
                self.__sunken = True

    def sunken(self):
        return self.__sunken
    
    def set_endpoints(self, start, end, board_size):
        """
        start/end: (row, col)
        board_size: (height, width) or (rows, cols)
        """
        
        r1, c1 = start
        r2, c2 = end
        
        # Only allow horizontal or vertical ships
        if r1 == r2: # horizontal
            s = (r1, min(c1, c2))
            e = (r2, max(c1, c2))
        elif c1 == c2: # vertical
            s = (min(r1, r2), c1)
            e = (max(r1, r2), c2)
        else:
            raise ValueError(f"Ship ID: {self.id} must be placed either horizontally or vertically.")
        
        # check ship length
        expected_len = abs(e[0] - s[0]) + abs(e[1] - s[1]) + 1
        if expected_len != self.length:
            raise ValueError(f"Ship ID: {self.id} length mismatch. Expected length: {self.length}, got: {expected_len}.") 
        
        # check if within board boundaries
        board_height, board_width = board_size
        rmin, rmax = 0, board_height - 1
        cmin, cmax = 0, board_width - 1
        
        for (r, c) in (s, e):
            if not ((r >= rmin and r <= rmax) and (c >= cmin and c <= cmax)):
                raise ValueError(f"Ship ID: {self.id} endpoint {r, c} is out of board boundaries {board_size}.")
        
        self.__start = s
        self.__end = e
    
    def get_endpoints(self):
        return (self.__start, self.__end)
    
    def get_orientation(self):
        if self.__start is None or self.__end is None:
            return None
        
        if self.__start[0] == self.__end[0]:
            return 'H' # horizontal
        else:
            return 'V' # vertical
    
    def cells(self):
        """
        Returns a list of (row, col) tuples occupied by the ship.
        """
        if self.__start is None or self.__end is None:
            return []
        
        cells = []
        if self.get_orientation() == 'H':
            r = self.__start[0]
            for c in range(self.__start[1], self.__end[1] + 1):
                cells.append((r, c))
        elif self.get_orientation() == 'V': 
            c = self.__start[1]
            for r in range(self.__start[0], self.__end[0] + 1):
                cells.append((r, c))
        
        return cells
            
        
        