#ifndef HOPCROFT_KARP_H_
#define HOPCROFT_KARP_H_

#include <set>
#include <queue>
#include <map>
#include "bigraph.h"

using namespace std;

// Container used to solve the maximum cardinality matching
// problem 
// http://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm

class HopcroftKarp{
 public:
  HopcroftKarp(BiGraph* nodes_bi_graph);
  void set_bigraph(BiGraph* nodes_bi_graph);
  void Match(map<int,int>* row_column_pairs);
  void Clear();

 private:
  static const int kInfinity;
  static const int kNone;
  set<int>* u_nodes_set_;
  set<int>* v_nodes_set_;
  map<int,int> node_pair_;
  map<int,int> node_distance_;
  queue<int> node_queue_;
  BiGraph* nodes_bigraph_;
  
  bool BreadthFirstSearch();
  bool DepthFirstSearch(int);
};

#endif //HOPCROFT_KARP_H_


