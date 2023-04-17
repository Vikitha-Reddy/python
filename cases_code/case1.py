from collections import Counter


def case_1(pairs):
    class FindParents:
        def __init__(self, lst_0, lst_1):
            self.lst_0 = lst_0
            self.lst_1 = lst_1

        def no_parents(self):
            No_parents = []
            for i in lst_0:
                if i not in lst_1:
                    No_parents.append(i)
            return list(set(No_parents))

        def one_parent(self):
            dic = dict(Counter(lst_1))
            lst_one_parent = [k for k, v in dic.items() if v == 1]
            return lst_one_parent

    lst_0 = [i[0] for i in pairs]
    lst_1 = [i[1] for i in pairs]
    obj = FindParents(lst_0, lst_1)
    childWithNoParents = obj.no_parents()
    childWithOneParent = obj.one_parent()
    # print(childWithNoParents)
    # print(childWithOneParent)
    return childWithNoParents, childWithOneParent
