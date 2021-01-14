class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):

    # Create a valid coloring for the graph
    # Questions asked:
    ## 1- which way to traverse the graph
    ## 2- is it possible to find a graph coloring with max D+1 colors (D is the degree)
    # => Each node has at most DD neighbors, and we have D+1D+1 colors. So, if we look at any node, there's always at least one color that's not taken by its neighbors.
    # => So yes, D+1 is always enough colors for a legal coloring.
    # one edge case identified while trying to prove that inductively
    # => if a graph has a loop ( an edge where both ends connect to the same node ),
    # it is not possible to find that graph coloring. (we re gonna throw an error when we find this case)
    ## Complexity of brute force approach: O(M x D^N)
    ## idea 1: color the graph one node by one node. C(N x D) Time Complexity,
    for v in graph:
        
        if(v in v.neighbors):
            raise Exception('loop found ! graph coloring not possible !')
        # Get the node's neighbors' colors, as a set so we
        # can check if a color is illegal in constant time
        illegal_colors =  set([x.color for x in v.neighbors])

        # Assign the first legal color (1)
        ## we don t have to look for all color that are not in illegal_colors,
        ## we simply have to find one color by which no neighbor is colord
        # legal_color = [color for color in colors if color not in illegal_colors]
        #   v.color = legal_color[0]
        
        # Assign the first legal color (2)
        for color in colors :
            if color not in illegal_colors:
                v.color = color
                break
            
        # -> this reduces our runtime to O(N+M) and O(D) space
        # linear Time complexity in graphs is when we look to node (O(N)) and every edge (O(M)) at least once
        
        ## 2 other edge cases:
        # nodes with no edges => no prob, the prob can occurs when we traverse the graph.
        """
        Isolated nodes tend to cause problems when we're traversing a graph (starting from one node and "walking along" edges to other nodes,
        like we do in a depth-first or breadth-first search).
        We're not doing that here—instead, we're iterating over a list of all the nodes.
        """
        # cycles => A graph has a cycle if there is a path from any node to itself via other nodes.
        """
        Yes, it will. Cycles also tend to cause problems with graph traversal,
        because we can end up in infinite loops (going around and around the cycle).
        But we're not actually traversing our graph here.
        """
    # Bonus:
    """
    1. Our solution runs in O(N+M) time but takes O(D) space. Can we get down to O(1)space?
    2. Our solution finds a legal coloring, but there are usually many legal colorings. 
    What if we wanted to optimize a coloring to use as few colors as possible?
    => For coloring a graph using as few colors as possible, 
    we don’t have a feasible solution. For real-world problems, 
    we'd often need to check so many possibilities that we’ll never be able to 
    use brute-force no matter how advanced our computers become.

    => One way to reliably reduce the number of colors we use is to use
    the greedy algorithm but carefully order the nodes.
    For example, we can prioritize nodes based on their degree, 
    the number of colored neighbors they have, 
    or the number of uniquely colored neighbors they have.    
    """
