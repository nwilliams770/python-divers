class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        busy_students = 0
        for i in range(len(startTime)):
            if startTime[i] < queryTime and endTime[i] > queryTime:
                busy_students += 1
        return busy_students
# time-complexity: O(n)
# local variable space: O(1) (constant)