package com.cs360;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


public class LoginDao {

    public boolean validate(Login login) throws ClassNotFoundException {
        boolean status = false;

        Class.forName("com.mysql.jdbc.Driver");

        try {
            var connection = DBConnection.getConnection();
             // Step 2:Create a statement using connection object
            PreparedStatement preparedStatement = connection
                     .prepareStatement("SELECT * FROM customer where FirstName = ? and LastName = ? ");
            //var firstName = login.getFirstName();
            //var lastName = login.getLastName();
            //System.out.println("Login.java attempt " + firstName + " " + lastName);
            //preparedStatement.setString(1, firstName);
            //preparedStatement.setString(2, lastName);

            System.out.println(preparedStatement);
            ResultSet rs = preparedStatement.executeQuery();
            status = rs.next();

        } catch (SQLException e) {
            // process sql exception
            printSQLException(e);
        }
        return status;
    }

    private void printSQLException(SQLException ex) {
        for (Throwable e: ex) {
            if (e instanceof SQLException) {
                e.printStackTrace(System.err);
                System.err.println("SQLState: " + ((SQLException) e).getSQLState());
                System.err.println("Error Code: " + ((SQLException) e).getErrorCode());
                System.err.println("Message: " + e.getMessage());
                Throwable t = ex.getCause();
                while (t != null) {
                    System.out.println("Cause: " + t);
                    t = t.getCause();
                }
            }
        }
    }
}
