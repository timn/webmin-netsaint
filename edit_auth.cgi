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

#    Created 09.04.2000

$whatfailed=$text{'auth_error'};
require './netsaint-lib.pl';
$access{'cgi'} || &error($text{'auth_notallowed'});

@conf=&parse_config($config{'cgi_config'});

$tmp=&find_name('use_authentication', \@conf);
if ($tmp->{'values'}->[0]) { $auth=" CHECKED" }
                      else { $nauth=" CHECKED" }

$tmp=&find_name('default_user_name', \@conf);
$defaultuser_value=$tmp->{'values'}->[0];


&header($text{'auth_title'}, "", "cgiauth", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");


foreach $a ("system_information", "system_commands", "configuration_information",
            "all_hosts", "all_host_commands", "all_services", "all_service_commands") {

  $tmp=&find_name("authorized_for_$a", \@conf);
  $tmpstr=$tmp->{'values'}->[0];
  chomp $tmpstr;

  $tmpstr =~ s/,/\n/g;

  ${"${a}_value"} = $tmpstr;

}



print <<EOM;
<HR>
<FORM ACTION="save_auth.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=4>
      <B>$text{'auth_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb COLSPAN=2>
      <B>$text{'auth_use'}</B>
     </TD>
     <TD $cb COLSPAN=2>
      <INPUT TYPE=radio NAME="useauth" VALUE=1 SIZE=35$auth> $text{'yes'}
      <INPUT TYPE=radio NAME="useauth" VALUE=0 SIZE=35$nauth> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb COLSPAN=2>
      <B>$text{'auth_default_user'}</B>
     </TD>
     <TD $cb COLSPAN=2>
      <INPUT TYPE=text NAME="defaultuser" VALUE="$defaultuser_value" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb COLSPAN=4>
      <BR><BR><B><U>$text{'auth_access'}</U></B><BR>&nbsp;
     </TD>
    </TR>
    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'auth_users_sysinfo'}</B>
     </TD>
     <TD $cb VALIGN=top>
<TEXTAREA NAME="sysinfo" ROWS=3 COLS=20>$system_information_value</TEXTAREA>
     </TD>
     <TD $cb VALIGN=top>
      <B>$text{'auth_users_syscomm'}</B>
     </TD>
     <TD $cb VALIGN=top>
<TEXTAREA NAME="syscomm" ROWS=3 COLS=20>$system_commands_value</TEXTAREA>
     </TD>
    </TR>
    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'auth_users_confinf'}</B>
     </TD>
     <TD $cb VALIGN=top>
<TEXTAREA NAME="confinf" ROWS=3 COLS=20>$configuration_information_value</TEXTAREA>
     </TD>
    </TR>
    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'auth_users_hosts'}</B>
     </TD>
     <TD $cb VALIGN=top>
<TEXTAREA NAME="hosts" ROWS=3 COLS=20>$all_hosts_value</TEXTAREA>
     </TD>
     <TD $cb VALIGN=top>
      <B>$text{'auth_users_hostcomm'}</B>
     </TD>
     <TD $cb VALIGN=top>
      <TEXTAREA NAME="hostcomm" ROWS=3 COLS=20>$all_host_commands_value</TEXTAREA>
     </TD>
    </TR>
    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'auth_users_serv'}</B>
     </TD>
     <TD $cb VALIGN=top>
<TEXTAREA NAME="serv" ROWS=3 COLS=20>$all_services_value</TEXTAREA>
     </TD>
     <TD $cb VALIGN=top>
      <B>$text{'auth_users_servcomm'}</B>
     </TD>
     <TD $cb VALIGN=top>
<TEXTAREA NAME="servcomm" ROWS=3 COLS=20>$all_service_commands_value</TEXTAREA>
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
&footer("", $text{'auth_return'});


### END of edit_auth.cgi ###.
