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

#    Created 03.04.1999


$whatfailed=$text{'extcommands_error'};
require './netsaint-lib.pl';
require './extcommands-lib.pl';

@commands = &parse_extcommands();

&header($text{'extcommands_title'}, "", "extcommands", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

if ($config{'sort_commands'}) {
 @commands = sort { $a->{'time'} cmp $b->{'time'} } @commands;
}

$colspan=$config{'list_commands_detailed'} ? "3" : "4";
print <<EOM;
<HR>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=$colspan>
      <B>$text{'extcommands_header'}</B>
     </TD>
    </TR>
EOM

if ($config{'list_commands_detailed'}) {
print <<EOM;
    <TR>
     <TD $cb><B>Time</B></TD>
     <TD $cb><B>External Command</B></TD>
     <TD $cb><B>Arguments</B></TD>
    </TR>
    <TR>
     <TD COLSPAN=$colspan $cb><HR></TD>
    </TR>
EOM
  for($i=0; $i<@commands; $i++) {
   print "<TR>\n";

   print "<TD>$commands[$i]->{'time'}</TD>\n";
   print "<td><A HREF=\"edit_extcommand.cgi?",
         "line=$commands[$i]->{'line'}\">",
         "$commands[$i]->{'comm'}</A></TD>\n";
   print "<TD>$commands[$i]->{'args'}</TD>\n";

   print "</TR>\n";
  }

} else {

  for($i=0; $i<@commands; $i++) {
   if ($i%4 == 0) { print "<TR>\n"; }

   print "<td><A HREF=\"edit_extcommand.cgi?",
         "line=$commands[$i]->{'line'}\">",
         "$commands[$i]->{'comm'}</A></TD>\n";

   if ($i%4 == 3) { print "</TR>\n"; }
  }

  if ((scalar(@commands)-1)%4 != 3) { print "</TR>\n"; }
}

if (! @commands) { print "<TR><TD><B>$text{'extcommands_err_nofound'}</B></TD></TR>\n" }

print <<EOM;
   </TABLE>
  </TD>
 </TR>
</TABLE>
<BR>
[ <A HREF="edit_extcommand.cgi">$text{'extcommands_new'}</A> ]
[ <A HREF="edit_extcommandoptions.cgi">$text{'extcommands_config'}</A> ]

EOM


print "<BR><HR>\n";
&footer("", $text{'extcommands_return'});


### END of list_extcomands.cgi ###.
