#Implement BFS and DFS traversals for the above graph.
# Save the nodes traversed in sequence to a text file.
 
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

    def DFSORT(self, vertices):
        
        self.visited = []
        self.stack= []

        self.stack.append(vertices)

        while self.stack != []:
            u = self.stack.pop()
            if u not in self.visited:
                self.visited.append(u)
                for edge in self.name [u]:
                    self.stack.append(edge)
                print('DFS to search from Vertex = ',vertices,'Visited Nodes = ',self.visited)
                file = open("DFSORT","w")
                file.write(str(self.visited))
                file.close
        
        return self.visited

    def BFSORT(self,vertices):

        self.q = []
        self.visited = []

        self.q.insert(0, vertices)

        while self.q != []:
            u = self.q.pop()
            if u not in self.visited:
                self.visited.append(u)
                for edge in self.name [u]:
                    self.q.insert(0,edge)
        print ('BFS to search from Vertex = ',vertices,'Visited Nodes = ',self.visited)
        file = open("BFSORT","w")
        file.write(str(self.visited))
        file.close
        return self.visited

        

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
    w.DFSORT('A')
    w.DFSORT('B')
    w.BFSORT('A')
    w.BFSORT('B')

    


        
        

        

