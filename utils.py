from myQueue import *
from myStack import *
from copy import *

Region = struct_type("Region", (int,"size"), ((NoneType, Node), "front"),((NoneType, Node), "back"))
Country = struct_type("Country", (str, "name"), (str, "CC"), (str, "region"), (str, "Income"), (list, "Years"), (list, "LE"), (str, "Special Notes"))
World = struct_type("World", (int, "size"), ((NoneType, Node), "front"), ((NoneType, Node), "back"))


def read_data(filename):
    '''
    The function reads the two data files and creates a data structure(queue) from these information files
    :param filename:A string, giving the partial name of the data file
    :return: a queue representing the data contained in the main data
        and metadata files
    '''
    l=open(filename+"_data.txt")
    y=open(filename+"_metadata.txt")
    d=l.readline().strip().split(",")
    x = y.readline().strip().split(",")
    Years=[]
    for idx in d[2:-1]:
        w=int(idx)
        Years.append(w)
    Globe=World(0, None, None)
    while x!=None and d!=None:
        d=l.readline().strip().split(",")
        x = y.readline().strip().split(",")
        if len(d) < 2 or len(x) < 2:
            break
        u = []
        for idx in d[2:-2]:
            if idx == "":
                u.append("")
            else:
                t = float(idx)
                u.append(t)
        s = Country(d[0], d[1], x[1], x[2], Years, u, x[3])
        enqueue(Globe, s)
    return Globe

def countries_only(Globe):
    '''
    the function takes in the queue from read_data and only retains the countries
    :param Globe: the data structure returned by read_data function
    :return: a queue with only countries
    '''
    County_Queue=World(0, None, None)
    while Globe.front != None or Globe.back != None:
        if Globe.front.value.region == "":
            dequeue(Globe)
        else:
            enqueue(County_Queue,Globe.front.value)
            dequeue(Globe)
    return County_Queue


def filter_region(data,region):
    '''
    The function filters the data structure returned by read_data and keeps only countries in that region
    :param data: the data structure being filtered
    :param region: the region that is being filtered for
    :return: a data structure with the region requested by user
    '''
    a=Region(0, None, None)
    while data.front != None or data.back != None:
        if region == "all":
            if data.front.value.region == "":
                dequeue(data)
            else:
                enqueue(a, data.front.value)
                dequeue(data)
        else:
            if data.front.value.region == region:
                    enqueue(a, data.front.value)
                    dequeue(data)
            else:
                dequeue(data)
    return a

def filter_income(data, income):
    '''
    The function filters the data structure returned by read_data and keeps only countries in that income level
    :param data: the data structure being filtered
    :param income: the income level that is being filtered for
    :return: a data structure with the income level requested by user
    '''
    i = Region(0, None, None)
    while data.front != None or data.back != None:
        if income == "all":
            if data.front.value.Income == "":
                dequeue(data)
            else:
                enqueue(i, data.front.value)
                dequeue(data)

        else:
            if data.front.value.Income == income:
                enqueue(i, data.front.value)
                dequeue(data)
            else:
                dequeue(data)
    return i

def print_country_data(data):
    '''
    prints the country years and their respective life expectancies
    :param data: the data structure which countries are to be printed from
    '''
    for x in data.front.value.Year:
        print("Year:", data.front.value.Year[x],"Life expectancy:",data.front.value.LE[x],")")
        dequeue(data)

def pretty_print_countries(data):
    '''
    prints the country name and its country code
    :param data: the data structure which countries are to be printed from
    '''
    while data!=None:
        print(data.front.value.name,"(",data.front.value.CC,")")
        dequeue(data)

def region_size(data):
    '''
    prints the number of countries in that region
    :param data: the data structure which countries are to be printed from
    '''
    print('Middle East & North Africa:',filter_region(data, 'Middle East & North Africa').size)
    print('Europe & Central Asia', filter_region(deepcopy(data), 'Europe & Central Asia').size)
    print('North America:',filter_region(deepcopy(data), 'North America').size)
    print('Latin America & Caribbean:',filter_region(deepcopy(data), 'Latin America & Caribbean').size)
    print('South Asia:',filter_region(deepcopy(data), 'South Asia').size)
    print('East Asia & Pacific:',filter_region(deepcopy(data), 'East Asia & Pacific').size)
    print('Sub - Saharan Africa:',filter_region(deepcopy(data), 'Sub - Saharan Africa').size)

def income_size(data):
    '''
    prints the number of countries in that income level
    :param data: the data structure which countries are to be printed from
    '''
    print('Lower middle income:',filter_income(deepcopy(data), 'Lower middle income').size)
    print('Upper middle income:',filter_income(deepcopy(data), 'Upper middle income').size)
    print('High income:',filter_income(deepcopy(data), 'High income:').size)
    print('Low income:',filter_income(deepcopy(data), 'Low income').size)

def deep_copy(x):
    if not isinstance(x, list): return x
    else: return map(deep_copy, x)

def main():
    '''
    Performs the stand alone behaviors of the program by calling other functions
    '''
    f = "worldbank_life_expectancy"
    x = read_data(f)
    a = countries_only(copy(x))
    print("Total number of entities:", x.size)
    print("Number of countries/territories:", copy(x).size)
    print("")
    print("Regions and their country count:")
    region_size(deep_copy(x))
    print("")
    print("Income categories and their country count")
    income_size(copy(x))
    r = input("Enter region name:")
    print("Countries in the ", r, "region:")
    pretty_print_countries(filter_region(deep_copy(x), r))
    print("")
    i = input("Enter income category:")
    print("Countries in the ", i, "region:")
    pretty_print_countries(filter_region(deep_copy(x), i))

if __name__ == '__main__':
    main()