from utils import *
from binarysearch import *


Range=struct_type("Range",(str,"country"),(int,"year1"),(int,"year2"),(float,"value1"),(float,"value2"))

def quickSort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0].value1-L[0].value2
        ( less, same, more ) = partition( pivot, L )
        return quickSort( less ) + same + quickSort( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    (less, same, more) = ([], [], [])
    for e in L:
        if e.value1-e.value2 < pivot:
            less.append( e )
        elif e.value1-e.value2 > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

def sorted_drop_data(data):
    '''
    this funtion  identifies the 10 worst drops in life expectancy
        throughout the 1960-2015 time frame.
    :param data:the data structure returned by countries only function.
    :return:a list in ascending order of the 10 worst drops in life expectancy
        throughout the 1960-2015 time frame.
    '''
    list = []
    a = countries_only(data)
    while a.front != None or a.back != None:
        test_drop = 0
        best_drop = 0
        c = a.front.value.LE[0]
        for idx in a.front.value.LE[1:]:
            if c == '' and idx == '':
                pass
            if c == '' and idx != '':
                c = idx
            if c != '' and idx == '':
                pass
            elif c < idx:
                d = c - idx
                if d < test_drop:
                    test_drop = d
            elif idx < c:
                if test_drop < best_drop:
                    best_drop = test_drop
                c = idx
        if test_drop == 0 and best_drop == 0:
            dequeue(a)
        else:
            f = binary_search(a.front.value.LE, c, 0, len(a.front.value.LE)-1)
            e = binary_search(a.front.value.LE, idx, 0, len(a.front.value.LE)-1)
            list.append(Range(a.front.value.name, a.front.value.Years[f], a.front.value.Years[e], c, idx))
            dequeue(a)
            print(list)
    return quickSort(list)

def main():
    f = "worldbank_life_expectancy"
    x = read_data(f)
    q = sorted_drop_data(x)
    print("Worst life expectancy drops: 1960 to 2015")
    for idx in range(10):
        print(idx + 1, ": ", q[idx].name, "from", q[idx].year, "(", q[idx].value1,")", "to",
              q[idx].year, "(", q[idx].value2,")", (q[idx].value1-q[idx].value2))

if __name__ == '__main__':
    main()


'''
if max_so_far - min_after_that>max_drop:
    max_drop=max_so_far-min_after_that'''