from SDA_exercises_OOP_1.cat import Cat
from SDA_exercises_OOP_1.dog import Dog
import SDA_exercises_OOP_1.figures as fig


def animals():
    cat_instance_1 = Cat("Kicia")
    cat_instance_2 = Cat("Mruczek")
    cat_instance_3 = Cat("Garfield")
    cat_instance_4 = Cat("Tygrys")
    dog_instance_1 = Dog("Łajka")
    dog_instance_2 = Dog("Perszing")
    dog_instance_3 = Dog("Bruno")

    animals_list = [cat_instance_1, cat_instance_2, cat_instance_3, cat_instance_4, dog_instance_1, dog_instance_2, dog_instance_3]

    for animal in animals_list:
        print(animal.make_sound())

    cat_instance_1.eat_mouse()
    cat_instance_1.eat_mouse()
    cat_instance_1.count_eaten_mouses()
    cat_instance_1.move()


def figures():

    figure_1 = fig.Rectangle(2, 3)
    figure_2 = fig.Rectangle(4, 5)
    figure_3 = fig.Triangle(5, 3)
    figure_4 = fig.Circle(10)

    print(figure_1.get_area())
    print(figure_2.get_area())
    print(figure_3.get_area())
    print(figure_4.get_area())
    print()

    print(fig.Figure.add_areas(figure_1, figure_2, figure_3, figure_4))
    print()

    print(fig.Figure.check_if_there_is_enough_paint(300, figure_1, figure_2, figure_3, figure_4))
    print(fig.Figure.check_if_there_is_enough_paint(350, figure_1, figure_2, figure_3, figure_4))


if __name__ == "__main__":
    figures()
