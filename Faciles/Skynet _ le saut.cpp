#include <iostream>

int main()
{
    int road; // the length of the road before the gap.
    std::cin >> road; std::cin.ignore();
    int gap; // the length of the gap.
    std::cin >> gap; std::cin.ignore();
    int platform; // the length of the landing platform.
    std::cin >> platform; std::cin.ignore();

    while (1)
    {
        int speed; // the motorbike's speed.
        std::cin >> speed; std::cin.ignore();
        int coordX; // the position on the road of the motorbike.
        std::cin >> coordX; std::cin.ignore();
        
        // If the motorbike is still on road.
        if (road - (speed + coordX) > 1)
        {
            // If our speed is not suffisant to cross the length oh gap,
            // we must increase it.
            if (speed < gap + 1)
            {
                std::cout << "SPEED" << std::endl;
            }
            else if (speed > gap + 1)
            {
                std::cout << "SLOW" << std::endl;
            }
            else
            {
                std::cout << "WAIT" << std::endl;
            }
        }
        else
        {
            // If our next position is greater than length of road + length
            // of gap, it means we're on the platform.
            // Or if our next move is at the end of road.
            if (coordX + speed > road + gap || coordX + speed == road)
            {
                std::cout << "SLOW" << std::endl;
            }
            else
            {
                std::cout << "JUMP" << std::endl;
            }
        }
    }
}
