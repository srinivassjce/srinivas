#!/usr/bin/perl


#Reading the input1-pattern and input2-directory path for program
if ( $#ARGV == 1  ) {

	$pattern_file=$ARGV[0];

	$dir_path=$ARGV[1] ;

} elsif ($#ARGV == 2) {

#reading option -i and validating it
	if ($ARGV[0] =~/-i/i ) {
		$option_i = 1 ;
		$pattern_file=$ARGV[1];
		$dir_path=$ARGV[2] ;
	}
	else {

		 print "usage : perl $0 ‐i perlRegexpPattern listOfFiles\n\nperl $0 RegexpPattern listOfFiles\n\n";
		 exit;
		}
}else  {

# valdiating the console arguments
	print "usage : perl $0 ‐i perlRegexpPattern listOfFiles\n\nperl $0 RegexpPattern listOfFiles\n\n";
                 exit;
	}


#calling the filesearch based on PART1 assignmnet logic

file_search($dir_path,$pattern_file);



sub file_search{

    ($dir_path,$pattern)=@_ ;
     $dir_path1=$dir_path;
     	
    chomp($dir_path) ;

#taking care logic for option -i
#find.pl ‐i perlRegexpPattern listOfFile
#If the ‐i option is passed, the script should return the opposite files (i.e., those which do not match the expression in file 
#name or contents).  The script should be invoked with the following format:   
    
    if ($option_i ) {

    	@files = glob($dir_path );
         $dir_path=~s/\/\*//;
         for $FILE (@files) {
                if ($FILE !~ m/$pattern/ ) {
                 $FILE=~s/$dir_path\///;
                 print $FILE."\n";
                }
		else {
                        open(DATA,"<$FILE") or die "Can't open data"; # opening the file which  match pattern
                        @lines = <DATA>;
                        for my $i ( @lines) {
                                if ($i !~ m/$pattern/) {  #displaying file and line which doenot  matching the file contents 
                                        $FILE=~s/$dir_path\///;
                                        print "$FILE".":"."$i";
                                }
                        }
			close(DATA);
			}

         }






	}


#If the file name matches, print that file name , If the file name doesn't match,
#it should look for instances of the regular expression within the text of the file.  If 
#found, it should print the filename, a colon, and the text for the first line that contained that pattern.     
    else {
	 		
	 @files = glob($dir_path );
	 $dir_path=~s/\/\*//;
	 for  $FILE (@files) { 
		if ($FILE=~m/$pattern/ ) {
		 $FILE=~s/$dir_path\///;
		 print $FILE."\n";	
		} 
		else {

			open(DATA,"<$FILE") or die "Can't open data"; # opening the file which donot match pattern
			@lines = <DATA>;
			for my $i ( @lines) {
				if ($i =~m/$pattern/) { ##displaying file and line which does matching the file contents 
				        $FILE=~s/$dir_path\///; 			
					print "$FILE".":"."$i";
				}
			}
			close(DATA);


		}
		
	 }
	


	
	 
    }
}

