import sys

def results(nodes_expanded,nodes_generated,distance, memory, start, end):
    print("nodes expanded:", nodes_expanded)
    print("nodes generated:", nodes_generated)
    if distance == "infinity":
        print("distance:", distance)
        print("route:\nnone")
    else:
        print("distance:", distance, "km")
        path(memory, start, end, distance)

def path(memory, start ,end, distance):
    route = []
    for i in memory:
        if end in i and distance in i:
            route.append(i)
    for i in range(route[0][3]-1):
        for j in memory:
            if route:
                if route[-1][1] in j and route[-1][3] - 1 in j:
                    route.append(j)
    route.reverse()
    print("route:")

    if number_of_arguments == 4:
        for i in range(len(route)):
            if i > 0:
                print(route[i][1],"to",route[i][0],",",route[i][2] - route[i-1][2],"km")
            else:
                print(route[i][1],"to",route[i][0],",",route[i][2],"km")
    
    elif number_of_arguments == 5:
        for i in range(len(route)):
            if i > 0:
                print(route[i][1],"to",route[i][0],",",route[i][4] - route[i-1][4],"km")
            else:
                print(route[i][1],"to",route[i][0],",",route[i][4],"km")
    return None


def graph_search(cost_func,source,destination,heuristic_func):

    closed_set = set()
    nodes_generated = 1
    fringe = [] 
    memory_lane = []
    nodes_expanded = []
    fringe.append([source, None, 0.0, 0, 0.0])
    memory_lane.append([source, None, 0.0, 0, 0.0])
    current_state = source
    done = False
    while not done:
        if not fringe:
            return False
        nodes_expanded.append(current_state)
        parent_cost = float(fringe[0][4])
        prev_depth = fringe[0][3]
        fringe.pop(0)
        if str(current_state) not in closed_set:
            for i in cost_func:
                if current_state in i:
                    nodes_generated+=1
                    a =[cost_func.index(i),i.index(current_state)]
                    generated_state = cost_func[cost_func.index(i)][1] if a[1]==0 else cost_func[cost_func.index(i)][0]
                    parent = current_state
                    depth = prev_depth +1
                    heuristic_value = 0
                    for j in heuristic_func:
                        if generated_state in j:
                            heuristic_value = float(heuristic_func[heuristic_func.index(j)][1])
                    actual_cost = parent_cost + float(cost_func[cost_func.index(i)][2])
                    cumulative_cost = heuristic_value + parent_cost + float(cost_func[cost_func.index(i)][2])
                    fringe.append([generated_state, parent, cumulative_cost, depth, actual_cost])
                    memory_lane.append([generated_state, parent, cumulative_cost, depth, actual_cost])
        closed_set.add(current_state)
        fringe = sorted(fringe,key=lambda x: x[2])
        if not fringe:
            distance = "infinity"
            count_nodes_expanded = len(nodes_expanded)
        else:
            current_state = str(fringe[0][0])
            distance = fringe[0][2]
            count_nodes_expanded = len(nodes_expanded) + 1

        if current_state == destination or distance == "infinity":
            results(count_nodes_expanded,nodes_generated,distance, memory_lane, source, destination)
            done = True

if __name__ == "__main__":
  input_file = sys.argv[1]
  source = sys.argv[2]
  destination = sys.argv[3]

  cost_func = []
  heuristics_func = []
  
  with open(input_file) as f:
    routes = f.readlines()
  
  for line in routes[:-1]:
    cities = line.split()
    cost_func.append([cities[0],cities[1],cities[2]])
  
  cities = set()
  for i in cost_func:
    cities.add(i[0])
    cities.add(i[1])
  number_of_cities = len(cities)
  
  try:
    heuristic_file = sys.argv[4]
    with open(heuristic_file) as f:
      heuristics = f.readlines()
    for line in heuristics[:-1]:
      h = line.split()
      heuristics_func.append([h[0],h[1]])
  except:
    heuristic_func = [[i,0.0] for i in cities]

  number_of_arguments = len(sys.argv)
  
  graph_search(cost_func,source,destination,heuristics_func)