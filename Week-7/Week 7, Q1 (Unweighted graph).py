# Write the pseudocode for an unweighted graph data structure.
# You either use an adjacency matrix or an adjacency list approach.
# Also, write a function to add a new node and a function to add an edge.
# Following that, implement the graph you have designed in the programming language of your choice.
# You must use Object Oriented Programming for this task. You may use your own linked list from previous
# labs, the STL LL, or use a simple fixed size array
#(10 elements would be fine).

#Pseudocode

"""
CLASS UNWEIGHTED_GRAPH()

    __INIT__(A) //self
    A.name ← {}

    VERTICES(A,B) //self,vertices
        if B !← A.name
           A.name[B] ← []
    else
        skip

    EDGE(A,B,C) //self,vertices,edge
        A.name[B].append[C]
        A.name[C].append[B]

    EMPTYDICT(A)//self
        for i in A.name
            print(i,A.name[i])


if __name__ = '__main__'

    w = UNWEIGHTED_GRAPH()

    w.VERTICES('B')
    w.VERTICES('A')
    w.VERTICES('C')
    w.VERTICES('D')
    w.EDGE('A','B')
    w.EDGE('A','C')
    w.EDGE('A','D')
    w.EDGE('B','D')
    w.EDGE(D','C')
    w.EMPTYDICT()

    
    


"""
#python code

class UNWEIGHTED_GRAPH:

    def __init__(self):
        self.name = {}

    def VERTICES(self,vertices):
        if vertices not in self.name :
            self.name [vertices] = []
        else:
            pass
        

    def EDGE(self,vertices,edge):
        self.name [vertices].append(edge)
        self.name [edge].append(vertices)

    def EMPTYDICT(self):
        for key in self.name :
            print('Vertex: ',key, '|','Edges: ' ,self.name [key])


if __name__ == '__main__':
    
    w = UNWEIGHTED_GRAPH()
    
    w.VERTICES('B')
    w.VERTICES('A')
    w.VERTICES('C')
    w.VERTICES('D')
    w.EDGE('A','B')
    w.EDGE('A','C')
    w.EDGE('A','D')
    w.EDGE('B','D')
    w.EDGE('D','C')
    w.EMPTYDICT()
    

