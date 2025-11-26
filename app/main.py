from __future__ import annotations


class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> None | int:
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self,
                 name: str,
                 is_hungry:
                 bool = True) -> None:
        super().__init__(name,
                         3,
                         is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 is_hungry:
                 bool = True) -> None:
        super().__init__(name,
                         7,
                         is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(list_animals: list) -> int:
    feed_count = 0
    for animal in list_animals:
        feed_count += animal.feed()
    return feed_count
