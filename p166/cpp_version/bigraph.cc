#include "bigraph.h"
#include<stdio.h>
#include<algorithm>

set<int>* BiGraph::neighbors(const int node) {
  return &neighbors_[node]; 
}

set<int>* BiGraph::u_nodes_set() {
  return &u_nodes_set_;
}

set<int>* BiGraph::v_nodes_set() {
  return &v_nodes_set_;
}

set<int>* BiGraph::all_nodes_set() {
  return &all_nodes_set_;
}

BiGraph::~BiGraph() {
  Clear();
}

void BiGraph::AddEdge(const int node_u, const int node_v) {
  pair<int,int>* row_column_pair = new pair<int,int>;
  *row_column_pair = make_pair(node_u,node_v);
  edges_.insert(row_column_pair);
  neighbors_[node_u].insert(node_v);
  neighbors_[node_v].insert(node_u);
  if (u_nodes_set_.count(node_u) == 0)
    u_nodes_set_.insert(node_u);
  if (v_nodes_set_.count(node_v) == 0)
    v_nodes_set_.insert(node_v);

  if (all_nodes_set_.count(node_v) == 0)
    all_nodes_set_.insert(node_v);
  if (all_nodes_set_.count(node_u) == 0)
    all_nodes_set_.insert(node_u);
}

void BiGraph::Clear() {
  set<pair<int,int>*>::iterator edge;
  v_nodes_set_.clear();
  u_nodes_set_.clear();
  neighbors_.clear();
  all_nodes_set_.clear();
  for (edge = edges_.begin(); edge != edges_.end(); ++edge)
    delete *edge;
  edges_.clear();
}

