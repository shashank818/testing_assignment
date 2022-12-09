class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self._current_speed = 0
        if self.max_speed < 0:
            raise ValueError('Invalid value for max_speed')
        if self.acceleration < 0:
            raise ValueError('Invalid value for acceleration')
        if self.tyre_friction < 0:
            raise ValueError('Invalid value for tyre_friction')

    def start_engine(self):
        self.is_engine_started = True

    def accelerate(self):
        if self.is_engine_started:
            if self._current_speed + self.acceleration <= self.max_speed:
                self._current_speed += self.acceleration
            else:
                self._current_speed = self.max_speed
        else:
            print('Start the engine to accelerate')

    def apply_break(self):
        if self._current_speed - self.tyre_friction < 0:
            self._current_speed = 0
        else:
            self._current_speed -= self.tyre_friction

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
            return "Beep Beep"
        else:
            print("Start the engine to sound_horn")
            return "Start the engine to sound_horn"

    def stop_engine(self):
        self.is_engine_started = False

        # print("Invalid value for max_speed")

    @property
    def current_speed(self):
        return self._current_speed


if __name__ == "__main__":

    obj1 = Car('Black', -6, 30, 34)
    obj1.sound_horn()
    obj1.accelerate()
    obj1.start_engine()
    obj1.accelerate()
    print(obj1.is_engine_started)
    print(obj1.current_speed)
    obj1.start_engine()
    obj1.apply_break()
    # obj1.current_speed = 50
    print(obj1.current_speed)
    print(obj1.is_engine_started)
    obj1.sound_horn()