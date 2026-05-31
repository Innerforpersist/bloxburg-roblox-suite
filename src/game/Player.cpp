#include "Player.h"

Player::Player(const std::string& name) : name(name), money(0) {}

void Player::setMoney(int amount) {
    money = amount;
}

int Player::getMoney() const {
    return money;
}

std::string Player::getName() const {
    return name;
}