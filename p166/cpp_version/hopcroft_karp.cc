#include "hopcroft_karp.h"
#include <algorithm>
#include <stdio.h>

const int HopcroftKarp::kInfinity = -1;

const int HopcroftKarp::kNone = -2;

HopcroftKarp::HopcroftKarp(BiGraph* nodes_bigraph) {
  nodes_bigraph_ = nodes_bigraph;
}

void HopcroftKarp::set_bigraph(BiGraph* nodes_bigraph) {
  nodes_bigraph_ = nodes_bigraph;
}


// returns a map of the row and columns that pair together for
// maximum cardinality (also equivalent for finding the minimum 
// number of lines which cover all 0's in the matrix used in the
// Hungarian algorithm
void HopcroftKarp::Match(map<int,int>* row_column_pairs) {
  int row_column_pairs_count = 0;
  int matrix_width;
  set<int>* all_nodes_set;
  set<int>::iterator node;

  // get the sets of vertices in U & V from the biparite graph
  u_nodes_set_ =   nodes_bigraph_->u_nodes_set();      
  v_nodes_set_ =   nodes_bigraph_->v_nodes_set();      

  // clear out the containers
  node_pair_.clear();
  node_distance_.clear();
  while (node_queue_.size() > 0)
    node_queue_.pop();
  all_nodes_set = nodes_bigraph_->all_nodes_set();
  for (node = all_nodes_set->begin();node != all_nodes_set->end(); ++node) {
    node_pair_[*node] = kNone;
    node_distance_[*node] = kInfinity;
  }

  //BFS return true when an augmenting path is found
  while (BreadthFirstSearch()) {
    for (node = u_nodes_set_->begin(); node != u_nodes_set_->end(); ++node)
      if (node_pair_[*node] == kNone && DepthFirstSearch(*node))
	row_column_pairs_count += 1;
  }

  // iterate over the vertices (nodes) in U, placing each's pair in V
  // in the map<int,int> for output
  matrix_width = all_nodes_set->size() / 2;
  for (node = u_nodes_set_->begin(); node != u_nodes_set_->end(); ++node)
    if (*node != kNone && node_pair_[*node] != kNone)
      (*row_column_pairs)[*node] = node_pair_[*node] % matrix_width;

}

void HopcroftKarp::Clear() {
  node_pair_.clear();
  node_distance_.clear();
  while (node_queue_.size() > 0) {
    node_queue_.pop();
  }
}


// partitions the bipartite graph in to 'layers'
// a node's layer denoted by the value in map<int,int>node_distance_
bool HopcroftKarp::BreadthFirstSearch() {
  set<int>::iterator set_iter;
  set<int>* neighbors; 
  int node;
  int node_neighbor;

  // if node from U isn't paired up yet, place it in layer 0 and add to queue
  // used in BFS, otherwise set it's layer to infinity
  for (set_iter = u_nodes_set_->begin(); set_iter != u_nodes_set_->end(); ++set_iter){
    node = *set_iter;
    if (node_pair_[node] == kNone ) {
      node_distance_[node] = 0;
      node_queue_.push(node);
    }else{
      node_distance_[node] = kInfinity;
    }
  }

  node_distance_[kNone] = kInfinity;
  
  while (node_queue_.size() > 0) {
    //get node at head of the queue
    node = node_queue_.front(); 
    node_queue_.pop();
    
    if (node != kNone) {
      //get nodes this node connects to by edges
      neighbors = nodes_bigraph_->neighbors(node);

      for (set_iter = neighbors->begin(); set_iter != neighbors->end(); ++set_iter){
        node_neighbor = *set_iter;
	if (node_distance_[node_pair_[node_neighbor]] == kInfinity) {
	  node_distance_[node_pair_[node_neighbor]] = node_distance_[node] +1;
	  node_queue_.push(node_pair_[node_neighbor]);
	}
      }
    }
  }

  return node_distance_[kNone] != kInfinity;

}


// DFS is done on free (unmatched nodes in U).
// Paths in the DFS alternate between unmatched and matched
// nodes and will traverse each 'layer' created by the BFS 
bool HopcroftKarp::DepthFirstSearch(int node) {
  set<int>::iterator u;
  set<int>* neighbors;
  int neighbor_node;
  
  if (node != kNone) {
    neighbors = nodes_bigraph_->neighbors(node);

    for (u = neighbors->begin();u != neighbors->end();++u){
      neighbor_node = *u;
      if (node_distance_[node_pair_[neighbor_node]] == node_distance_[node]+1 && 
          DepthFirstSearch(node_pair_[neighbor_node])) {
	node_pair_[neighbor_node] = node;
        node_pair_[node] = neighbor_node;
        return true; 
      }
    }

    node_distance_[node] = kInfinity;
    return false;
  }

  return true;

}
