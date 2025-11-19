import random
import os
import time

possibilities = [-1, 0, 1]

class Point:
    def __init__(self, x, y, marker="*"):
        self.x = x
        self.y = y
        self.marker = marker

    def move(self, max_x, max_y):
        x_new = self.x + random.choice(possibilities)
        y_new = self.y + random.choice(possibilities)

        self.x = min(max_x - 1, max(0, x_new))
        self.y = min(max_y - 1, max(0, y_new))

class Grid:
    def __init__(self, width=0, height=0, points=None):
        if points is None:
            points = []
        self.width = width
        self.height = height
        self.points = points

    def add_points(self, point):
        self.points.append(point)

    def display_grid(self):
        print(" " + "_" * self.width)
        for y in range(self.height):
            print("|", end="")
            for x in range(self.width):
                marker = " "
                for p in self.points:
                    if p.x == x and p.y == y:
                        marker = p.marker
                        break
                print(marker, end="")
            print("|")
        print(" " + "‾" * self.width)

G1 = Grid(10, 10)

p1 = Point(3, 5, "A")
p2 = Point(6, 2, "B")

G1.add_points(p1)
G1.add_points(p2)

while True:
    os.system("cls" if os.name == "nt" else "clear") 
    G1.display_grid()

    p1.move(G1.width, G1.height)
    p2.move(G1.width, G1.height)

    time.sleep(0.6)