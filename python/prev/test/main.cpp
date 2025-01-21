#include<iostream>
#include<string>

class Entity
{
    public:
    Entity(){
        std::cout<<"Created Entity!" <<std::endl;
    }
    
    ~Entity(){
        std::cout<< "Destroyed Entity!" <<std::endl;
    }

};

int main(){



    {
        Entity e;
    }

    std::cin.get();
}