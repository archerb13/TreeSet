#Bryce Archer

    
def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    
    #Compares the first names of the tow people
    if a.first < b.first:
        return True
    else:
        return False
    
    
def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    
    #Compares the last names of the two people
    if a.last < b.last:
        return True
    else:
        return False

def is_alphabetized(roster, ordering):
    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """
    
    #Loops through the roster and compares the two people to sort correctly
    for index in range (1,len(roster)):
        if (ordering(roster[index-1], roster[index])):
            return True
        else:
            return False
        
   
def mergSort(Ll, Rl, ordering):
    """
    Seperates the list into halves until two per group
    :param Ll: the left side of the list
    :param Rl: the right side of the list
    :param ordering: a function omparing two elements
    :return: the new sorted list
    :return: the number of comparisons
    """
    
    i = 0   #Int variable
    k = 0   #Int variable
    empty_l = []    #Empty list
    cost = 0    #Keep count of comparisons
    
    
    #Loop through until two lists become one again
    while (i < len(Ll) and k < len(Rl)):
        cost += 1
        #Appeneds to the Left side of the list after sorting correctly
        if ordering (Ll[i], Rl[k]):
            empty_l.append(Ll[i])
            i += 1
        #Appends to the right side of the list after sorting correctly
        else:
            empty_l.append(Rl[k])
            k += 1
    #Combines the left and right side of the list
    empty_l.extend(Ll[i:])
    empty_l.extend(Rl[k:])
    
    return (list(empty_l), cost)

    
def alphabetize(roster, ordering):
    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a result given through mergSort
    :return: the number of comparisons made on both sides
    """
    
    #Checks to see if the roster has 1 or fewer elements and returns the list
    if len(roster) <= 1:
        return (roster,0)
    #If more, separate the list into two parts
    else:
        mid = len(roster)//2
        list1, cl1 = alphabetize(roster[:mid], ordering)    #Left side
        list2, cl2 = alphabetize(roster[mid:], ordering)    #Right side
        res, cost = mergSort(list1, list2, ordering) #Gives the list and comparison amount 
        
        print(res)
                            
        return res, cl1+cl2+cost


