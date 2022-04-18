<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html lang="en">
<head>
   <link rel="stylesheet" href="../css/bootstrap.min.css"/>
   <script src="../js/bootstrap.min.js"></script>
   <title>Login</title>
</head>
<body>
<div class="container">
  <h1>Login</h1>
<form action="Login" method="post" style="width:300px">
  <div class="form-group">
    <label for="InputFirstName">First Name:</label>
    <input type="text" class="form-control" name="firstName" placeholder="First Name">
  </div>
  <div class="form-group">
    <label for="InputLastName">Last Name:</label>
    <input type="text" class="form-control" name="lastName" placeholder="Last Name">
  </div>

  <button type="submit" class="btn btn-primary" name="login">Login </button>
  <button type="submit" class="btn btn-secondary" name="new">Create New Account</button>
</form>
</body>
</html>
