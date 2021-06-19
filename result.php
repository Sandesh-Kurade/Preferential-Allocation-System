
<!DOCTYPE html>

<html>

<head>
	<meta charset=UTF-8" />
	
	<title>pref</title>
	
	<link rel="stylesheet" type="text/css" href="style.css" />
</head>

<body>

	<div id="page-wrap">

		<h1>Form Status</h1>
		
        <?php
            
            $answer1 = $_POST['question-1-answers'];
            $answer2 = $_POST['question-2-answers'];
            $answer3 = $_POST['question-3-answers'];
            $answer4 = $_POST['question-4-answers'];
             $name = $_POST['n'];
           
         
        $fh = fopen("record.csv", "a");
 $no_rows = count(file("record.csv"));
           
 if($no_rows > 1)
            {
               $no_rows = ($no_rows - 1) + 1;
            } 

        
        $headers = array('Sr no.' => $no_rows ,'Name' => $name ,'First Preference '=> $answer1, 'Second Preference ' => $answer2,
                   'Third Preference ' => $answer3, 'Fourth Preference ' => $answer4);
         
           fputcsv($fh , $headers);


             
		$output = shell_exec("python projectsource.py records2.csv");
		echo "submitted successfully"
       
                       
	
            
        ?>

   
	
	</div>

</body>

