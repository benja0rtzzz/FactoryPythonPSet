from abc import ABC, abstractmethod

# ---------- Super Classes ----------- #
class Factory(ABC):
    @abstractmethod
    def printInfo(self):
        pass

    @abstractmethod
    def getWorkers(self):
        pass

    @abstractmethod
    def startProduction(self):
        pass

class Employee(ABC):
    @abstractmethod
    def introduce(self):
        pass
    
    @abstractmethod
    def work(self):
        pass
    

# ---------- Classes ----------- #
class Engineer(Employee):
    def introduce(self):
        print("Im an engineer")

    def work(self):
        return("Engineering !")

class Supervisor(Employee):
    def introduce(self):
        print("Im a supervisor")

    def work(self):
        return("Supervising !")


class ColorTechnician(Employee):
    def introduce(self):
        print("Im a color tech")

    def work(self):
        return("Painting !")


class Intern(Employee):
    def introduce(self):
        print("Im an intern")

    def work(self):
        return("Trust me pls !")


class PorscheFactory(Factory):
    def printInfo(self):
        print("Welcome to the Porsche Factory !")

    def getWorkers(self):
        return [
            Engineer(),
            Supervisor(),
            ColorTechnician()
        ]
    
    def startProduction(self):
        print("Starting production of the Porsche 911 !")


class LaptopFactory(Factory):

    def printInfo(self):
        print("Welcome to the Laptop Factory !")

    def getWorkers(self):
        return [
            Engineer(),
            Supervisor(),
            Intern()
        ]
    
    def startProduction(self):
        print("Starting production of the MacBook Air M3 !")


def main():
    # ----------------------------------- #
    appleFactory = LaptopFactory()
    appleFactory.printInfo()
    for employee in appleFactory.getWorkers():
        employee.introduce()
        print("My role is: " + employee.work())

    appleFactory.startProduction()

    print("---------------------")

    carFactory = PorscheFactory()
    carFactory.printInfo()
    for employee in carFactory.getWorkers():
        employee.introduce()
        print("My role is: " + employee.work())

    carFactory.startProduction()

    print("---------------------")


    # ----------------------------------- #

# ---------- Main ----------- #
main()
