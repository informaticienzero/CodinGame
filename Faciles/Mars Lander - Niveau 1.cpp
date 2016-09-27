#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> positions_y;
    
    int surfaceN;
    std::cin >> surfaceN; std::cin.ignore();
    for (int i = 0; i < surfaceN; i++)
    {
        int landX;
        int landY;
        std::cin >> landX >> landY; std::cin.ignore();
        
        positions_y.push_back(landY);
    }

    int vitess_to_apply = 2;
    int max_speed = 40;
    
    while (1)
    {
        int X;
        int Y;
        int hSpeed; 
        int vSpeed;
        int fuel;
        int rotate;
        int power;
        std::cin >> X >> Y >> hSpeed >> vSpeed >> fuel >> rotate >> power; std::cin.ignore();
        
        const int ground_y = positions_y[X];
        
        if (std::abs(vSpeed) >= max_speed)
        {
            vitess_to_apply = 4;
        }
        else
        {
            vitess_to_apply = 0;
        }

        std::cout << "0 " + std::to_string(vitess_to_apply) << std::endl;
    }
}
