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

#    Created 06.04.2000

$whatfailed=$text{'extcommopt_error'};
require './netsaint-lib.pl';
$access{'extcommedit'} || &error($text{'extcommopt_notallowed'});


@conf=&parse_config($config{'main_config'});

$tmp=&find_name('check_external_commands', \@conf);
if ($tmp->{'values'}->[0] eq "1") { $check=" CHECKED" }
                             else { $ncheck=" CHECKED" }

$tmp=&find_name('command_check_interval', \@conf);
$interval_value=$tmp->{'values'}->[0];



&header($text{'extcommopt_title'}, "", "", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

print <<EOM;
<HR>
<FORM ACTION="save_extcommandoptions.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'extcommopt_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'extcommopt_check'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="check" VALUE=1 SIZE=35$check> $text{'yes'}
      <INPUT TYPE=radio NAME="check" VALUE=0 SIZE=35$ncheck> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_interval_length'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="interval" VALUE="$interval_value" SIZE=5> $text{'timeunits'}
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
&footer("list_extcommands.cgi", $text{'extcommopt_return'});


### END of edit_extcommandoptions.cgi ###.
