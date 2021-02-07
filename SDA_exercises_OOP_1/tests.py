from SDA_exercises_OOP_1.figures import Figure, Triangle, Rectangle, Circle


def test_check_area():
    # given
    figure_1 = Rectangle(2, 2)
    figure_2 = Triangle(2, 1)
    figure_3 = Circle(1)

    # when
    result = Figure.add_areas(figure_1, figure_2, figure_3)

    # then
    assert result == 8.141592653589793
