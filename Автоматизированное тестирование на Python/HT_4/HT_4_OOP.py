
class Auto:
    color = 'red'
    type_fuel = '-'
    year_of_issue = '0000'

    def __init__(self, transmision):
        self.transmision = transmision
    #     self.type_fuel = type_fuel
    #     self.year_of_issue = year_of_issue

    def drive(self):
        speed_1 = 40
        speed_2 = 50
        speed_3 = 60

if __name__ == '__main__':

    firs_auto = Auto('manual')
    firs_auto.color = 'green'
    firs_auto.type_fuel= 'diesel'
    print(firs_auto.color)

    second_auto = Auto('automated')
    print(second_auto.color)






