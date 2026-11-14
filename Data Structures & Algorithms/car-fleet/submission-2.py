class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [1, 4] > [4, 6] > [7, 8] > [10, 10] one carFleet
        # [4,1,0,7] > [6, 3, 1, 8] > [8, 5, 2, 9] > [10, 7, 3, 10] 3 carFleet
        # [7, 4, 1, 0] times = [3, 3, 4.5, 10]
        n = len(position)
        times = [0] * n
        for i in range(n):
            times[i] = (target - position[i]) / speed[i]
        
        cars = sorted(zip(position, times), reverse=True)

        position, times = zip(*cars)

        stack = []

        for i in range(0, n):
            if not stack:
                stack.append(times[i])
            elif stack and times[i] > stack[-1]:
                stack.append(times[i])
        return len(stack)

        