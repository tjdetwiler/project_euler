#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct {
  int first, second, third, fourth;
} four_tuple;


void get_set(const int sum_value, set<four_tuple*>* s_set) {
  int D [] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  int a, b, c, d;
  four_tuple* tuple;
  for (int i = 0; i < 10; ++i){
    a = D[i]; 
    for (int j = 0; j < 10; ++j){
      b = D[j]; 
      for (int k = 0; k < 10; ++k){
        c = D[k]; 
        for (int l = 0; l < 10; ++l){
          d = D[l];
          if (a + b + c + d == sum_value) {
            tuple = new four_tuple;
            tuple->first = a; 
            tuple->second = b; 
            tuple->third = c;
            tuple->fourth = d;
            s_set->insert(tuple);
          } 
	}
      }
    }
  }
}

int get_value_by_index(const four_tuple* tuple, const int index) {
  if (index == 0 ){ return tuple->first;}
  if (index == 1 ){ return tuple->second;}
  if (index == 2 ){ return tuple->third;}
  else {return tuple->fourth;}
  
}

void get_subset(vector<four_tuple*>* entire_set,
                vector<pair<int,int>* >* position_vals,
                vector<four_tuple*>* sub_set) {

  bool match;
  int position, value;
  pair<int,int>* pv;

  for (unsigned int i = 0; i < entire_set->size(); ++i) {
    match = true;
    for (unsigned int j = 0; j < position_vals->size(); ++j) {
      pv = position_vals->at(j);
      position = pv->first;
      value = pv->second;
      if (get_value_by_index(entire_set->at(i),position) != value) {
        match = false;
        break;
      }
    }
    if (match) 
      sub_set->push_back( entire_set->at(i) );

  }
}


def count_mixtures(int sum_value) {
  int count = 0;
  int M[4][4];
  

}

int main(int argc, char** argv){
  set<four_tuple*> s_set;
  int sum_value = 6;
  get_set(sum_value, &s_set);
  printf("s_set size: %ld\n",s_set.size());


}














  // for (set<four_tuple*>::iterator it = s_set.begin(); it != s_set.end(); ++it) {
  //   printf("(%d,%d,%d,%d)\n", (*it)->first, (*it)->second, (*it)->third, (*it)->fourth);
  // }


