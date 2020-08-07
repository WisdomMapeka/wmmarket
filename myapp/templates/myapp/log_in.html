
<?php
$host = "localhost";
$user = "root";
$pass = "1234567wiz";

$email = " ";
$password = " ";

if(isset($_POST["Login"])){
    if(empty($_POST["email"]) || empty($_POST["password"])){
        $err_ = "Fill all fields";
    }else{
        $email =  $_POST["email"];
        $password =  $_POST["password"];
    }
   

}

?>




<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="log_in.css">
	<script type="text/javascript" src="index.js"></script>
</head>
<body onresize="myfunc()">
	<div class="logo">MWJ Soulutions</div>
	<header>
		<div class="header-login-text">
			Enjoy The Ultimate Experience
		</div>
	</header>
	<div class="log-in-home"><a href="index.php"> Go To Home Page</a></div>
	<div class="login-form">
		
		<div class="invalid">
			<?php if (isset($err_)) {
			echo $err_;
		     } ?>	
		</div>
		<div class="invalid">
			<?php if (isset($err_message)) {
			echo $err_message;
		     } ?>	
		</div>
		<form action="log_in.php" method="POST">
			<table>
				<tr>
					<td>Email or Username</td>
					<td><input type="text" name="email"></td>
				</tr>
				<tr>
					<td>password</td>
					<td><input type="text" name="password"></td>
				</tr>
				<tr>
					<td>
						<input type="submit" name="Login" value="Login">
					</td>
				</tr>
			</table>
		</form>
		<div class="log-in-crerate-account"> <a href="signup_account.php">Create an account</a> </div>
	</div>
	<div id="div"></div>
	<div class="foot">MWJ Soulutions &copy; 2019</div>
</body>
</html>


<?php 
    $conn = new PDO("mysql:host=$host;dbname=mwj", $user, $pass);
    // set the PDO error mode to exception
    $dat_email = "select * from users where email='wis@gmail.com' ";
      foreach($conn->query($dat_email) as $row){
      $mail =  $row["email"] ;
      $pass = $row["password"];
      $user_first_name = $row["firstName"];
      $user_last_name = $row["lastName"];
      }

      if($mail===$email && $pass===$password){
      	 session_start();
        $_SESSION["email"] = $mail;
        $_SESSION["firstName"] = $user_first_name;
        $_SESSION["lastName"] = $user_last_name;
        header("Location:index.php");
      }else{
        $err_message = "Ivalid password user combination. Try again";
      }

$conn = null;

?>


