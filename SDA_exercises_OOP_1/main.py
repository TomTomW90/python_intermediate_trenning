from SDA_exercises_OOP_1.cat import Cat


def main():
    cat_instance_1 = Cat("Kicia")
    cat_instance_2 = Cat("Mruczek")
    cat_instance_3 = Cat("Garfield")
    cat_instance_4 = Cat("Tygrys")

    cats = [cat_instance_1, cat_instance_2, cat_instance_3, cat_instance_4]

    for cat in cats:
        print(cat.make_sound())

    cat_instance_1.eat_mouse()
    cat_instance_1.eat_mouse()
    cat_instance_1.count_eaten_mouses()


if __name__ == "__main__":
    main()
