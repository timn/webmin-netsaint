#!/usr/bin/perl

#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999-2000 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
#    Written by Tim Niemueller <tim@niemueller.de> - http://www.niemueller.de

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    This module inherited from the Webmin Module Template 0.75.1 by tn

#    Created 28.12.1999


$whatfailed=$text{'timeperiod_error'};
require './netsaint-lib.pl';

@conf=&parse_config($config{'host_config'});

@timeperiods=&find_struct('timeperiod', \@conf);

$timeperiod=0;
foreach $h (@timeperiods) {
 if ($h->{'value'} eq $in{'name'}) { $timeperiod=$h; break; }
}

if ($timeperiod) {
 $header=&text('timeperiod_header', $timeperiod->{'value'});
 $title=$text{'timeperiod_title_edit'};
} else {
 $header=$text{'timeperiod_create'};
 $title=$text{'timeperiod_title_create'};
}

&header($title, "", "timeperiod", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

$header=&text('timeperiod_header', $timeperiod->{'value'});

print <<EOM;
<HR>
<FORM ACTION="save_timeperiod.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=4>
      <B>$header</B>
     </TD>
    </TR>
EOM

if ($timeperiod) {
 print "<INPUT TYPE=hidden NAME=\"name\" VALUE=\"$in{'name'}\">";
} else {
 print "<TR><TD $cb><B>$text{'name'}</B></TD> <TD $cb COLSPAN=3><INPUT TYPE=text NAME=\"name\"></TD></TR>";
}

print <<EOM;
    <TR>
     <TD $cb WIDTH=20%>
      <B>$text{'timeperiod_alias'}</B>
     </TD>
     <TD $cb COLSPAN=3 WIDTH=80%>
      <INPUT TYPE="text" NAME="timeperiodalias" VALUE="$timeperiod->{'values'}->[0]" SIZE=45>
     </TD>
    </TR>

    <TR>
     <TD $cb VALIGN=top WIDTH=20%>
      <B>$text{'timeperiod_sunday'}</B><BR>
      $text{'timeperiod_one_per_line'}
     </TD>
     <TD $cb WIDTH=30%>
<TEXTAREA NAME="sunday" ROWS=3 COLS=15>
EOM
@sunday=split(/,/, $timeperiod->{'values'}->[1]);
foreach $p (@sunday) {
 print "$p\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
     <TD $cb VALIGN=top WIDTH=20%>
      <B>$text{'timeperiod_monday'}</B>
     </TD>
     <TD $cb WIDTH=30%>
<TEXTAREA NAME="monday" ROWS=3 COLS=15>
EOM
@monday=split(/,/, $timeperiod->{'values'}->[2]);
foreach $p (@monday) {
 print "$p\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
    </TR>

    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'timeperiod_tuesday'}</B><BR>
      $text{'timeperiod_one_per_line'}
     </TD>
     <TD $cb>
<TEXTAREA NAME="tuesday" ROWS=3 COLS=15>
EOM
@tuesday=split(/,/, $timeperiod->{'values'}->[2]);
foreach $p (@tuesday) {
 print "$p\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
     <TD $cb VALIGN=top>
      <B>$text{'timeperiod_wednesday'}</B>
     </TD>
     <TD $cb>
<TEXTAREA NAME="wednesday" ROWS=3 COLS=15>
EOM
@wednesday=split(/,/, $timeperiod->{'values'}->[3]);
foreach $p (@wednesday) {
 print "$p\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
    </TR>
    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'timeperiod_thursday'}</B><BR>
      $text{'timeperiod_one_per_line'}
     </TD>
     <TD $cb>
<TEXTAREA NAME="thursday" ROWS=3 COLS=15>
EOM
@thursday=split(/,/, $timeperiod->{'values'}->[4]);
foreach $p (@thursday) {
 print "$p\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
     <TD $cb VALIGN=top>
      <B>$text{'timeperiod_friday'}</B>
     </TD>
     <TD $cb>
<TEXTAREA NAME="friday" ROWS=3 COLS=15>
EOM
@friday=split(/,/, $timeperiod->{'values'}->[5]);
foreach $p (@friday) {
 print "$p\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
    </TR>
    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'timeperiod_saturday'}</B><BR>
      $text{'timeperiod_one_per_line'}
     </TD>
     <TD $cb>
<TEXTAREA NAME="saturday" ROWS=3 COLS=15>
EOM
@saturday=split(/,/, $timeperiod->{'values'}->[6]);
foreach $p (@saturday) {
 print "$p\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
     <TD COLSPAN=2>
      $text{'timeperiod_desc'}
     </TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>

EOM

if ($timeperiod) {
 print "<INPUT TYPE=submit VALUE=\"$text{'save'}\">\n";
 print "<INPUT NAME=\"delete\" TYPE=submit VALUE=\"$text{'timeperiod_delete'}\">";
} else {
 print "<INPUT TYPE=submit NAME=\"new\" VALUE=\"$text{'timeperiod_create'}\">";
}


print "</FORM><HR>\n";
&footer("list_timeperiods.cgi", $text{'timeperiod_return'});


### END of edit_timeperiod.cgi ###.
