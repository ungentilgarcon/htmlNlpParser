#! /bin/perl

$Args = $ARGV[0];
my $progr= "httrack ";
my $urlHttrack = $Args;#'http://aadn.org';
my  $urlHttrackFolder = $urlHttrack;
my $find_1 = "/";
my $find_2 = ":";
my $replace = "_";
 $find_1 = quotemeta $find_1; # escape regex metachars if present
 $find_2 = quotemeta $find_2; # escape regex metachars if present
 $urlHttrackFolder =~ s/$find_1/$replace/g;
 $urlHttrackFolder =~ s/$find_2/$replace/g;


# httrack 'http://'+urlHttrack -O '/tmp/'+urlHttrack -Y -r30 -%P0 -t -XO -o0  -s0  -F 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15' -%l '*' -q -z -I0 -B -e -#L10000



my $params1 = "\'\\ http://";
my $params2 = "' -O '/tmp/";
my $params3  = " -Y -r30  -%P0 -t -X0 -o0  -s0 -F 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15' -%l '*' -q -z -I0 -B -e -#L10000 ";
my $other = "Other";

my $string =  $progr."'".$urlHttrack.$params2.$urlHttrackFolder."'".$params3;
 print ($string, "\n");
    @args = ( $string );
print @args;


     system @args ;
