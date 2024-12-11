import sys
import networkx as nx

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    input = file.read()

def make_graph(rules, pages):
    g = nx.DiGraph()
    not_checked_rules = rules.copy()
    while len(not_checked_rules) > 0:
        rule = not_checked_rules.pop()
        vertices = rule.split("|")
        if vertices[0] in pages and vertices[1] in pages:
            g.add_edge(vertices[0], vertices[1])
    for i, page in enumerate(pages):
        if i < len(pages) - 1:
            g.add_edge(page, pages[i+1])
    return g

input_list = input.splitlines()
sep = input_list.index("")

rules = input_list[:sep]
mans_lists = input_list[sep+1:]

res = 0
for man in mans_lists:
    pages = man.split(",")
    graph = make_graph(rules, pages)
    try:
        nx.find_cycle(graph)
    except nx.NetworkXNoCycle:
        mid = pages[int((len(pages)-1)/2)]
        res += int(mid)

print(res)
