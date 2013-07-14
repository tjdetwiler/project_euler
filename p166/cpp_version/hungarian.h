#ifndef HUNGARIAN_H_
#define HUNGARIAN_H_

#include<set>
#include<queue>
#include<map>
#include "bigraph.h"
#include "hopcroft_karp.h"

using namespace std;

class Hungarian{
 public:
  ~Hungarian();
  Hungarian(const int h_matrix_width,const int** h_matrix);
  void Solve(map<int,int>* row_column_pairs);
  void Clear();
  void set_h_matrix(const int h_matrix_width,const int** h_matrix);

 private:
  int h_matrix_width_;
  int** h_matrix_;
  BiGraph bigraph_;
  HopcroftKarp* hopcroft_karp_;

  void Normalize(const int h_matrix_wdith, int** h_matrix);
  void ReduceRows(const int h_matrix_width, int** h_matrix);
  void ReduceColumns(const int h_matrix_width, int** h_matrix);
  void GetLinedRows(const set<int> marked_rows,
                    const int h_matrix_width,
                    set<int>* lined_rows);

  void ReduceMatrix(int**,int,map<int,int>);
  void AssignMatrixToBiGraph(int**,int,BiGraph*);

};

#endif //HUNGARIAN_H_
