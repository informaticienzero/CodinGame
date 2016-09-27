#include <algorithm>
#include <iostream>
#include <numeric>
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
    std::string N;
    std::getline(std::cin, N);
    
    N.erase(0, 1);
    N.erase(N.length() - 1, 1);
    
    auto && values = split(N, ',');
    std::vector<int> numbers;
    
    for (auto value : values)
    {
        numbers.push_back(std::stoi(value));
    }
    std::sort(std::begin(numbers), std::end(numbers));
    
    int previous = numbers[0];
    int first = 0;
    std::size_t count = 0;
    
    std::vector<int> ranges;
    const std::size_t size = numbers.size();
    for (auto i = 0u; i < size; ++i)
    {
        if (numbers[i] - previous == 1)
        {
            if (count == 0)
            {
                first = previous;
            }
            
            previous = numbers[i];
            ++count;
            
            // If last turn.
            if (i == size - 1)
            {
                if (count >= 2)
                {
                    ranges.push_back(first);
                    ranges.push_back(previous);
                }
            }
        }
        else
        {
            if (count >= 2)
            {
                ranges.push_back(first);
                ranges.push_back(previous);
            }
            
            count = 0;
            previous = numbers[i];
        }
    }
    
    std::string result;
    for (int i = 0; i < size; ++i)
    {
        if (!ranges.empty())
        {
            auto it = std::find(std::begin(ranges), std::end(ranges), numbers[i]);
            if (it != std::end(ranges))
            {
                result += std::to_string(ranges[0]) + "-" + std::to_string(ranges[1]) + ",";
                
                while(numbers[i] != ranges[1])
                {
                    ++i;
                }
                ranges.erase(std::begin(ranges), std::begin(ranges) + 2);
            }
            else
            {
                result += std::to_string(numbers[i]) + ",";
            }
        }
        else
        {
            result += std::to_string(numbers[i]) + ",";
        }
    }
    
    result.erase(result.length() - 1);
    std::cout << result << std::endl;
}