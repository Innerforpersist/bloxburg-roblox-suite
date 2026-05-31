#include <iostream>
#include "game/Player.h"
#include "game/Automation.h"

int main() {
    Player player("BuilderPro");
    player.setMoney(5000);

    Automation autoBuilder;
    autoBuilder.buildHouse(player);

    std::cout << "Player " << player.getName() << " now has $" << player.getMoney() << std::endl;
    return 0;
}