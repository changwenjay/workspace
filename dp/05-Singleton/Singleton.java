public class Singleton
{
	private static Singleton _instance = null;

	private Singleton() {
		System.out.println("Creating instance...");
	}

	public static Singleton getInstance() {
		if (_instance == null) {
			_instance = new Singleton();
		}
		return _instance;
	}

	public static void doSomething() {
		System.out.println("Doing something...");
	}

	public static void main(String args[]) {
		Singleton.getInstance().doSomething();
		Singleton.getInstance().doSomething();
		Singleton.getInstance().doSomething();
	}

}

