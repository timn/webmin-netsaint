#!/usr/bin/perl

#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999/2000 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
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

#    Created 22.12.1999


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';
$access{'misc'} || &error($text{'misc_notallowed'});

$whatfailed=$text{'misc_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});

$tmp=&find_name('use_agressive_host_checking', \@conf);
if ($tmp->{'values'}->[0]) { $aggr=" CHECKED" }
                      else { $naggr=" CHECKED" }

$tmp=&find_name('sleep_time', \@conf);
$sleeptime_value=$tmp->{'values'}->[0];

$tmp=&find_name('interval_length', \@conf);
$intervallength_value=$tmp->{'values'}->[0];


&header($text{'misc_title'}, "", "misc", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

print <<EOM;
<HR>
<FORM NAME="misc" ACTION="save_misc.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'misc_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_sleep_time'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="sleeptime" VALUE="$sleeptime_value" SIZE=5> $text{'seconds'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_interval_length'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="intervallength" VALUE="$intervallength_value" SIZE=5> $text{'seconds'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_aggressive'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="aggressivechecks" VALUE=1 SIZE=35$aggr> $text{'yes'}
      <INPUT TYPE=radio NAME="aggressivechecks" VALUE=0 SIZE=35$naggr> $text{'no'}
     </TD>
    </TR>
   </TABLE>
  </TD>
 </TR>
</TABLE>

<BR>
<INPUT TYPE=submit VALUE="$text{'save'}">
</FORM>

EOM

print "<HR>\n";
&footer("", $text{'misc_return'});


### END of index.cgi ###.
