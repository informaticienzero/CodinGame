#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

struct Node
{
    int x, y;
    int right_x, right_y;
    int below_x, below_y;
    
    Node(int x, int y)
    : x(x), y(y), right_x(-1), right_y(-1), below_x(-1), below_y(-1)
    {
        
    }
    
    friend std::ostream & operator<<(std::ostream & out, Node const & node)
    {
        return out << node.x << " " << node.y << " " << node.right_x
        << " " << node.right_y << " " << node.below_x << " " << node.below_y;
    }
    
    friend inline bool operator==(Node const & lhs, Node const & rhs)
    {
        return lhs.x == rhs.x && lhs.y == rhs.y;
    }
    
    friend inline bool operator!=(Node const & lhs, Node const & rhs)
    {
        return !(lhs == rhs);
    }
    
    inline bool is_right_of_node(Node node) const noexcept
    {
        return this->x > node.x && this->y == node.y;
    }
    
    inline bool is_below_of_node(Node node) const noexcept
    {
        return this->y > node.y && this->x == node.x;
    }
    
    inline bool is_right_setted() const noexcept
    {
        return this->right_x != -1 && this->right_y != -1;
    }
    
    inline bool is_below_setted() const noexcept
    {
        return this->below_x != -1 && this->below_y != -1;
    }
};

int main()
{
    int width; // the number of cells on the X axis
    std::cin >> width; std::cin.ignore();
    int height; // the number of cells on the Y axis
    std::cin >> height; std::cin.ignore();
    
    int x = 0; int y = 0;
    std::vector<Node> nodes;
    
    for (int i = 0; i < height; i++)
    {
        std::string line; // width characters, each either 0 or .
        std::getline(std::cin, line);
        
        // Restart the x index.
        x = 0;
        
        for (auto c : line)
        {
            if (c == '0')
            {
                Node current(x, y);
                
                if (!nodes.empty())
                {
                    for (auto & node : nodes)
                    {
                        if (current.is_right_of_node(node) && !node.is_right_setted())
                        {
                            node.right_x = current.x;
                            node.right_y = current.y;
                        }
                        
                        if (current.is_below_of_node(node) && !node.is_below_setted())
                        {
                            node.below_x = current.x;
                            node.below_y = current.y;
                        }
                    }
                }
                
                nodes.push_back(current);
            }
            
            ++x;
        }
        
        ++y;
    }
    
    for (auto node : nodes)
    {
        std::cout << node << std::endl;
    }
}
