def orig_run_experiment(school, days = 10):
    print("Initial State: {}".format(school))
    nursery = []

    for i in range(days):
        school = list(map(lambda x: (x - 1) % 7, school))
        new_adults_from_nursery = nursery.count(0)
        new_kids_from_school = school.count(6)
        if new_adults_from_nursery > 0:
            school.extend([6 for x in range(new_adults_from_nursery)])
            for j in range(new_adults_from_nursery):
                nursery.remove(0)

        nursery = list(map(lambda x: (x - 1) % 9, nursery))
        if new_adults_from_nursery + new_kids_from_school > 0:
            nursery.extend([8 for x in range(new_adults_from_nursery + new_kids_from_school)])
        print("After {} days: {}".format(i + 1, school + nursery))    
    return len(school) + len(nursery)
    
def run_experiment(school_init, days = 10):

    #print("Initial State: {}".format(school))
    nursery = [0 for x in range(9)]
    school = [school_init.count(x) for x in range(7)]

    for i in range(days):
        new_fish_from_school = school[0]
        school = school[1:]
        school.extend([new_fish_from_school])
        #school = list(map(lambda x: (x - 1) % 7, school))
        new_kids_from_nursery = nursery[0]
        nursery = nursery[1:]
        nursery.extend([new_fish_from_school + new_kids_from_nursery])
        school[-1] += new_kids_from_nursery
        #new_adults_from_nursery = nursery.count(0)
        #new_kids_from_school = school.count(6)
        #if new_adults_from_nursery > 0:
        #    school.extend([6 for x in range(new_adults_from_nursery)])
        #    for j in range(new_adults_from_nursery):
        #        nursery.remove(0)

        #nursery = list(map(lambda x: (x - 1) % 9, nursery))
        #if new_adults_from_nursery + new_kids_from_school > 0:
        #    nursery.extend([8 for x in range(new_adults_from_nursery + new_kids_from_school)])
        #print("After {} days: {}".format(i + 1, school + nursery))    
    return sum(school) + sum(nursery)

if __name__ == "__main__":

    school = [3, 4, 3, 1, 2]

    exp1 = run_experiment(school, days = 18)
    exp2 = run_experiment(school, days = 80)

    if exp1 == 26:
        print("Exp1 passed")
    else:
        print("Oops! Exp1 expected 26 but found {} instead.".format(exp1))
    
    if exp2 == 5934:
        print("Exp2 passed")
    else:
        print("Oops! Exp2 expected 5934 but found {} instead.".format(exp2))

    
    exp3 = run_experiment(school, days = 256)

    if exp3 == 26984457539:
        print("Exp3 passed")
    else:
        print("Oops! Exp3 expected 26984457539 but found {} instead.".format(exp3))
       