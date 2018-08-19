import turtle as t
from utils import *
from copy import *

def quickSort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0].value
        ( less, same, more ) = partition( pivot, L )
        return quickSort( less ) + same + quickSort( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    (less, same, more) = ([], [], [])
    for e in L:
        if e.value < pivot:
            less.append( e )
        elif e.value > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

def draw_border1():
    t.penup()
    t.goto(-600,-250)
    t.pendown()
    t.forward(550)
    t.write("2015")
    t.penup()
    t.backward(550)
    t.pendown()
    t.left(90)
    t.forward(550)
    t.penup()
    t.goto(0,0)


def get_values(data):
    list=[]
    median_list=[]
    while data != "":
        count = 0
        while data.front!=None:
            list.append(data.front.value.LE[count])
            dequeue(data)
        quickSort(list)
        median_idx = (len(list))//2
        median_list.append(list[median_idx])
        count+1
    print(median_list)





def main():
    f = "worldbank_life_expectancy"
    x = read_data(f)
    data1 = get_values(filter_region(x, 'Sub-Saharan Africa'))
    data2 = get_values(filter_region(deepcopy(x), 'South Asia'))
    data3 = get_values(filter_region(deepcopy(x), 'Europe & Central Asia'))
    data4 = get_values(filter_region(deepcopy(x), 'Latin America & Caribbean'))
    data5 = get_values(filter_region(deepcopy(x), 'Middle East & North Africa'))
    data6 = get_values(filter_region(deepcopy(x), "North America"))
    data8 = get_values(filter_region(deepcopy(x), 'East Asia & Pacific'))
    data6 = get_values(filter_income(deepcopy(x), "Low income"))
    data9 = get_values(filter_income(deepcopy(x), 'Upper middle income'))
    data10 = get_values(filter_income(deepcopy(x), 'Lower middle income'))
    data11 = get_values(filter_income(deepcopy(x), 'High income'))
    #draw_border1()
    get_values(x)
    t.done()


if __name__ == '__main__':
    main()