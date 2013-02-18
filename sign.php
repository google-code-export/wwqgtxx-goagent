<?php
/* Set Current Directory */
preg_match('/(.*?)\\\sign\.php$/',__FILE__,$currentdir); 
chdir($currentdir[1]);

/* Sign */
if($data=md5(file_get_contents("wwqgtxx-goagent/hash.dat"))){
	echo " Signing...";

	$privkey=file_get_contents("wwqgtxx-goagent.prikey");
	$privkey = openssl_get_privatekey($privkey,"123456");
	if(openssl_sign($data, $signature, $privkey,OPENSSL_ALGO_MD5)){
		echo "OK!\r\n";
	}else{
		echo "Fail!\r\n";
	}
	
	echo " Verifying...";
	
	$pubkey=file_get_contents("wwqgtxx-goagent/data/wwqgtxx-goagent.pubkey");
	if($pubkey=openssl_get_publickey($pubkey)){
		if(openssl_verify($data,$signature,$pubkey,OPENSSL_ALGO_MD5)){
			echo "OK!\r\n";
		}else{
			echo "Fail!\r\n";
		}
	}else{
		echo "\r\n [!]Cannot load wwqgtxx-goagent.pubkey!\r\n";
	}
	
	openssl_free_key($pubkey); openssl_free_key($privkey);
	file_put_contents("wwqgtxx-goagent/sign.dat",base64_encode($signature));
}else{
	echo "FAIL to read hash.dat";
}
?>