#!/usr/bin/perl


#Reading the input1-pattern and input2-directory path for program
if ( $#ARGV == 0  ) {


	$dir_path=$ARGV[0] ;

} 

else  {

# valdiating the console arguments
	print "usage:=> perl $0 <DATAB>\n";
                 exit;
	}


#calling the filesearch based on PART1 assignmnet logic

file_sort($dir_path);

########displaying files under dir_path###################

system("ls -l $dir_path/* ");


sub file_sort{

    ($dir_path)=@_ ;
    $pattern="proj" ;	
      	
    chomp($dir_path) ;    
    @files = glob($dir_path."/*" );

    for $FILE (@files) {
		$FILE =~s/$dir_path\///;
		#print $FILE."\n"; #checking the proj string in each file based on creating directory and sorting it
                 if ( $FILE =~m/^proj(.*)\./ and $FILE !~m/^misc/ ) {
			$new_dir= "$dir_path/"."assignment"."$1/";
			
			unless(-d $new_dir) {
				mkdir($new_dir) or "Couldn't create $dir directory, $!";	
			}
			system("mv $dir_path/$FILE $new_dir/");	
		  }

		#file name not matching the proj string in each file based on creating directory "misc" and sorting it
		 elsif  ( $FILE !~m/^proj/ and $FILE !~m/^misc/ ) {
			$new_dir= "$dir_path/"."misc";
			unless(-d $new_dir) {
				mkdir( "$new_dir" ) or "Couldn't create $dir directory, $!";
			}
			#moving the misc file
			system("mv $dir_path/$FILE $new_dir/");
                        #print " $FILE and $new_dir \n";
		}

    }
 }
