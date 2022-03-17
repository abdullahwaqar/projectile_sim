from math import sin, cos, radians
from matplotlib import pyplot as plt


class Projectile:
    def __init__(self, x, y, velocity, angle):
        """
        * x and y are initial coordinates of the cannon
        * velocity is the initial velocity
        * angle is the angle of shooting in degrees
        """
        # * Current x and y coordinates of the projectile
        self.x = x
        self.y = y

        # * Current value of velocity components
        self.vx = velocity * cos(radians(angle))
        self.vy = velocity * sin(radians(angle))

        # * Acceleration by x and y axes
        self.ax = 0
        self.ay = -9.8  # constant, thanks gravity
        # * Flight start time
        self.time = 0

        # * These list will contain discrete set of projectile coordinates
        self.xarr = [self.x]
        self.yarr = [self.y]

    def update_vx(self, dt):
        self.vx = self.vx + self.ax * dt
        print(f'Updated velocity on x axis: {self.vx}')
        return self.vx

    def update_vy(self, dt):
        self.vy = self.vy + self.ay * dt
        print(f'Updated velocity on y axis: {self.vy}')
        return self.vy

    def update_x(self, dt):
        self.x = self.x + 0.5 * (self.vx + self.update_vx(dt)) * dt
        print(f'Current x coordinate: {self.x}')
        return self.x

    def update_y(self, dt):
        self.y = self.y + 0.5 * (self.vy + self.update_vy(dt)) * dt
        print(f'Current y coordinate: {self.y}')
        return self.y

    def step(self, dt):
        self.xarr.append(self.update_x(dt))
        self.yarr.append(self.update_y(dt))
        self.time = self.time + dt


def init_flight(x, y, velocity, angle):
    """
    * Returns a tuple with sequential pairs of x and y coordinates
    """
    projectile = Projectile(x, y, velocity, angle)
    # * Time step, position update time
    time_delta = 0.01
    # * Initial time
    t = 0
    projectile.step(time_delta)

    # * Step until the object hits the ground
    while projectile.y >= 0:
        projectile.step(time_delta)
        t = t + time_delta

    return (projectile.xarr, projectile.yarr)


if __name__ == '__main__':
    x60, y60 = init_flight(0, 0, 10, 60)
    x_buff = []
    y_buff = []

    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')

    for x, y in zip(x60, y60):
        x_buff.append(x)
        y_buff.append(y)
        plt.plot(
            x_buff,
            y_buff,
            'g-',
            [0, 12],
            [0, 0],
            'k-'  # ground,
        )

        plt.pause(0.0001)

    plt.show()
    plt.close()
