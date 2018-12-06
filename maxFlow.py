"""From Taha 'Introduction to Operations Research', example 6.4-2."""

from __future__ import print_function
from ortools.graph import pywrapgraph
import parse,csv
def main():

    """MaxFlow simple interface example."""

  # Define three parallel arrays: start_nodes, end_nodes, and the capacities
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 20.

  # start_nodes = [0, 0, 0, 1, 1, 2, 2, 3, 3]
  # end_nodes = [1, 2, 3, 2, 4, 3, 4, 2, 4]
  # capacities = [20, 30, 10, 40, 30, 10, 20, 5, 20]

  # Instantiate a SimpleMaxFlow solver.
    word_dict = parse.construct_word_dict('vocab.txt')
    parse.count_words("train.tsv", word_dict)
    start_nodes,end_nodes,capacities=parse.create_edge(word_dict)


    with open('./test.tsv','rb') as f:
        reader=csv.reader(f,delimiter='\t')
        next(reader, None)
        for row in reader:
            max_flow = pywrapgraph.SimpleMaxFlow()
            # Add each arc.
            for i in range(0, len(start_nodes)):
                max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])
            tokens=parse.remove_punctuations(row[2].lower()).split(' ')
            label=row[1]
            lastvalidtoken=word_dict['[SOURCE]']['word_id']
            for i,token1 in enumerate(tokens):
                if not (token1 in word_dict):
                    continue
                else:
                    max_flow.AddArcWithCapacity(word_dict['[SOURCE]']['word_id'],word_dict[token1]['word_id'],99)
                    lastvalidtoken=word_dict[token1]['word_id']
            max_flow.AddArcWithCapacity(lastvalidtoken+len(word_dict)-2,word_dict['[SINK]']['word_id'],99)

            if max_flow.Solve(word_dict['[SOURCE]']['word_id'], word_dict['[SINK]']['word_id']) == max_flow.OPTIMAL:
                print('label:\t',label,'\tMax flow:\t', max_flow.OptimalFlow())

            else:
                print('There was an issue with the max flow input.')


if __name__ == '__main__':
  main()