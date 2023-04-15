<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>PHP Basic</h1>
    <?php
    $name = "Meyer";
    $num = 2 /* A comment */+ 3;
    echo "Hello $name<br>";

    print "Hey, this is print. att: $name" . $num . "<br><br>";

    echo "<b>array(1, 2, 3, array('a', 5, TRUE))</b><br>";
    $arr = array(1, 2, 3, array("a", 5, TRUE));
    print_r($arr);
    echo "<br>";
    var_dump($arr);
    ?>

    <h2>Funciones</h2>
    <?php
    function get_name()
    {
        global $name;
        $GLOBALS['num'] = $GLOBALS['num'] + 2;
        echo $name . $GLOBALS['num'];
    }

    get_name();

    echo "<h3>Static</h3>";

    function get_some()
    {
        static $st = 1;
        echo "<li>" . $st . "<br>";
        $st++;
    }

    get_some();
    get_some();

    ?>

</body>

</html>