import sys
import networkx as nx
import math

graph = nx.Graph()


prev_vert = []
num_line = 0

with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        left_conn = False
        num_line += 1
        new_vert = []
        for tile in range(len(line.strip())):
            curr_id = str(num_line) + '.' +  str(tile)
            curr_char = line[tile]
            if curr_char == ".":
                continue
            up = down = left = right = False

            if curr_char == "|":
                up = down = True
            elif curr_char == "-":
                left = right = True
            elif curr_char == "L":
                up = right = True
            elif curr_char == "J":
                up = left = True
            elif curr_char == "7":
                down = left = True
            elif curr_char == "F":
                down = right = True
            elif curr_char == "S":
                up = down = right = left = True
                start_tile = curr_id

            upper_id = str(num_line - 1) + '.' + str(tile)
            left_id = str(num_line) + '.' + str(tile - 1)
            if up and (upper_id in prev_vert):
                graph.add_edge(curr_id, upper_id)
            if left and left_conn:
                graph.add_edge(curr_id, left_id)
            
            if right:
                left_conn = True
            if not right:
                left_conn = False

            if down:
                new_vert.append(curr_id)
        prev_vert = new_vert

sol_loop = nx.node_connected_component(graph, start_tile)
print(sol_loop)

print(len(sol_loop)/2)