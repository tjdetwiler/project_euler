#include "utils.h"
#include <stdio.h>

void utils::print_matrix(int** mat,int mat_dim){
    for(int i = 0; i < mat_dim; i++){
      for(int j = 0; j < mat_dim; j++){
	printf("%4d", mat[i][j]);
      }
      printf("\n");
    }
    printf("\n");
}

void utils::print_map(map<int,int> m){
  map<int,int>::iterator it;
  for(it = m.begin(); it != m.end(); ++it){
    printf("(%d,%d)\n",it->first,it->second);
  }
}


void utils::print_set(set<int> v){
   for (set<int>::iterator it=v.begin();it!=v.end();++it){
       printf("%d, ",*it);
   }
   printf("\n");

}

bool utils::map_contains(map<int,int> pairs, std::pair<int,int> row_col_pair) {
  map<int,int>::iterator it;
  if (pairs.size() == 0) {
    return false;
  }

  it = pairs.find(row_col_pair.first);

  if (it->first == row_col_pair.first && 
     it->second == row_col_pair.second) {
    return true;
  }
  return false;
} 
