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

#    Created 26.12.1999

$whatfailed=$text{'extcommand_error'};
require './netsaint-lib.pl';
require './extcommands-lib.pl';


@commands = &parse_extcommands();

$command=0;
foreach $c (@commands) {
 if ($c->{'line'} eq $in{'line'}) { $command=$c; last; }
}

if ($command) {
 $header=&text('extcommand_header', $command->{'comm'});
 $title=$text{'extcommand_title_edit'};
} else {
 $header=$text{'extcommand_create'};
 $title=$text{'extcommand_title_create'};
}

$commselect = &commselect($command->{'comm'});

&header($title, "", "extcommand", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");


print <<EOM;
<HR>
<FORM ACTION="save_extcommand.cgi" METHOD=POST>
<INPUT TYPE=hidden NAME="line" VALUE="$command->{'line'}">

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=5>
      <B>$header</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'extcommand_command'}</B>
     </TD>
     <TD $cb>
      $commselect
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'extcommand_arguments'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="arguments" VALUE="$command->{'args'}" SIZE=25>
     </TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>

EOM

if ($command) {
 print "<INPUT TYPE=submit VALUE=\"$text{'save'}\">\n";
 print "<INPUT NAME=\"delete\" TYPE=submit VALUE=\"$text{'command_delete'}\">";
} else {
 print "<INPUT TYPE=submit NAME=\"new\" VALUE=\"$text{'command_create'}\">";
}


print "</FORM><HR>\n";
&footer("list_extcommands.cgi", $text{'command_return'});


### END of edit_command.cgi ###.
