#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> split(const std::string & to_split, char delimitor)
{
    std::vector<std::string> result;
    std::string part = to_split;
    
    std::size_t position = to_split.find(delimitor);
    while (position != std::string::npos)
    {
        result.push_back(part.substr(0, position));
        part = part.substr(position + 1);
        position = part.find(delimitor);
    }
    
    result.push_back(part);
    
    using std::sort;
    sort(result.begin(), result.end());
    result.erase( std::unique(result.begin(), result.end()), result.end() );
    return result;
}

int main()
{
    int n;
    std::cin >> n; std::cin.ignore();
    std::string temps;
    std::getline(std::cin, temps);
    
    int closest = 5527;
    std::cerr << temps << std::endl;
    
    if (n != 0)
    {
        std::vector<std::string> results = split(temps, ' ');
        
        for (auto temperature_string : results)
        {
            int temperature = std::stoi(temperature_string);
            if (temperature >= 0 && temperature <= std::abs(closest))
            {
                closest = temperature;
            }
            else
            {
                if (std::abs(temperature) < std::abs(closest))
                {
                    closest = temperature;
                }
            }
        }
    }
    else
    {
        closest = 0;
    }

    std::cout << closest << std::endl;
}
