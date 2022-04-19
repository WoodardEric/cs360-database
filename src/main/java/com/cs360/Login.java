package com.cs360;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;

@WebServlet("/Login")
public class Login extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        if (req.getParameter("new") != null){
            resp.sendRedirect("register.jsp");
            return;
        }
        String email = req.getParameter("email");
        String password = req.getParameter("password");
        System.out.println("Login attempt: " + email);
        Connection con = DBConnection.getConnection();
        try {
            PreparedStatement preparedStatement = con.prepareStatement("select password from customer where email = ?");
            preparedStatement.setString(1, email);
            ResultSet rs = preparedStatement.executeQuery();
            rs.next();
            if (rs.getString("password").equals(password)) {
                System.out.println("Login Sucessfully");
            }
        } catch (SQLException ex) {
            Logger.getLogger(Login.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
