from tree import Node

class KnightPathFinder:
    def __init__(self, root):
        self._root = Node(root)
        self._considered_positions = set(root) 
        
    
    def get_valid_moves(self, pos):
        possible_moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]
    # for i in range(-2, 3):
    #     if i is not 0:
    #         for j in range( i - -2, 3):
    #             if j is not 0:
    #                 print(i, j)
    # -2 1
    # -2 2
    # -1 1
    # -1 2
        moves = []
        root_x, root_y = pos
        for x,y in possible_moves:
            new_pos = (root_x + x, root_y + y)
            new_x, new_y = new_pos
            if new_x in range(0, 8) and new_y in range(0, 8):
                moves.append(new_pos)
        return moves
        # return [move for move in possible_moves if (7 >= pos)]
        
    
    def new_move_positions(self, pos):
        filtered_moves = self.get_valid_moves(pos)
        new_position = {(pos[0] + mv[0], pos[1] + mv[1]) for mv in filtered_moves}
        possible_new_possition = new_position - self._considered_positions
        self._considered_positions = new_position | self._considered_positions # or .union()
        
        return possible_new_possition
    
    
    
finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))
