package com.cs360;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.PreparedStatement;
import java.sql.SQLException;

@WebServlet("/Register")
public class RegisterServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String email = req.getParameter("email");
        String password = req.getParameter("password");
        String lastName = req.getParameter("lastName");
        String firstName = req.getParameter("firstName");
        String address = req.getParameter("address");
        String phone = req.getParameter("phone");
        try {
            PreparedStatement preparedStatement = DBConnection.getConnection()
                .prepareStatement("INSERT INTO customer (Email, Password, LastName, FirstName, Address, Phone, Router) " +
                        "VALUES (?, ?, ?, ?, ?, ?, true)");

            preparedStatement.setString(1, email);
            preparedStatement.setString(2, password);
            preparedStatement.setString(3, lastName);
            preparedStatement.setString(4, firstName);
            preparedStatement.setString(5, address);
            preparedStatement.setString(6, phone);
            preparedStatement.executeUpdate();
        } catch (SQLException x) {
            x.printStackTrace();
        }

        resp.sendRedirect("login.jsp");

    }
}
