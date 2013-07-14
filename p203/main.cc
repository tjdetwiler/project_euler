#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <vector>
#include "utils.h"
#include <iostream>
#include <set>


using namespace std;



vector<long> get_primes(long max_val) {
  vector<long> vals (max_val + 1);
  for(int i = 0; i < (int)vals.size(); ++i)
    vals[i] = i;

  vals[0] = 0;
  long v,m,r;
  vector<long> X;
  for(int i = 2; i < (int)vals.size()/2 + 2; ++i) {
    v = vals[i];
    if ( v == 0 ) 
      continue;
    m = 2;
    r = m*v;

    while (r <= max_val) {
      vals[r] = 0;
      m++;
      r = m*v;
    }
  }
  for(int i = 0; i < (int)vals.size(); ++i)
    if (vals[i] != 0)
      X.push_back(vals[i]);

  return X;
}


void next_pascal_row(long* previous_row, int previous_row_length, long* next_row) {
  next_row[0] = 1;
  next_row[previous_row_length] = 1;
  for(int i = 1; i < previous_row_length; ++i)
    next_row[i] = previous_row[i-1] + previous_row[i];
}


void pascals_triangle(int rows) {

  long* previous_row = new long[2];
  previous_row[0] = 1;
  previous_row[1] = 1;
  long* current_row;

  for (int row = 3; row < rows; ++row) {

    current_row = new long[row];
    next_pascal_row(previous_row,row-1,current_row);

    // for(int j = 0; j < row; ++j)
    //   cout << current_row[j] << ",";
    // cout << endl;

    delete [] previous_row;
    previous_row = current_row;

  }

  long max_val = 0L;
  for (int j = 0; j < rows; ++j)
    if (current_row[j] > max_val)
      max_val = current_row[j];
  cout << "max value: " << max_val << endl;

   
}

set<long> get_primes_squared(int max_val) {
  vector<long> primes = get_primes((long)sqrt(max_val)+1L);
  set<long> primes_squared;
  for (int i = 1; i < (int)primes.size(); ++i) 
    primes_squared.insert((long)pow(primes[i],2));
  return primes_squared;
}


long sum_squarefree(int rows, set<long> primes_squared) { 

  long sum = 0;
  set<long> squarefree_numbers;
  long* previous_row = new long[2];
  previous_row[0] = 1;
  previous_row[1] = 1;
  long* current_row;
  vector<long> divisors;

  for (int row = 3; row <= rows; ++row) {
    cout << "row = " << row << endl;
    current_row = new long[row];
    next_pascal_row(previous_row,row-1,current_row);

    for (int i = 1; i < row-1; ++i) {
      squarefree_numbers.insert(current_row[i]);        
      divisors = eulerutils::get_divisors(current_row[i]);
      for(int j = 0; j < (int)divisors.size(); ++j) {
        if(primes_squared.count(divisors[j])){ 
          squarefree_numbers.erase(current_row[i]);
          break;
	}
      }
    }
    delete [] previous_row;
    previous_row = current_row;

  }

  for(set<long>::iterator it = squarefree_numbers.begin(); 
      it != squarefree_numbers.end();
      ++it) {
    // cout << *it << endl;
    sum += *it;
  }

  return sum +1 ;
}
  


int main(int argc, char** argv) {

  long max_val = 63205303218876L;
  set<long> primes_squared = get_primes_squared(max_val);
  long sum = sum_squarefree(51,primes_squared);
  cout << endl << "***********" << endl;
  cout << sum << endl;



  // vector<long> divisors = eulerutils::get_divisors(5);
  
  // for(int i = 0; i < (int)divisors.size(); ++i)
  //   cout << divisors[i] << ",";
  // cout << endl;

  // cout << (int)divisors.size() << endl;

  // vector<pair<long,int> > X = eulerutils::get_factors(63205303218876);
  // for(int i = 0; i < (int)X.size(); ++i)
  //   cout << X[i].first << "," << X[i].second << endl;


  
}

