class Exam
{
	public static void main(String[] args) {
		String[] a = new String[2];
		Object[] b = a;
		a[0] = "hi";
		b[1] = Integer.valueOf(53).toString();
		// b[1] = Integer.valueOf(42);

		System.out.println("a[0]: " + a[0]);
		System.out.println("a[1]: " + a[1]);
		System.out.println("b[1]: " + b[1]);
	}
}

