#!/usr/bin/perl 


# Reading the command line args
if ( @ARGV < 1 ) {
    print "Please enter: proj5.pl <mm/dd/yyyy>\n";
    exit;
}


my $date = $ARGV[0];


open (my $file, '<', './p5Customer.txt') or die"Could not open file";

my $dir = "Emails";
mkdir $dir unless -e $dir;

while (<$file>) {

    chomp;
    my ($email, $fname, $title, $paid, $owe) = split /,/;
    
    next if $owe < $paid;

    open (my $temp, '<', 'template.txt') or die "Could not open template.txt";
    #reading the EMAIL dirtory path	
    my $path = "$dir/$email";
    open (my $outfile, '>', $path) or die "Unable to create file path";
    #opening the template.txt for reading and replacing the EMAIL,FULLNAME,TITLE,AMOUNT,DATE
    # and then writing into specific email address files
    while ( <$temp> ) {

        s/EMAIL/$email/g;
        s/FULLNAME|NAME/$fname/g;
        s/TITLE/$title/g;
        s/AMOUNT/$owe/g;
        s/DATE/$date/g;

        print $outfile $_;
    }

    close($outfile);

}
