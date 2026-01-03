// Basic Data Types
// https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem?isFullScreen=true
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a;
    long b;
    std::string c;
    float d;
    double e;
    cin >> a >> b >> c >> d >> e;
    cout << a <<std::endl;
    cout << b << std::endl;
    cout << c << std::endl;
    cout << std::fixed << std::setprecision(3) << d << std::endl;
    cout << std::fixed << std::setprecision(9) << e << std::endl;
    
    return 0;
}
