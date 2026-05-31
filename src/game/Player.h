#ifndef PLAYER_H
#define PLAYER_H

#include <string>

class Player {
private:
    std::string name;
    int money;
public:
    Player(const std::string& name);
    void setMoney(int amount);
    int getMoney() const;
    std::string getName() const;
};

#endif