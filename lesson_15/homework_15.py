import pytest


class Rhombus:

    def __init__(self, side_a: int, angle_a: int):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise AttributeError("The side_a should be > 0!")
        if name == "angle_a" and (value >= 180 or value <= 0):
            raise AttributeError("The angle_a should be < 180 or > 0 degrees!")
        super().__setattr__(name, value)

    def angle_a(self) -> int:
        print(f"The angle_a is equal - {self.angle_a} degrees.")
        return self.angle_a

    def angle_b(self) -> int:
        print(f"The angle_b is equal - {self.angle_b} degrees.")
        return self.angle_b


if __name__ == "__main__":
    try:
        figure_1 = Rhombus(10, 170).angle_b
    except AttributeError:
        print("You tried to SET the side_a < 0 or angle_a > 180 or < 0 degrees!")


@pytest.mark.parametrize("side_a,angle_a,expected",
                         [(20, 30, 150),
                          (1, 179, 1),
                          (-2, 55, AttributeError),
                          (12, 181, AttributeError)])
def test_success(side_a, angle_a, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            Rhombus(side_a, angle_a)
    else:
        rhombus = Rhombus(side_a, angle_a)
        result = rhombus.angle_b
        assert result == expected

