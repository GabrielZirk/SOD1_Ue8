import abc
from typing import Dict

class RealEstate(abc.ABC):
    def __init__(self, square_meter: float):
        self.__square_meter = square_meter

    @property
    def square_meter(self):
        return self.__square_meter

    @square_meter.setter
    def square_meter(self, value):
        self.__square_meter = value

    @abc.abstractmethod
    def calc_lease(self) -> float:
        pass

    def category(self) -> int:
        return self.__square_meter/10

    def __repr__(self):
        return f"I'm the Superclass: {__class__.__name__}."


class Office(RealEstate):
    def __init__(self, square_meter: float, people: int):
        super().__init__(square_meter)
        self.__square_meter = square_meter
        self.__people = people

    def __repr__(self):
        return f"Real Estate Type: {__class__.__name__}, People: {self.__people}"

    def calc_lease(self) -> float:
        if self.__people < 50:
            return self.square_meter * 8
        elif self.__people >= 50 and self.__people < 100:
            return self.square_meter * 8.2 + 90
        elif self.__people >= 100:
            return self.square_meter * 8.5 + self.__people


class Flat(RealEstate):
    def __init__(self, square_meter: float, count_room: int, type: str):
        super().__init__(square_meter)
        self.__square_meter = square_meter
        self.__count_room = count_room
        allowed_flattypes = ["High", "Standard", "Low"]
        if type in allowed_flattypes:
            self.__type = type
        else:
            raise ValueError("Flat type must be: High, Standard or Low")

    def __repr__(self):
        return f"Real Estate Type: {__class__.__name__}, Room #: {self.__count_room}, Flat type: {self.__type}"

    def calc_lease(self) -> float:
        if self.__type == "Low":
            return self.square_meter * 7
        elif self.__type == "Standard":
            return self.square_meter * 7.5 + self.__count_room * 10
        elif self.__type == "High":
            return self.square_meter * 8 + self.__count_room * 12

class House(RealEstate):
    def __init__(self, square_meter: float, garden: bool):
        super().__init__(square_meter)
        self.__garden = garden

    def __repr__(self):
        return f"Real Estate Type: {__class__.__name__}, garden: {self.__garden}"

    def calc_lease(self) -> float:
        rent = 0
        if self.__garden:
            rent = self.square_meter * 10 + 200
        else:
            rent =  self.square_meter * 15

        if rent < 1000:
            return 1000
        else:
            return rent

class Accounting:
    def __init__(self):
        self.__real_estates = []

    def add(self, re: RealEstate):
        self.__real_estates.append(re)
        print(f"Added {re}.")

    def print_all(self):
        for i in self.__real_estates:
            print(f"{i}, m2: {i.square_meter}")

    def get_overall_lease(self) -> float:
        total_lease = 0
        for i in self.__real_estates:
            #print(i.calc_lease())
            total_lease += i.calc_lease()
            #print(total_lease)
        return total_lease

    def get_real_estate_in_category(self) -> Dict[str, int]:
        re_dict = dict()
        for i in self.__real_estates:
            print(i.__class__.__name__)
            if i.__class__.__name__ in re_dict.keys():
                re_dict[i.__class__.__name__] += 1
            else:
                re_dict[i.__class__.__name__] = 1
        return re_dict


if __name__ == '__main__':
    office1 = Office(100, 80)
    # print(office1)
    # print(office1.calc_lease())

    flat1 = Flat(80, 3, "High")
    # print(flat1)
    # print(flat1.calc_lease())

    house1 = House(150, True)
    # print(house1)
    # print(house1.calc_lease())
    # print(house1.square_meter)
    # print(house1.calc_lease())
    house2 = House(130, True)

    Acc1 = Accounting()
    Acc1.add(office1)
    Acc1.add(flat1)
    Acc1.add(house1)
    Acc1.add(house2)
    #Acc1.print_all()
    #print(Acc1.get_overall_lease())
    print(Acc1.get_real_estate_in_category())