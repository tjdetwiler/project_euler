#include <iostream>
#include <math.h>
#include <cmath>

using namespace std;

static inline bool is_int( long double T) {
  long double eps = 1e-60;
  return ( std::abs( floor(T) - T ) < eps  );
}

// static inline bool has_integer_area(int a, int b, int c) {
//   int w, x, y, z;
//   double T;
//   w = a + b + c;
//   x = c - a + b;
//   y = c + a - b;
//   z = a + b - c;
//   T = .25*sqrt(w*x*y*z);
//   return is_int(T);
// }


static inline bool has_integer_area(long double a, long double b, long double c) {
  long double s = (a + b + c) /2.0;
  long double T;
  T = sqrt(s*(s-a)*(s-b)*(s-c));
  return is_int(T);
}


static inline int has_almost_eq_triangle(int a_int) {
  long double a = (long double)a_int;
  if ( has_integer_area(a+1.0,a,a) ){ 
    // cout << a << "," << a << "," << a+1 << " : ";
    return 3*a_int + 1;
  }
  if ( has_integer_area(a,a,a-1.0) ){ 
    // cout << a << "," << a << "," << a- 1 << " : " ;
    return 3*a_int -1;
  }
  return 0;
}

long solve(){
  int a = 4;
  int max_perimeter = (int)1e9 + 2;
  int perimeter = 3 * a + 1;
  int count = 0;
  long perimeter_sum = 0;
  int result;
  while (perimeter < max_perimeter) {
    // if (a % (int)1e7 == 0)
    //   cout << "a = " << a << endl;

    result = has_almost_eq_triangle(a);
    if (result){
      perimeter_sum += result;
      cout << result << endl;
    }
    a++;
    perimeter = 3 * a + 1;
  }

  return perimeter_sum;
}


int main(int argc, char** argv){
  long ans = solve();
  cout << "*****************\n";
  cout << "ans = " << ans << endl;
}


