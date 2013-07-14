#include <limits.h>
#include <algorithm>
#include <set>
#include "hopcroft_karp.h"
#include "hungarian.h"
#include "utils.h"

using namespace std;

Hungarian::Hungarian(const int h_matrix_width, const int** h_matrix) {
  h_matrix_width_ = h_matrix_width;
  h_matrix_ = (int**)malloc(h_matrix_width_ * sizeof(int*));
  for (int i = 0; i < h_matrix_width_; ++i) {
    h_matrix_[i] = (int*)malloc(h_matrix_width_ * sizeof(int));
    for (int j = 0; j < h_matrix_width_; ++j)
      h_matrix_[i][j] = h_matrix[i][j];
  }
  AssignMatrixToBiGraph(h_matrix_,h_matrix_width_,&bigraph_);
  hopcroft_karp_ = new HopcroftKarp(&bigraph_);
}

Hungarian::~Hungarian() {
  delete hopcroft_karp_;
  hopcroft_karp_ = 0;
  for (int i = 0;i < h_matrix_width_; ++i) {
    delete h_matrix_[i];
    h_matrix_[i] = 0;
  }
  delete h_matrix_;
  h_matrix_ = 0;
}


// solves assignment problem in polynomial time
// http://en.wikipedia.org/wiki/Hungarian_algorithm
//
// Step-by-step explained in:
// http://en.wikipedia.org/wiki/Hungarian_algorithm#Matrix_interpretation
//
// first argument is populated with the optimal row/columns
// which produce the max sum of respective values
// from the matrix provided 
//
// example usage:
//   map<int,int> pairs;
//   Hungarian hungarian (h_matrix_width,h_matrix);
//   hungarian.Solve(&pairs);
//   utils::print_map(pairs);
void Hungarian::Solve(map<int,int>* row_column_pairs) {
  Normalize(h_matrix_width_, h_matrix_);
  ReduceRows(h_matrix_width_, h_matrix_);
  ReduceColumns(h_matrix_width_, h_matrix_);

  AssignMatrixToBiGraph(h_matrix_, h_matrix_width_, &bigraph_);
  hopcroft_karp_->Match(row_column_pairs);
   
  // once the minimum number of lines drawn over matrix
  while ((int)row_column_pairs->size() != h_matrix_width_) {

    //step 3&4 in http://en.wikipedia.org/wiki/Hungarian_algorithm#Matrix_interpretation
    ReduceMatrix(h_matrix_,h_matrix_width_,*row_column_pairs); 
    bigraph_.Clear();
    row_column_pairs->clear();

    // create bipartite graph from where 0's are in h_matrix
    AssignMatrixToBiGraph(h_matrix_,h_matrix_width_,&bigraph_);
    hopcroft_karp_->set_bigraph(&bigraph_); 

    //draw minimum lines to cover all 0's     
    hopcroft_karp_->Match(row_column_pairs);
   }
   

}

// frees memory of copy of matrix 
void Hungarian::Clear() {
  if (h_matrix_ == NULL) {
    for (int i = 0; i < h_matrix_width_; ++i) {
      delete h_matrix_[i];
      h_matrix_[i] = 0;
    }
    delete h_matrix_;
    h_matrix_ = 0;
  }

  if (hopcroft_karp_ != NULL)
    hopcroft_karp_->Clear();

  bigraph_.Clear();

}

void Hungarian::set_h_matrix(const int h_matrix_width, const int** h_matrix) {
  h_matrix_width_ = h_matrix_width;
  h_matrix_ = (int**)malloc(h_matrix_width_ * sizeof(int*));
  for (int i = 0; i < h_matrix_width_; ++i) {
    h_matrix_[i] = (int*)malloc(h_matrix_width_ * sizeof(int));
    for (int j = 0; j < h_matrix_width_; ++j)
      h_matrix_[i][j] = h_matrix[i][j];
  }
  AssignMatrixToBiGraph(h_matrix_,h_matrix_width_,&bigraph_);
  hopcroft_karp_ = new HopcroftKarp(&bigraph_);
}

// Used when the assignment problem is needed to maximize the sum of the
// selected values. If not called the fucntion Hungarian::Solve() with
// produce the minimum sum of selected values
void Hungarian::Normalize(const int h_matrix_width, int** h_matrix) {
    int max_val = 0;
    int i,j,val;
    for (int i = 0; i < h_matrix_width; ++i) {
        for (int j = 0; j < h_matrix_width; ++j) {
	    val = h_matrix[i][j];
            if (val > max_val)
	      max_val = val;
        }
    }
    for (int i = 0; i < h_matrix_width; ++i) {
        for (int j = 0; j < h_matrix_width; ++j)
	  h_matrix[i][j] = max_val - h_matrix[i][j];
    }
}


// subtract minimum value from each row
void Hungarian::ReduceRows(const int h_matrix_width, int** h_matrix) {
  int minimum_row_value;
  for (int row = 0; row < h_matrix_width; ++row) {
    minimum_row_value = INT_MAX;

    for (int column = 0; column< h_matrix_width; ++column)
      if (h_matrix[row][column] < minimum_row_value)
	minimum_row_value = h_matrix[row][column];

    for (int column = 0; column < h_matrix_width; ++column)
      h_matrix[row][column] -= minimum_row_value;
  }
}

// subtract minimum value from each column
void Hungarian::ReduceColumns(const int h_matrix_width, int** h_matrix) {
  int minimum_column_value;
  for (int column = 0; column < h_matrix_width; ++column) {
    minimum_column_value = INT_MAX;

    for (int row = 0;row < h_matrix_width; ++row)
      if (h_matrix[row][column] < minimum_column_value)
	minimum_column_value = h_matrix[row][column];

    for (int row = 0; row < h_matrix_width; ++row)
      h_matrix[row][column] -= minimum_column_value;

  }
}

void Hungarian::GetLinedRows(const set<int> marked_rows,
                             const int h_matrix_width,
                             set<int>* lined_rows) {
  lined_rows->clear();
  for (int row = 0; row < h_matrix_width; ++row)
    if (marked_rows.count(row) == 0)
      lined_rows->insert(row);
}


void Hungarian::ReduceMatrix(int** h_matrix, 
                              int h_matrix_width,
                              map<int,int> pairs) {
  set<int> assigned_rows_set;
  set<int> assigned_columns_set;
  set<int> marked_rows_set;
  set<int> marked_columns;
  set<int> lined_rows_set;  
  map<int,int>::iterator map_it;
  set<int>::iterator set_it;
  int marking;  
  int row;
  int column;
  int min_value;
  pair<int,int> row_column_pair;
  priority_queue<int,vector<int>,greater<int> > left_overs;
 
  for (map_it = pairs.begin(); map_it != pairs.end(); ++map_it) {
    assigned_rows_set.insert(map_it->first);
    assigned_columns_set.insert(map_it->second - h_matrix_width);
  }

  // mark rows with no assignment
  for (row = 0; row < h_matrix_width; ++row)
    if (assigned_rows_set.count(row) == 0)
      marked_rows_set.insert(row);

  marking = 1;

  while(marking) {
    marking = 0;

    // mark columns with 0's in the marked rows      
    for (set_it=marked_rows_set.begin();set_it != marked_rows_set.end(); ++set_it) {
      row = *set_it;
      for (column=0;column<h_matrix_width;++column)
	if (h_matrix[row][column] == 0 && marked_columns.count(column)==0)
	  marked_columns.insert(column);
    }

    // mark rows with 0's in the marked columns      
    for (set_it=marked_columns.begin();set_it != marked_columns.end();++set_it) {
      column = *set_it;
      for (row=0;row < h_matrix_width;++row) {
	row_column_pair = make_pair(row,column+h_matrix_width);
        if (utils::map_contains(pairs,row_column_pair))
	  if (marked_rows_set.count(row)==0) {
	     marked_rows_set.insert(row);
             marking = 1;
	  }

      }
    }

    GetLinedRows(marked_rows_set,h_matrix_width,&lined_rows_set);

    for (row=0; row < h_matrix_width; ++row)
      for (column=0; column < h_matrix_width; ++column)
	if (lined_rows_set.count(row) > 0 || marked_columns.count(column) > 0 ) {
	  continue;
	}else{
	  left_overs.push(h_matrix[row][column]);
	}

    if (left_overs.size() > 0) {
      min_value = left_overs.top();

      for (row=0; row < h_matrix_width; ++row)
	for (column=0; column < h_matrix_width; ++column) {
	  if (lined_rows_set.count(row) > 0 && marked_columns.count(column) > 0 )
	    h_matrix[row][column] += min_value;

	  if (lined_rows_set.count(row) == 0 && marked_columns.count(column) == 0 )
	    h_matrix[row][column] -= min_value;
	}
    }

  } //while(marking)
}

void Hungarian::AssignMatrixToBiGraph(int** h_matrix,int h_matrix_width,BiGraph* G) {
  for (int row = 0; row < h_matrix_width; ++row) 
    for (int column = 0; column < h_matrix_width; ++column) 
      if (h_matrix[row][column] == 0) 
	G->AddEdge(row,column + h_matrix_width);
}

