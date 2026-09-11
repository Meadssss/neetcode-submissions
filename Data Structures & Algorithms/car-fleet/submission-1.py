class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p, (target - p) / s))

        cars.sort()

        fleets = 0
        time = 0

        for _, t in reversed(cars):
            if t > time:
                fleets += 1
                time = t
        return fleets