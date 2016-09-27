#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    int N;
    std::cin >> N; std::cin.ignore();
    std::vector<int> powers;
    
    for (int i = 0; i < N; i++)
    {
        int Pi;
        std::cin >> Pi; std::cin.ignore();
        
        powers.push_back(Pi);
    }
    
    using std::sort;
    sort(std::begin(powers), std::end(powers));
    
    int shortest_difference {1000000};
    const std::size_t size = powers.size();
    for (std::size_t i = 0; i < size; ++i)
    {
        if (i != 0)
        {
            int previous = powers[i - 1];
            int difference = std::abs(previous - powers[i]);
            
            if (difference < shortest_difference)
            {
                shortest_difference = difference;
            }
        }
    }
    
    std::cout << shortest_difference << std::endl;
}
