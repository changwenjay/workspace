class Singleton
{
public:
   static Singleton *getInstance();
   static void doSomething();

private:
   Singleton() {};
   static Singleton *_instance;

};

