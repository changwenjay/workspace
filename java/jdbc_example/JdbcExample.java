// STEP 1. Import required packages
import java.sql.*;

public class JdbcExample {
	// JDBC driver name and database URL
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
	static final String DB_URL = "jdbc:mysql://localhost/wenztest";

	//  Database credentials
	static final String USER = "wenjay";
	static final String PASS = "dcc";

	public static void main(String[] args) {

		Connection conn = null;
		Statement stmt = null;

		try{
			//STEP 2: Register JDBC driver
			// Class.forName("com.mysql.cj.jdbc.Driver");
			Class.forName("org.mariadb.jdbc.Driver");
			// Class.forName(JDBC_DRIVER);

			//STEP 3: Open a connection
			// System.out.println("Connecting to database...");
			conn = DriverManager.getConnection(DB_URL, USER, PASS);

			//STEP 4: Execute a query
			// System.out.println("Creating statement...");
			stmt = conn.createStatement();
			String sql;
			sql = "SELECT name_first, name_last, age, phone FROM employee order by age desc";
			ResultSet rs = stmt.executeQuery(sql);
			
			//STEP 5: Extract data from result set
			while(rs.next()){
			//Retrieve by column name
				int age = rs.getInt("age");
				String first = rs.getString("name_first");
				String last = rs.getString("name_last");
				String phone = rs.getString("phone");

				//Display values
				System.out.print(first);
				System.out.print(",\t" + last);
				System.out.print(",\t" + age);
				System.out.println(",\t" + phone);
			}
			//STEP 6: Clean-up environment
			rs.close();
			stmt.close();
			conn.close();
		}catch(SQLException se){
			//Handle errors for JDBC
			se.printStackTrace();
		}catch(Exception e){
			//Handle errors for Class.forName
			e.printStackTrace();
		}finally{
			//finally block used to close resources
			try{
				if(stmt!=null)
					stmt.close();
			}catch(SQLException se2){
			}// nothing we can do

			try{
				if(conn!=null)
					conn.close();
			}catch(SQLException se){
				se.printStackTrace();
			}//end finally try
		}//end try

		System.out.println("Goodbye!");
	}//end main
}//end FirstExample

