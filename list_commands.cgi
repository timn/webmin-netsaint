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

$whatfailed=$text{'commands_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});
@commands=&find_struct('command', \@conf);


&header($text{'commands_title'}, "", "commands", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

if ($config{'sort_commands'}) {
 @commands = sort { $a->{'value'} cmp $b->{'value'} } @commands;
}

$colspan=$config{'list_commands_detailed'} ? "2" : "4";
print <<EOM;
<HR>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=$colspan>
      <B>$text{'commands_header'}</B>
     </TD>
    </TR>
EOM

if ($config{'list_commands_detailed'}) {
print <<EOM;
    <TR>
     <TD $cb><B>Name</B></TD>
     <TD $cb><B>Command</B></TD>
    </TR>
    <TR>
     <TD COLSPAN=2 $cb><HR></TD>
    </TR>
EOM
  for($i=0; $i<@commands; $i++) {
   print "<TR>\n";

   print "<td><A HREF=\"edit_command.cgi?",
         "name=$commands[$i]->{'value'}\">",
         "$commands[$i]->{'value'}</A></TD>\n";
   print "<TD>$commands[$i]->{'values'}->[0]</TD>\n";

   print "</TR>\n";
  }

} else {

  for($i=0; $i<@commands; $i++) {
   if ($i%4 == 0) { print "<TR>\n"; }

   print "<td><A HREF=\"edit_command.cgi?",
         "name=$commands[$i]->{'value'}\">",
         "$commands[$i]->{'value'}</A></TD>\n";

   if ($i%4 == 3) { print "</TR>\n"; }
  }

  if ((scalar(@commands)-1)%4 != 3) { print "</TR>\n"; }
}

if (! @commands) { print "<TR><TD><B>No commands found!</B></TD></TR>\n" }

print <<EOM;
   </TABLE>
  </TD>
 </TR>
</TABLE>
<BR>
<A HREF="edit_command.cgi">$text{'commands_new'}</A>

EOM


print "<BR><HR>\n";
&footer("", $text{'commands_return'});


### END of index.cgi ###.
