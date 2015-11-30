from subprocess import call

urlHttrack = 'http://aadn.org'
urlHttrackFolder = urlHttrack.replace('/','_').replace(':','_')

#httrack 'http://'+urlHttrack -O '/tmp/'+urlHttrack -Y -r30 -%P0 -t -XO -o0  -s0  -F 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15' -%l '*' -q -z -I0 -B -e -#L10000 
#call(['httrack',  "\""+urlHttrack+"\"",  "-Y", "-r30","-%P0","-t","-o0 " ,"-s0"  ,"-F 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'", "-%l", "'*'", "-q", "-z", "-I0", "-B", "-e" ,"-#L10000 "  ])
#call(['httrack', urlHttrack, "-O \/tmp\/htttarc", "-Y", "-r30" ,"-%P0" ,"-t" ,"-XO" ,"-o0 " ,"-s0"  ,"-F 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'", "-%l", "'*'", "-q", "-z", "-I0", "-B", "-e" ,"-#L10000 "])
call(['httrack',  "\""+urlHttrack+"\"", "-Y", "-r30" ,"-%P0" ,"-t" ,"-X0" ,"-o0 " ,"-s0", "-%l", "'*'", "-q", "-z", "-I0", "-B", "-e" ,"-#L10000 "])




# cf https://www.httrack.com/html/fcguide.html
# -O:output
# -Y   mirror ALL links located in the first level pages
# -rN set the mirror depth to N (* r9999) (--depth[=N])
# -N5: hierarchisé par type de fichier
# -Q :no log
# -q: no questions