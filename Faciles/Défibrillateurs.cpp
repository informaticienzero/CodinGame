#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

enum Line
{
    NUMBER, NAME, ADDRESS, SEMICOLON, LONGITUDE, LATITUDE
};

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
    return result;
}

std::string change_decimal_culture(const std::string & to_change)
{
    std::string result = to_change;
    const std::size_t position = result.find(',');
    if (position != std::string::npos)
    {
        result[position] = '.';
    }
    return result;
}

int main()
{
    std::string LON;
    std::cin >> LON; std::cin.ignore();
    LON = change_decimal_culture(LON);
    
    std::string LAT;
    std::cin >> LAT; std::cin.ignore();
    LAT = change_decimal_culture(LAT);
    
    int N;
    std::cin >> N; std::cin.ignore();
    
    double shortest_distance {5000000};
    std::string closest_point {};
    for (int i = 0; i < N; i++)
    {
        std::string DEFIB;
        std::getline(std::cin, DEFIB);
        
        std::vector<std::string> informations {split(DEFIB, ';')};
        double latitude {std::stod(change_decimal_culture(informations[LATITUDE]))};
        double longitude {std::stod(change_decimal_culture(informations[LONGITUDE]))};
        
        double lon {std::stod(LON)};
        double lat {std::stod(LAT)};
        
        double x = (longitude - lon) * std::cos((latitude + lat) / 2.);
        double y = (latitude - lat);
        double distance = std::sqrt(x*x + y*y) * 6371;
        
        if (distance < shortest_distance)
        {
            shortest_distance = distance;
            closest_point = informations[NAME];
        }
    }
    
    std::cout << closest_point << std::endl;
}
