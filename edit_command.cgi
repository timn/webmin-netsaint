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


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'command_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@commands=&find_struct('command', \@conf);

$command=0;
foreach $c (@commands) {
 if ($c->{'value'} eq $in{'name'}) { $command=$c; break; }
}

if ($command) {
 $header=&text('command_header', $command->{'value'});
 $title=$text{'command_title_edit'};
} else {
 $header=$text{'command_create'};
 $title=$text{'command_title_create'};
}

&header($title, "", "command", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");


print <<EOM;
<HR>
<FORM ACTION="save_command.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=5>
      <B>$header</B>
     </TD>
    </TR>
EOM

if ($command) {
 print "<INPUT TYPE=hidden NAME=\"name\" VALUE=\"$in{'name'}\">";
} else {
 print "<TR><TD $cb><B>$text{'name'}</B></TD> <TD $cb><INPUT TYPE=text NAME=\"name\"></TD></TR>";
}

print <<EOM;
    <TR>
     <TD $cb>
      <B>$text{'command_command'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="command" VALUE="$command->{'values'}->[0]" SIZE=50>
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
&footer("list_commands.cgi", $text{'command_return'});


### END of edit_command.cgi ###.
