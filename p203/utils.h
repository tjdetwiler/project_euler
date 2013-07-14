#include <stdio.h>
#include <vector>
#include <string>
#include <stdint.h>

using namespace std;

namespace eulerutils{
  vector< pair<long,int> > get_factors(long value);
  vector<long> get_prime_factors(long value);
  vector<long> get_divisors(long value);

}

