class Board:
    def __init__(self, width, height):
        # Set maximum value to limit the board size, preventing memory crashes
        self.__maximum_width = 15
        self.__maximum_height = 15
        
        if width > self.__maximum_width or height > self.__maximum_height:
            raise ValueError(f"Board size exceeds maximum allowed dimensions of {self.__maximum_width}x{self.__maximum_height}.")
        
        self.width = width  # number of columns
        self.height = height # number of rows
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]


class ShipBoard(Board):
    """
    This board is used for placing and tracking ships.
    """
    pass


class BattleBoard(Board):
    """
    This board records the player's hits and misses against the opponent.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        self.miss_list = []  # List of (row, col) tuples for misses
        self.hit_list = []   # List of (row, col) tuples for hits
        
    def __isValidCoordinate(self, row, col):
        if row >= 0 and row < self.height and col >= 0 and col < self.width:
            return True
        return False

    def mark_hit(self, row, col):
        if self.__isValidCoordinate(row, col):
            self.grid[row][col] = 'x'  # Mark hit with 'x'
            self.hit_list.append((row, col))
        else:
            raise ValueError(f"Coordinates ({row}, {col}) out of bounds")

    def mark_miss(self, row, col):
        if self.__isValidCoordinate(row, col):
            self.grid[row][col] = 'm'  # Mark miss with 'm'
            self.miss_list.append((row, col))
        else:
            raise ValueError(f"Coordinates ({row}, {col}) out of bounds")




    