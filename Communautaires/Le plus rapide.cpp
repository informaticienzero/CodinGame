#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main()
{
    int N;
    std::cin >> N; std::cin.ignore();
    
    std::vector<std::string> values;
    for (int i = 0; i < N; i++)
    {
        std::string t;
        std::cin >> t; std::cin.ignore();
        values.push_back(t);
    }
    
    std::sort(std::begin(values), std::end(values));
    std::cout << values[0] << std::endl;
}