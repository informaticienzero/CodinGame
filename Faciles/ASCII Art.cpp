#include <array>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>

struct Letter
{
    char associated_char;
    std::vector<std::string> parts;
};

int main()
{
    int L;
    std::cin >> L; std::cin.ignore();
    int H;
    std::cin >> H; std::cin.ignore();
    
    std::string T;
    std::getline(std::cin, T);
    
    // First preparing the line to print.
    for (char & c : T)
    {
        if (isalpha(c))
        {
            c = toupper(c);
        }
        else
        {
            c = '?';
        }
    }
    
    std::vector<std::string> rows;
    for (int i = 0; i < H; i++)
    {
        std::string ROW;
        std::getline(std::cin, ROW);
        
        rows.push_back(ROW);
    }
    
    constexpr std::size_t char_number = 27;
    std::array<Letter, char_number> letters;
    for (std::size_t i = 0; i < char_number; ++i)
    {
        // Get the rows one by one, from 0 to H.
        // To divise them, we advance each turn by L.
        for (std::size_t j = 0; j < H; ++j)
        {
            letters[i].parts.push_back(rows[j].substr(i * L, L));
        }
        
        letters[i].associated_char = 'A' + i;
    }
    
    std::vector<Letter> to_print;
    for (char c : T)
    {
        // We know that '?' is the last one of the letters array.
        if (c == '?')
        {
            to_print.push_back(letters[char_number - 1]);
        }
        else
        {
            to_print.push_back(letters[c - 'A']);
        }
    }

    const std::size_t size = to_print.size(); 
    for (std::size_t line = 0; line < H; ++line)
    {
        for (std::size_t i = 0; i < size; ++i)
        {
            std::cout << to_print[i].parts[line];
        }
        std::cout << std::endl;
    }
}
