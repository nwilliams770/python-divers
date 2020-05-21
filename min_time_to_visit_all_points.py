class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#      get our start and end points, points[i] + points[i + 1]
#      traversing:
#           if we can move diagnoally, do so
#           otherwise move vertical or horizontal
        traversal_time = 0

        for i in range(len(points) - 1):
            print(self.get_min_traversal(points[i], points[i + 1]))
            traversal_time += self.get_min_traversal(points[i], points[i + 1])

        return traversal_time




    def get_min_traversal(self, point1: List[int], point2: List[int]) -> int:
        start_x, start_y = point1[0], point1[1]
        end_x, end_y = point2[0], point2[1]

        dx = -1 if start_x > end_x else 1
        dy = -1 if start_y > end_y else 1

        traversal_time = 0

        while not self.is_at_target(start_x, start_y, end_x, end_y):
            if self.can_move_diagonal(start_x, start_y, end_x, end_y):
                start_x += dx
                start_y += dy
                traversal_time += 1

            elif self.can_move_horizontal(start_x, end_x):
                start_x += dx
                traversal_time += 1

            elif self.can_move_vertical(start_y, end_y):
                start_y += dy
                traversal_time += 1

        return traversal_time


    def is_at_target(self, x1, y1, x2, y2):
        return x1 == x2 and y1 == y2

    def can_move_diagonal(self, x1: int, y1: int, x2: int, y2: int) -> bool:
#         We can move diagonal ONLY IF both coordinates are not on the same coordinate line as target
        return x1 != x2 and y1 != y2

    def can_move_horizontal(self, x1: int, x2: int) -> bool:
        return x1 != x2

    def can_move_vertical(self, y1: int, y2: int) -> bool:
        return y1 != y2