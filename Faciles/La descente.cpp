#include <iostream>

int main()
{
    while (1)
    {
        int spaceX;
        int spaceY;
        std::cin >> spaceX >> spaceY; std::cin.ignore();
        
        int highest_mountain = 0;
        int highest_mountain_position = 0;
        
        for (int i = 0; i < 8; i++)
        {
            int mountainH;
            std::cin >> mountainH; std::cin.ignore();
            
            if (mountainH > highest_mountain)
            {
                highest_mountain = mountainH;
                highest_mountain_position = i;
            }
        }
        
        if (spaceX == highest_mountain_position)
        {
            std::cout << "FIRE" << std::endl;
        }
        else
        {
            std::cout << "HOLD" << std::endl;
        }
    }
}
