# """From Bradley, Hax, and Magnanti, 'Applied Mathematical Programming', figure 8.1."""

from __future__ import print_function
from ortools.graph import pywrapgraph

def main():
  """MinCostFlow simple interface example."""

  # Define four parallel arrays: start_nodes, end_nodes, capacities, and unit costs
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 15 and a unit cost of 4.

  start_nodes = [ 0,  0,  0] + [ 1,  1,  1,  1,  2,  2,  2,  2,  3,  3,  3,  3]
  end_nodes   = [ 1,  2,  3] + [ 4,  5,  6,  7,  4,  5,  6,  7,  4,  5,  6,  7]
  capacities  = [99, 99, 99] + [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
  unit_costs  = [ 0,  0,  0] + [ 1,  6,  3,  5,  7,  3,  1,  6,  9,  4,  5,  4]
  
  # Define an array of supplies at each node.
#   supplies = [0, 20, 10, 25, -11, -13, -17, -14]
  supplies = [0, 20, 12, 25, -13, -13, -17, -14]


  # Instantiate a SimpleMinCostFlow solver.
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Add each arc.
  for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])

  # Add node supplies.

  for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


  # Find the minimum cost flow between node 0 and node 4.
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print('')
    print('  Arc    Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s  / %3s       %3s' % (
          min_cost_flow.Tail(i),
          min_cost_flow.Head(i),
          min_cost_flow.Flow(i),
          min_cost_flow.Capacity(i),
          cost))
  else:
    print('There was an issue with the min cost flow input.')

if __name__ == '__main__':
  main()