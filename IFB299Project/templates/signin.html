<!DOCTYPE HTML SYSTEM>
<html>
    <head>
        <meta CHARSET="UTF-8">
          <meta name="description" content="login page of searcho">
          <meta name="keywords" content="HTML,CSS,PHP,JavaScript,MYsql">
          <meta name="author" content="Kishan virani, Shivam  sachdeva ">
    <title>Sign in</title>
        <link href="css/maincss.css" rel="stylesheet" type="text/css"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <script src="javascript/mainjavascript.js"></script>

    </head>

    <body>

        <?php
        //require 'PHP/connect.php';

                foreach ($_POST as $key => $value) {
                    //echo "($key) => ($value)<br/>";
                }
      $servername = "fastapps04.qut.edu.au";
        $username = "n9307834";
        $pass = "password";


        try{


        $pdo= new PDO("mysql:host=$servername;dbname=n9307834", $username,$pass);

            //echo "pass";

        } catch(PDOException $e){
            //echo "failed to connect";
        }
        foreach ($_POST as $key => $value) {
            //echo "($key) => ($value)<br/>";

        }

        session_start();

        require 'PHP/validate.php';


        $errors = array();
        $emailerr = "";

        $email  = $password = "";
        validateEmail($errors, $_POST, 'signinemail');
        validatepassword($errors, $_POST, 'signinpassword');

        if ($errors) {
            //echo 'Errors:<br/>';
            foreach ($errors as $field => $error){
                //echo "$field $error</br>";
            }
        } else {
            //echo 'Data ok';
        }


        if(isset($_POST['signin'])){

            $login = $pdo->prepare("SELECT * FROM userDB WHERE email = :email");
            $login->bindParam(':email', $_POST['signinemail']);
            $login->execute();

            $emailoflogin = $login->fetch(PDO::FETCH_ASSOC);

            if($emailoflogin === false){

                die('Username is not registered.');
            } else{

                //varifies user password with our database password then user can login.
                $Passwordoflogin = password_verify($_POST['signinpassword'], $emailoflogin['password']);

                //echo $_POST['signinpassword'];
                //echo $emailoflogin['password'];

                if($Passwordoflogin){
                    //if  password of login is in our database
                    $_SESSION['userlogin'] = time();
                    $_SESSION['username'] = $emailoflogin['name'];
                    $_SESSION['user_id_on_database'] = $emailoflogin['ID'];
                    $_SESSION['signin']=true;
                    //location : 'cab230.php';
                    header('Location: cab230.php');
                    } else{
                        die('Email and Password are not available in database');
                    }

                }
            }

        ?>

        <div id="top-header">
            <div id="topbar-content">
                <div id="logo">
                <img id="logo-image"src="image/logo.png">
                </div>
                <div>
                    <h1><a href="cab230.php" id="logo-name">SEARCHO</a></h1>
                </div>
                    <input id="search-box" type="text" placeholder=" Search Here" >
                    <button id="search-button" type="submit" value="submit" name="search-button"><i class="fa fa-search" aria-hidden="true" style="font-size:45px;"></i></button>
                <div id="signin-buttons">
                    <a href="cab230.php">Search</a>
                  <?php
                  if(isset($_SESSION['signin'])){
                    echo '<a href="logoutuser.php">Hello ',$_SESSION['username'],' Logout</a>';

                  }else{
                      echo '<a href="loginpage.php">Sign in</a>';
                      echo '<a href="signinpage.php#signup">Sign up</a>';
                  }
                  ?>
                </div>
            </div>
        </div>
        <hr>
        <div id="main-content">
            <form id="signin" name="signin" onsubmit="return validateFormSignin()" method="post">
                <h1>Sign in</h1>
                User ID:
                <br>
                <input type="text" placeholder=" Please Enter Email" class="signininput" id="userid" name="signinemail"><span id="emailsigninvalidator" class="validatormsgeml">  </span>
                <br>
                <br>
                Password:
                <br>
                <input type="password" placeholder="Password"  class="signininput"id="signinpassword" name="signinpassword" ><span class="validatorsigninmsgpwd" id="passvalidator"></span>
                <br>
                <button id="signinsubmit" type="submit"  value="signin" name="signin">Sign in</button>
                <p id="forgotpswrd"><a href="">Forgot Password ?</a>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<a href="signinpage.php#signup" id="register">Register Now</a></p>
                <?php
                if ($errors) {

                echo "Data invalid </br>";

        } else {
            //echo 'Data ok';
        }
                ?>
<!--                <a href="signinpage.php#signup" id="register">Register Now</a>-->
            </form>
        </div>
            <div id="footer">
            <div id="quick-links">
                <table id="quick-links-table">
                  <tr>
                    <th><a href="cab230.php">Home</a></th>
                    <th><a href="loginpage.php">Sign in</a></th>
                    <th><a href="signinpage.php#signup">Sign up</a></th>
                    <th><a href=" ">About Us</a></th>
                  </tr>
                </table>
            </div>
        </div>
    </body>


</html>
