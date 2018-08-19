from utils import *
from binarysearch import *
from quickSort import *


Queue = struct_type("Queue",
           (int, 'size'),
           ((NoneType, Node), 'front'), ((NoneType, Node), 'back'))

CountryValue = struct_type("CountryValue", (str, "country"), (float, "value"))


def sorted_ranking_data(data, year):
    '''
    this function ranks countries by their life expectancy for a
        particular year
    :param data: the data structure returned by read_data function
    :param year: the year in which the countries would be ranked
    :return: a list of data structure Country value which is sorted in descending order
    '''
    n=deep_copy(data)
    list = []
    while n.front !=  None or n.back !=  None:
        o = binary_search(data.front.value.Years, year, 0, len(n.front.value.Years)-1)
        if data.front.value.LE[o] == "":
            dequeue(n)
        else:
            list.append(CountryValue(n.front.value.name, n.front.value.LE[o]))
            dequeue(n)
    a = quickSort(list)
    print(a)
    print(len(a))
    return a



def main():
    '''
    Performs the stand alone behaviors of the program by calling other functions
    '''
    f = "worldbank_life_expectancy"
    x = read_data(f)
    print(sorted_ranking_data(filter_region(x, "Middle East & North Africa"),1965))
    while f != '':
        print("")
        year = int(input("Enter year of Interest(-1 to quit):"))
        if year != -1:
            if year > 2015 or year < 1960:
                print("Valid years are 1960-2015")
            region = input("Enter region (type ’all’ to consider all):")
            income = input("Enter income category (type ’all’ to consider all):")
            e = filter_region(x, region)
            i = filter_income(e, income)
            s = sorted_ranking_data(i, year)
            print("")
            if len(s)-1 < 10:
                print("Top 10 Life Expectancy for ", year)
                for idx in range(len(s)):
                    print(idx+1, ": ", s[idx].country, s[idx].value)
                print("")
                print("Bottom 10 Life Expectancy for ", year)
                for idx in range(len(s)-1, -1, -1):
                    print(idx + 1, ": ", s[idx].country, s[idx].value)
                print("")
            else:
                print("Top 10 Life Expectancy for ", year)
                for idx in range(10):
                    print(idx + 1, ": ", s[idx].country, s[idx].value)
                print("")
                print("Bottom 10 Life Expectancy for ", year)
                for idx in range(len(s)-1, len(s) - 11, -1):
                    print(idx + 1, ": ", s[idx].country, s[idx].value)
                print("")
        else:
            quit()



if __name__ == '__main__':
    main()