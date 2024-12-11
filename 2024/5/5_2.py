import sys
import networkx as nx

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    input = file.read()

def make_graph(rules, pages, add_pages=True):
    g = nx.DiGraph()
    not_checked_rules = rules.copy()
    while len(not_checked_rules) > 0:
        rule = not_checked_rules.pop()
        vertices = rule.split("|")
        if vertices[0] in pages and vertices[1] in pages:
            g.add_edge(vertices[0], vertices[1])
    if add_pages:
        for i, page in enumerate(pages):
            if i < len(pages) - 1:
                g.add_edge(page, pages[i+1])
    return g

def find_correct_order(graph, pages):
    correct_pages = []
    pages_copy = pages.copy()
    while len(correct_pages) < len(pages):
        for page in pages_copy:
            if len(list(graph.successors(page))) == 0:
                graph.remove_node(page)
                correct_pages.insert(0, page)
                pages_copy.remove(page)
                break
    return correct_pages

input_list = input.splitlines()
sep = input_list.index("")

rules = input_list[:sep]
mans_lists = input_list[sep+1:]

res = 0
for man in mans_lists:
    pages = man.split(",")
    graph = make_graph(rules, pages, True)
    try:
        nx.find_cycle(graph)
        new_pages = find_correct_order(make_graph(rules, pages, False), pages)
        mid = new_pages[int((len(new_pages)-1)/2)]
        res += int(mid)
    except nx.NetworkXNoCycle:
       pass

print(res)
