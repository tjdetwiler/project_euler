#include <iostream>
#include <set>
#include <stdint.h>
#include <math.h>
#include "utils.h"
#include <algorithm>


vector<long> eulerutils::get_prime_factors(long value) {
  vector<long> factors;
  long d = 2;
  while (value > 1) {
    while ( value % d == 0 ) {
      factors.push_back(d);
      value = value/d;
    }
    d++;
    if(d*d > value) {
      if ( value > 1)
        factors.push_back(value);
      break; 
    }
  }
  return factors;
}


vector< pair< long,int > > eulerutils::get_factors(long value) {
  vector<long> pfactors = get_prime_factors(value);
  std::sort(pfactors.begin(),pfactors.end());
  vector< pair< long,int> > factor_count_pairs;
  pair<long,int> factor_count_pair; 
  set<long> factors;

  for(int i = 0; i < (int)pfactors.size(); ++i) {
    if (factors.count(pfactors[i]))
      continue;

    factor_count_pair.first = pfactors[i];
    factor_count_pair.second =(int) std::count(pfactors.begin(),pfactors.end(),pfactors[i]);    

    factor_count_pairs.push_back(factor_count_pair);
    factors.insert(pfactors[i]);
  }
  return factor_count_pairs;
}

vector<long> eulerutils::get_divisors(long value) {
  vector<long> divisors;
  vector< pair<long,int> > factor_count_pairs;
  factor_count_pairs = eulerutils::get_factors(value);
  long f [(int)factor_count_pairs.size()];
  for (int i = 0; i < (int)factor_count_pairs.size(); ++i)
    f[i] = 0L;

  long product;
  int i;

  while(true) {
    product = 1;
    for (int j = 0; j < (int)factor_count_pairs.size(); ++j)
      product *= (long)pow(factor_count_pairs[j].first,f[j]);
    divisors.push_back(product);
    i = 0;
    while(true) {
      f[i] += 1L;
      if (f[i] <= (long)factor_count_pairs[i].second)
        break;
      f[i] = 0L;
      i++;
      if (i >= (int)factor_count_pairs.size())
        return divisors;
    }
  }
  

}


