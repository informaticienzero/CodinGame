#include <iostream>
#include <limits>
#include <string>
#include <vector>

int main()
{
    std::string MESSAGE;
    std::getline(std::cin, MESSAGE);
    
    const auto size = std::numeric_limits<char>::digits;
    std::vector<bool> bits;
    for (auto c : MESSAGE)
    {
        for (int i = size - 1; i >= 0; --i)
        {
            bits.push_back((c >> i) & 0x01);
        }
    }
    
    std::string to_print {};
    bool previous {false};
    bool is_first_iteration {true};
    for (auto bit : bits)
    {
        // Is the previous one was the same bit than now.
        if (!is_first_iteration && previous == bit)
        {
            to_print += "0";
        }
        // For each case, we check if we have to add a space before the string or not.
        else
        {
            if (bit)
            {
                if (!is_first_iteration)
                {
                    to_print += " 0 0";
                }
                else
                {
                    to_print += "0 0";
                }
            }
            else
            {
                if (!is_first_iteration)
                {
                    to_print += " 00 0";
                }
                else
                {
                    to_print += "00 0";
                }
            }
        }
        
        previous = bit;
        is_first_iteration = false;
    }
    
    std::cout << to_print << std::endl;
}
