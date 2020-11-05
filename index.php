<form action="get">
  Mot: <input type="text"  name="mot" value=<?php echo "\"".$_GET["mot"]."\"" ?> required><br><br>
  Profondeur min: <input type="number" name="profondeur" min="2" value=<?php echo "\"".$_GET["profondeur"]."\"" ?> required><br><br>
  Imprécision: <input type="number" name="imprecision" value=<?php echo "\"".$_GET["imprecision"]."\"" ?> required><br><br>

  <input type="submit" value="Submit">
</form> 

<br>

<?php
 
 $mot = explode(" ",$_GET["mot"]);
 $profondeur = $_GET["profondeur"];
 $imprecision = $_GET["imprecision"];

 $dico = file("dico");

/*
 foreach($mot as $m){
 	echo $m."<br>";
 }
 */

for($i=0;$i<count($mot);$i++){
	$bool[$i] = FALSE;
}

$i=0;
foreach($mot as $m){
	$tabPhone[$i] = "";
	$i++;
}


 foreach ($dico as $line) {
 	$line = explode("\t",$line);
 	for($i=0;$i<count($mot);$i++){
 		if($line[0] == $mot[$i]){
 			$tabPhone[$i] = $line[1];
 			$bool[$i] = TRUE;
 		}
 	}
 }

 $find = TRUE;

for($i=0;$i<count($mot);$i++){
	if($bool[$i] == FALSE){
		echo "Mot [".$mot[$i]."] non trouvé :'(";
		$find = FALSE;
	}
}



if($find == TRUE){

	$phone = "";
	foreach($tabPhone as $p){
		$phone = $phone.$p;
	}
	$phone = str_replace("\n", "", $phone);

	

	foreach($dico as $line){
		$line = explode("\t",$line);
		$line[1] = str_replace("\n", "", $line[1]);
 		if(strlen($phone)>strlen($line[1])){
 			$taille = strlen($line[1]);
 		}
 		else $taille = strlen($phone);
 		$ok = FALSE;
		for(;$taille >= $profondeur and $ok==FALSE;$taille--){
			if(substr($phone, -$taille) == substr($line[1], -$taille)){
				echo $line[0]."<br>";
				$ok = TRUE;
 			}
 		}		
	}
} 



 ?>