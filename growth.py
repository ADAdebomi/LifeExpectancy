from utils import *
from binarysearch import *
from quickSort  import *

CountryValue=struct_type("CountryValue",(str,"country"),(float,"value"))

def sorted_growth_data(data,year1,year2):
    '''
    this function ranks countries by absolute growth in life
        expectancy over a specified range of years
    :param data:the data structure returned by read_data function
    :param year1:the first year being considered
    :param year2:the second year being considered
    :return:a list of data structure Country value which is sorted in descending order
    '''
    list = []
    while data.front != None or data.back != None:
        o=binary_search(data.front.value.Years, year1, 0, len(data.front.value.Years)-1)
        z = binary_search(data.front.value.Years, year2, 0, len(data.front.value.Years) - 1)
        if data.front.value.LE[o]=="" or data.front.value.LE[z]=="":
            dequeue(data)
        else:
            d = abs(data.front.value.LE[z]-data.front.value.LE[o])
            list.append(CountryValue(data.front.value.name, d))
            dequeue(data)
    return quickSort(list)


def main():
    '''
    Performs the stand alone behaviors of the program by calling other functions
    '''
    f = "worldbank_life_expectancy"
    x = read_data(f)
    while f != "":
        print("")
        year1 = int(input("Enter starting year of Interest(-1 to quit):"))
        if year1 != -1 :
            year2 = int(input("Enter ending year of Interest(-1 to quit):"))
            region = input("Enter region (type ’all’ to consider all):")
            income = input("Enter income category (type ’all’ to consider all):")
            e = filter_region(x, region)
            i = filter_income(e, income)
            s = sorted_growth_data(i, year1, year2)
            print("")
            if len(s)-1 <= 10:
                print("Top 10 Life Expectancy Growth ", year1, "to", year2)
                for idx in range(len(s)):
                    print(idx+1, ": ", s[idx].country, s[idx].value)
                print("")
                print("Bottom 10 Life Expectancy Growth ", year1, "to", year2)
                for idx in range(len(s)-1, -1, -1):
                    print(idx + 1, ": ", s[idx].country, s[idx].value)
                print("")
            else:
                print("Bottom 10 Life Expectancy Growth ", year1, "to", year2)
                for idx in range(10):
                    print(idx + 1, ": ", s[idx].country, s[idx].value)
                print("")
                print("Bottom 10 Life Expectancy Growth ", year1, "to", year2)
                for idx in range(len(s)-1,len(s) - 11,-1):
                    print(idx + 1, ": ", s[idx].country, s[idx].value)
                print("")
        else:
            quit()


if __name__ == '__main__':
    main()
