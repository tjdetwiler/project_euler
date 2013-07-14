#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <vector>
#include "utils.h"
#include <iostream>
#include <set>
#include <cmath>

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
  
bool is_int(double value) {
  double eps = 1e-19;
  if(std::abs(floor(value) - value) < eps)
    return true;
  return false;
}

long count_psquares(long max_val) {
  long n = 1L;
  long sq = 1L;
  long count = 0L;
  while(sq < max_val) {
    count++;
    n++;
    sq = (long)pow(n,2);
  }
  return count;
}

int main(int argc, char** argv) {

  // long max_val = 75424722;
  // long sq;
  // for(long n = 2; n < max_val+1; ++n )
  //   sq = (long)pow(n,2);

  vector<long> divisors;
  int max_val = (int)64e6;
  long sum = 0L;
  unsigned long total_sum = 0L;
  for ( int n = 2; n < max_val; ++n ) {
    // if ( n % 100000 == 0)
    //   cout << "n: " << n << endl;
    sum = 0L;
    divisors = eulerutils::get_divisors(n);
    for (int j = 0; j < (int)divisors.size(); ++j)
      sum += (long)pow(divisors[j],2);      
    if (is_int(sqrt(sum))){
      cout << n << endl;
      total_sum += n;
    }

  }
  // cout << count_psquares(5688888803185771);
  cout << "***********\n" << total_sum << endl; 
  cout << "***********\n" << total_sum +1 << endl; 
  cout << "done.\n";
}

