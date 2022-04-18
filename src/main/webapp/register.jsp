<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html lang="en">
<head>
   <link rel="stylesheet" href="../css/bootstrap.min.css"/>
   <script src="../js/bootstrap.min.js"></script>
   <title>Login</title>
</head>
<body>
<div class="container">
  <h1>Registration</h1>

<form action="Login" method="post" style="width:300px">
  <div class="form-group">
    <label for="InputUserName">Last Name:</label>
    <input type="text" class="form-control" name="userName" placeholder="User Name">
  </div>
    <div class="form-group">
      <label for="InputPassword">Last Name:</label>
      <input type="text" class="form-control" name="password" placeholder="Password">
    </div>
  <div class="form-group">
    <label for="InputFirstName">First Name:</label>
    <input type="text" class="form-control" name="firstName" placeholder="First Name">
  </div>
  <div class="form-group">
    <label for="InputLastName">Last Name:</label>
    <input type="text" class="form-control" name="lastName" placeholder="Last Name">
  </div>
    <div class="form-group">
      <label for="InputAddress">Last Name:</label>
      <input type="text" class="form-control" name="address" placeholder="1234 west st">
    </div>
    <div class="form-group">
          <label for="InputPhone">Last Name:</label>
          <input type="text" class="form-control" name="phone" placeholder="555-555-5555">
        </div>

  <button type="submit" class="btn btn-primary">Create</button>
  <button type="submit" class="btn btn-danger">Cancel</button>
</form>
</body>
</html>
