#include "Singleton.h"
#include <iostream>

Singleton *Singleton::_instance = 0;

Singleton *Singleton::getInstance()
{
	if (_instance == 0) {
		_instance = new Singleton();
		std::cout << "creating singleton...\n";
	}
	return _instance;
}

void Singleton::doSomething()
{
	std::cout << "do something...\n";
}

int main()
{
	Singleton::getInstance()->doSomething();
	Singleton::getInstance()->doSomething();
	Singleton::getInstance()->doSomething();

	return 0;
}

