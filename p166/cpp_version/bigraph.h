#ifndef BIGRAPH_H_
#define BIGRAPH_H_

#include<set>
#include<map>

using namespace std;

// Used as a container 
// for bipartite graphs. Sets U and V are 
// disjoint. Each vertex (node) in U is connect
// by at least one edge to a vertex (node) in V

class BiGraph {
 public:
  set<int>* neighbors(const int);    
  set<int>* u_nodes_set();
  set<int>* v_nodes_set();
  set<int>* all_nodes_set();
  ~BiGraph();

  void AddEdge(const int u , const int v);    
  void Clear();

 private:
  set<int> u_nodes_set_;
  set<int> v_nodes_set_;
  set<int> all_nodes_set_;
  set<pair<int,int>* > edges_;
  map<int,set<int> > neighbors_;

};

#endif //BIGRAPH_H_
