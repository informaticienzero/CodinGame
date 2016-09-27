#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    int N;
    std::cin >> N; std::cin.ignore();
    int Q;
    std::cin >> Q; std::cin.ignore();
    
    std::map<std::string, std::string> valid_extentions;
    for (int i = 0; i < N; i++)
    {
        std::string EXT; // file extension
        std::string MT; // MIME type.
        std::cin >> EXT >> MT; std::cin.ignore();
        
        // We force the extension to be in lower cases for being
        // easier to compare after.
        for (auto & c : EXT)
        {
            c = std::tolower(c);
        }
        
        valid_extentions[EXT] = MT;
    }
    
    for (int i = 0; i < Q; i++)
    {
        std::string FNAME;
        std::getline(std::cin, FNAME);
        
        std::string to_print {"UNKNOWN"};
        
        std::size_t dot_position = FNAME.find_last_of(".");
        if (dot_position != std::string::npos)
        {
            if (dot_position != FNAME.length())
            {
                std::string extention = FNAME.substr(dot_position + 1);
                for (auto & c : extention)
                {
                    c = std::tolower(c);
                }
                
                auto it = valid_extentions.find(extention);
                if (it != std::end(valid_extentions))
                {
                    to_print = it->second;
                }
            }
        }
        
        std::cout << to_print << std::endl;
    }
}
