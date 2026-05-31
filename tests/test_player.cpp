#include "../src/game/Player.h"
#include <cassert>

void testPlayerMoney() {
    Player player("TestPlayer");
    player.setMoney(1000);
    assert(player.getMoney() == 1000);
    assert(player.getName() == "TestPlayer");
}

int main() {
    testPlayerMoney();
    return 0;
}