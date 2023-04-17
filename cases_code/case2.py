from collections import defaultdict
from flask import request


def case_2(pairs, nodes):
    class FindAncestors:
        def get_child_parent_relations(self, pairs):
            pairs_1 = list(pairs)
            defdic = defaultdict(list)
            for k, v in pairs_1:
                defdic[v].append(k)
            return defdic

        def get_ancestors(self, root, child_to_parent):
            ancestors = set()
            lst = list([root])
            while lst:
                node = lst.pop()
                if node is not root:
                    ancestors.add(node)
                lst.extend(child_to_parent[node])
            return ancestors

        def common(self, ancestors):
            a = ancestors[0]
            b = ancestors[1]
            if (a & b):
                return True
            else:
                return False
    obj = FindAncestors()
    child_to_parent = obj.get_child_parent_relations(pairs)
    # print('child_to_parent: ',child_to_parent)
    # input_nodes = list(input('Enter 2 nodes as 2,3'))
    node1 = nodes[0]
    node2 = nodes[1]
    print(node1, node2)
    ancestors = [obj.get_ancestors(node, child_to_parent)
                 for node in (node1, node2)]
    # print('ancestors: ',ancestors)
    common_ancestors = obj.common(ancestors)
    print(common_ancestors)
    return common_ancestors
# pairs = [(10,3), (2,3), (3,6), (5,6), (5,17), (4,5), (4,8), (8,9)]
# nodes = [6,8]
# case_2(pairs, nodes)
