#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    int lightX;
    int lightY;
    int initialTX;
    int initialTY;
    std::cin >> lightX >> lightY >> initialTX >> initialTY; std::cin.ignore();
    
    int thorX = initialTX;
    int thorY = initialTY;

    while (1)
    {
        int remainingTurns;
        std::cin >> remainingTurns; std::cin.ignore();

        std::string directionX {};
        std::string directionY {};

        if (thorX > lightX)
        {
            directionX = "W";
            --thorX;
        }
        else if (thorX < lightX)
        {
            directionX = "E";
            ++thorX;
        }
        
        if (thorY > lightY)
        {
            directionY = "N";
            --thorY;
        }
        else if (thorY < lightY)
        {
            directionY = "S";
            ++thorY;
        }
        
        std::cout << directionY + directionX << std::endl;
    }
}
