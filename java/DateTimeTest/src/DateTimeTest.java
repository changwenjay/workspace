import java.time.Instant;
import java.time.LocalDateTime;
import java.time.Period;

public class DateTimeTest {
	static Instant ist = Instant.now();
	static LocalDateTime ldt = LocalDateTime.now();
	static LocalDateTime ldt2 = LocalDateTime.now();
	
	public static void main(String args[]) {
		System.out.println(ist);
		System.out.println(ist.plus(Period.ofDays(1)));
		
		System.out.println(ldt);
		System.out.println(ldt.plus(Period.ofDays(1)));
		
		System.out.println(ldt2);
		System.out.println(ldt2.plusDays(1));
		
		System.out.println(
				ldt.getYear() + "-"
				+ ldt.getMonthValue() + "-"
				+ ldt.getDayOfMonth());
		
	}
}
