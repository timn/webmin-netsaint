#!/usr/bin/perl

#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
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


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'timeperiods_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@timeperiods=&find_struct('timeperiod', \@conf);


&header($text{'timeperiods_title'}, "", "timeperiods", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

# foreach $l (@timeperiods) {
#  print "\n<BR>$l->{'name'}::$l->{'value'}::$l->{'line'}";
# }

if ($config{'sort_timeperiods'}) {
 @timeperiods = sort { $a->{'value'} cmp $b->{'value'} } @timeperiods;
}
# Just show names

print <<EOM;
<HR>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'timeperiods_timeperiods'}</B>
     </TD>
    </TR>
    <TR>
     <TD>
      <TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 WIDTH=100%>
EOM

for($i=0; $i<@timeperiods; $i++) {
 if ($i%4 == 0) { print "<TR>\n"; }

 print "<td><A HREF=\"edit_timeperiod.cgi?",
	"name=$timeperiods[$i]->{'value'}\">",
	"$timeperiods[$i]->{'value'}</A></TD>\n";

 if ($i%4 == 3) { print "</TR>\n"; }
}

if ((scalar(@timeperiods)-1)%4 != 3) { print "</TR>\n"; }
if (! @timeperiods) { print "<TR><TD><B>No timeperiods found!</B></TD></TR>\n" }

print <<EOM;
      </TABLE>
     </TD>
    </TR>
   </TABLE>
  </TD>
 </TR>
</TABLE>
<A HREF="edit_timeperiod.cgi">$text{'timeperiods_new'}</A>

EOM


print "<HR>\n";
&footer("", $text{'timeperiods_return'});


### END of list_timeperiods.cgi ###.