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

#    Created 21.12.1999


require './netsaint-lib.pl';
$access{'files'} || &error($text{'efiles_notallowed'});

$whatfailed=$text{'efiles_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});

$logselector=&file_chooser_button('log', 0, 0);
$hostcfgselector=&file_chooser_button('hostcfg', 0, 0);
$statusselector=&file_chooser_button('status', 0, 0);
$tempselector=&file_chooser_button('temp', 0, 0);
$commselector=&file_chooser_button('comm', 0, 0);

$tmp=&find_name('log_file', \@conf);
$logvalue=$tmp->{'values'}->[0];

$tmp=&find_name('cfg_file', \@conf);
$hostcfgvalue=$tmp->{'values'}->[0];

$tmp=&find_name('status_file', \@conf);
$statusvalue=$tmp->{'values'}->[0];

$tmp=&find_name('temp_file', \@conf);
$tempvalue=$tmp->{'values'}->[0];

$tmp=&find_name('command_file', \@conf);
$commvalue=$tmp->{'values'}->[0];


&header($text{'efiles_title'}, "", "files", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

# foreach $l (@conf) {
#  print "\n<BR>$l->{'name'}::$l->{'values'}->[0]::$l->{'line'}";
# }

print <<EOM;
<HR>
<FORM NAME="files" ACTION="save_files.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'efiles_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'efiles_log'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="log" VALUE="$logvalue" SIZE=35> $logselector
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'efiles_hostcfg'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="hostcfg" VALUE="$hostcfgvalue" SIZE=35> $hostcfgselector
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'efiles_status'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="status" VALUE="$statusvalue" SIZE=35> $statusselector
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'efiles_temp'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="temp" VALUE="$tempvalue" SIZE=35> $tempselector
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'efiles_comm'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="comm" VALUE="$commvalue" SIZE=35> $commselector
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
&footer("", $text{'efiles_return'});


### END of index.cgi ###.
