class Apple(object):

    def get_apple(self):
        return "apple"

    def get_apple1(self,one_letter):
        return str(one_letter) + "pple"


class Summing(object):

    def sum_of_num(self, numbers=[]):
        sum_of_all_numbers = 0
        for number in numbers:
            sum_of_all_numbers += number
        return sum_of_all_numbers