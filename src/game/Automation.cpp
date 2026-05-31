#include "Automation.h"
#include <iostream>

void Automation::buildHouse(Player& player) {
    const int houseCost = 2500;
    if (player.getMoney() >= houseCost) {
        player.setMoney(player.getMoney() - houseCost);
        std::cout << "House built successfully!" << std::endl;
    } else {
        std::cout << "Not enough money to build a house." << std::endl;
    }
}