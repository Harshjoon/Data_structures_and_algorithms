#include <iostream>
#include <vector>
using namespace std;

class Graph {
        int V;
        // adjacency list
        vector<list<int>> adj;
    public:
        // Constructor
        Graph(int V);
        void addEdge(int v, int w);
        void BFS(int s);
};

Graph::Graph(int V){
    this->V = V;
    adj.resize(V);
}
void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
}
void Graph::BFS(int s){
    
}

