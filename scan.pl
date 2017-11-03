use 5.010;
use Socket;
use URI;
use Net::Ping;  
use LWP::UserAgent;
use HTTP::Request::Common;
use Term::ANSIColor;
use Win32::Console::ANSI;
use HTTP::Request::Common qw(GET);
$ag = LWP::UserAgent->new();
$ag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$ag->timeout(10);


#declaring the default proxy and Ip.txt
use Getopt::Long; 
my $proxy = "proxy.txt";
my $ip = 'IP.txt';
my $dorks = 'dorks.txt';
GetOptions (  "proxy=s" => \$proxy ,   # string
              "ip=s"   => \$ip ,      # string
              "dorks=s"  => \$dorks , )   # string 
or die("Error in command line arguments\n");



#print clearing the console output using system comamnd
if ($^O =~ /MSWin32/) 
{
	system("cls");
}
else { 
	system("clear"); 
}


print colored("[ BING DORKER  V1.0]",'white on_blue'),"\n";
$banner = (
'coded by Author'
  );
  
print color("white"), ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n";
print color("white"), ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n";
print color("green"), "[1]Bing Dorker |> it will load default proxy.txt on based on user choice-YES/NO
		User wants to load  his own proxy file --> use the command line option --proxy  e.g perl scan.pl --proxy <proxy_listfile>\n\n";
print color("green"), "[2]Bing Dorker |> Scan websites from IP's inside IP.txt file
		User wants to load  his own IP.txt file --> use the command line option --ip  e.g perl scan.pl --ip <ip_listfile>\n\n";
print color("green"), "[3]Extract websites using dork file
		User wants to load  his own dork.txt file -- use the command line option --dorks  e.g perl scan.pl --dorks <dorks-listfile>\n\n";
print color("green"), "[4]Extract websites usuing dork file \"dorks.txt\"  plus ip_list file \"ip.txt\" 
		User wants to load  his own dork.txt and ip file --> use the command line option -dorks and -ip  e.g perl scan.pl -dorks  <dorks-listfile> -ip <ip_listfile>\n\n";
print color("white"), ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n";
print color("white"), ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n";
print "[+] Choose Number :";
my $targett = <STDIN>;
chomp $targett;



if($targett eq '1'){
print color("white"),"Do you want use proxy.txt\n";
print color("green"),"Enter Yes to laod \" $proxy \" file and  No to choose  Number \"2\" : ";

$input=<STDIN>;
chomp($input);

if ($input =~m/^yes$/i ){
	print color("green"),"Loading each proxy \n";
	open ($THETARGET,"<$proxy") || die "[-] Can't open the proxy file!";
	@TARGETS = <$THETARGET>;
	close $THETARGET;
	OUTER: foreach my $target(@TARGETS){
		chomp($target);
		#print "$target\n";
	 $ag->proxy([ 
        [ 'http', 'https' ] => "http://$target/",
    ]);
	
	}
	
	print color("green"),"proxies are loading and moving to second option[2] \n";
	$targett=2
	}else {
		print "chosing the second[2] option\n";
		$targett=2	
	}

}

if($targett eq '2')
{
print "Extracting the website based on Ip list file \"$ip\" \n";
chomp($ip);
$ip=~s/'//i;
$ip=~s/"//i;
open (my $THETARGET, "$ip") || die "[-] Can't open the file!";
@TARGETS = <$THETARGET>;
close $THETARGET;
#$link=$#TARGETS + 1;
OUTER: foreach $target(@TARGETS){
		chomp($target);
		get($target);
}
}


if($targett eq '3')
{
print "Extracting the website using dorks file\"$dorks\"";
chomp($dorks);
$dorks=~s/"//i;
$dorks=~s/'//i;
open (THETARGET, "<$dorks") || die "[-] Can't open the file!";
@TARGETS = <THETARGET>;
close THETARGET;
#$link=$#TARGETS + 1;
#print "@TARGETS";
OUTER: foreach $target(@TARGETS){
	chomp($target);
	if($target =~m/index\.php\?option\=.*/) {
		
		gassonee($target);
	}

}


}
if($targett eq '4'){
	print "Extracting the websites based on ip address plus dorks  \n";
	print "reading dorks file \"$dorks\" and ip file \"$ip\" \n";
	open (THETARGET, "<$dorks") || die "[-] Can't open the file!";
	@TARGETS_dork = <THETARGET>;
	close THETARGET;	
	
	open (THETARGET, "<$ip") || die "[-] Can't open the file!";
	@TARGETS_ip = <THETARGET>;
	close THETARGET;
	
	OUTER:foreach $target_ip(@TARGETS_ip ){
	chomp($target_ip);
	for $target_dork (@TARGETS_dork) {
		chomp($target_dork);
		if($target_dork =~m/index\.php\?option\=.*/) {
			
			gassonee_ip_dork($target_ip,$target_dork);
		}

	}
	}
}


##############################
sub gett(){
	$target=@_;
	$ip= (gethostbyname($target))[4];
	my ($a,$b,$c,$d) = unpack('C4',$ip);
	for ($i = 1; $i <= 255; $i+=1){
	$ips ="$a.$b.$c.$i";
	OUTER: foreach $ip($ips){
	print color("red"), " [IP] > [$ips]\n";
	print color ('reset');
	open (TEXT, '>>ipsss.txt');
	print TEXT "$ips\n";
	close (TEXT);
	$dork="ip:$ips";
	gassone();
}
}
}
#############################
sub get(){
	@target=@_;
	$ip= (gethostbyname($target))[4];
	#print "iam here ",(gethostbyname($tofuck))[4] ;

	my ($a,$b,$c,$d) = unpack('C4',$ip);
	$ips="$a.$b.$c.$d";
	print " [IP] > [$ips]\n";
	open (TEXT, '>>ipsss.txt');
	print TEXT "$ips\n";
	close (TEXT);
	$dork="ip:$ips";
	gassone();
}
####################################"
sub gassone(){

	for ($ii = 1; $ii <= 2000; $ii+=10){

		$url = "http://www.bing.com/search?q=$dork&filt=all&first=$ii&FORM=PERE";
		if ( ping($url) == 1 ) {
			print "\$url is $url\n";
		}
		$resp = $ag->request(HTTP::Request->new(GET => $url));
		#print "\$resp is $resp\n";
		$rrs = $resp->content;
        #print "\$rrs is $rrs\n";
		

		while($rrs =~ m/<a href=\"?http:\/\/(.*?)\//g){

			$link = $1;
			if ( $link !~ /overture|msn|live|bing|yahoo|duckduckgo|google|yahoo|microsof/)
			{
						if ($link !~ /^http:/)
					 {
						$link = 'http://' . "$link" . '/';
					 }



			if($link !~ /\"|\?|\=|index\.php/){
				if  (!  grep (/$link/,@result)){
					print "$link\n";
					open(save, '>>SS1.txt');
					print save "$link\n";
					close(save);
					push(@result,$link);
				}
			} 
		}
		
		#print "iteration : ".($i);
		#$i++;
		}
	####
	if ($rrs !~ m/class=\"sb_pagN\"/g){
	next OUTER;
	}
	}
	}
	###########
sub gassonee(){
	$dork=@_;
	for ($ii = 1; $ii <= 2000; $ii+=10){

	$url = "http://www.bing.com/search?q=$dork&filt=all&first=$ii&FORM=PERE";
	$resp = $ag->request(HTTP::Request->new(GET => $url));
	$rrs = $resp->content;
	#print "\$rrs is $rrs\n";
		
		
	#open(my $handle, ">out.txt")    || die "can't open $path: $!";
	#binmode($handle);               # for raw; else set the encoding

	#print $handle "$rrs\n";
		
	#close($handle);
	
	while($rrs =~ m/<a href=\"?http:\/\/(.*?)\//g){



	$link = $1;
	#print "HERE is $link\n";
		
		if ( $link !~ /overture|msn|live|bing|yahoo|duckduckgo|google|yahoo|microsof/)
		{
					if ($link !~ /^http:/)
				 {
					$link = "http://"."$link" ."/";
				 }



		if($link !~ /\"|\?|\=|index\.php/){
			if  (!  grep (/$link/,@result)){
				#print "Here just before ping is $link\n";
			
				if ( ping($link) == 1 ) {

				print "$link\n";

			}
		open(save, '>>SS.txt');
		print save "$link\n";
		close(save);
		push(@result,$link);
						}
	} 
	}
	}
	####
	if ($rrs !~ m/class=\"sb_pagN\"/g){
	exit;
	}
	}
}

sub gassone(){

	for ($ii = 1; $ii <= 2000; $ii+=10){

		$url = "http://www.bing.com/search?q=$dork&filt=all&first=$ii&FORM=PERE";
		if ( ping($url) == 1 ) {
			print "\$url is $url\n";
		}
		$resp = $ag->request(HTTP::Request->new(GET => $url));
		#print "\$resp is $resp\n";
		$rrs = $resp->content;
        #print "\$rrs is $rrs\n";
		

		while($rrs =~ m/<a href=\"?http:\/\/(.*?)\//g){

			$link = $1;
			if ( $link !~ /overture|msn|live|bing|yahoo|duckduckgo|google|yahoo|microsof/)
			{
						if ($link !~ /^http:/)
					 {
						$link = 'http://' . "$link" . '/';
					 }



			if($link !~ /\"|\?|\=|index\.php/){
				if  (!  grep (/$link/,@result)){
					print "$link\n";
					open(save, '>>SS1.txt');
					print save "$link\n";
					close(save);
					push(@result,$link);
				}
			} 
		}
		
		#print "iteration : ".($i);
		#$i++;
		}
	####
	if ($rrs !~ m/class=\"sb_pagN\"/g){
	next OUTER;
	}
	}
	}
	###########
sub gassonee_ip_dork(){
	my ($ips,$dorks)=@_;
	$dork="ip:$ips"."+"."$dorks";
	
	print color("green"),"\nsearch in bingo for ip + dork".$dork."\n" ;
	for ($ii = 1; $ii <= 2000; $ii+=10){

	$url = "http://www.bing.com/search?q=$dork&filt=all&first=$ii&FORM=PERE";
	$resp = $ag->request(HTTP::Request->new(GET => $url));
	$rrs = $resp->content;
	
	
	while($rrs =~ m/<a href=\"?http:\/\/(.*?)\//g){


	$link = $1;
	#print "HERE is $link\n";
		
		if ( $link !~ /overture|msn|live|bing|yahoo|duckduckgo|google|yahoo|microsof/)
		{
					if ($link !~ /^http:/)
				 {
					$link = "http://"."$link" ."/";
				 }



		if($link !~ /\"|\?|\=|index\.php/){
			if  (!  grep (/$link/,@result)){
				#print "Here just before ping is $link\n";
			
				if ( ping($link) == 1 ) {

				print "$link\n";

			}
		open(save, '>>SS.txt');
		print save "$link\n";
		close(save);
		push(@result,$link);
						}
	} 
	}
	}
	####
	if ($rrs !~ m/class=\"sb_pagN\"/g){
	exit;
	}
	}
}


sub ping{
my ($site)=@_;
use Net::Ping;
my $p = Net::Ping->new();
#print "site is $site\n";
my $uri = URI->new($site);
my $ip_addr = gethostbyname( $uri->host );
eval ($ip_addr = inet_ntoa( $ip_addr ));
#print "$ip_addr"."\n";

if (eval {$p->ping($ip_addr)}) {
   #	say 'alive';
   		open(save, '>>pinged_ips.txt');
		print save "$ip\n";
		close(save);
		push(@result,$link);
	return 1
}
return 0


}
