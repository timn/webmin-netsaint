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

#    Created 21.12.1999


require './netsaint-lib.pl';
$access{'logging'} || &error($text{'log_notallowed'});

$whatfailed=$text{'log_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});

$tmp=&find_name('log_level', \@conf);
if ($tmp->{'values'}->[0] == 1) { $level1=" SELECTED" }
                           else { $level2=" SELECTED" }


$tmp=&find_name('use_syslog', \@conf);
if ($tmp->{'values'}->[0]) { $usesyslog=" CHECKED" }
                      else { $nusesyslog=" CHECKED" }

$tmp=&find_name('syslog_level', \@conf);
if ($tmp->{'values'}->[0] == 1) { $slevel1=" SELECTED" }
                           else { $slevel2=" SELECTED" }

$tmp=&find_name('log_notifications', \@conf);
if ($tmp->{'values'}->[0]) { $lognot=" CHECKED" }
                      else { $nlognot=" CHECKED" }

$tmp=&find_name('log_service_retries', \@conf);
if ($tmp->{'values'}->[0]) { $serret=" CHECKED" }
                      else { $nserret=" CHECKED" }

$tmp=&find_name('log_event_handlers', \@conf);
if ($tmp->{'values'}->[0]) { $evha=" CHECKED" }
                      else { $nevha=" CHECKED" }

$tmp=&find_name('log_host_retries', \@conf);
if ($tmp->{'values'}->[0]) { $horet=" CHECKED" }
                      else { $nhoret=" CHECKED" }

$tmp=&find_name('log_rotation_method', \@conf);
if ($tmp->{'values'}->[0] eq "n") { $lrot_n=" SELECTED" }
  elsif ($tmp->{'values'}->[0] eq "h") { $lrot_h=" SELECTED" }
  elsif ($tmp->{'values'}->[0] eq "d") { $lrot_d=" SELECTED" }
  elsif ($tmp->{'values'}->[0] eq "w") { $lrot_w=" SELECTED" }
  elsif ($tmp->{'values'}->[0] eq "m") { $lrot_m=" SELECTED" }

$tmp=&find_name('log_archive_path', \@conf);
$logrotarch_value=$tmp->{'values'}->[0];
$logselector=&file_chooser_button('logrotarch', 0, 0);




&header($text{'log_title'}, "", "logging", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

print <<EOM;
<HR>
<FORM NAME="log" ACTION="save_logging.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=4>
      <B>$text{'log_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'log_level'}</B>
     </TD>
     <TD $cb>
       <SELECT NAME="loglevel">
        <OPTION VALUE="1"$level1>1
        <OPTION VALUE="2"$level2>2
       </SELECT>
     </TD>
    </TR>

    <TR>
     <TD $cb>
      <B>$text{'log_use_syslog'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="usesyslog" VALUE=1 SIZE=35$usesyslog> $text{'yes'}
      <INPUT TYPE=radio NAME="usesyslog" VALUE=0 SIZE=35$nusesyslog> $text{'no'}
     </TD>
     <TD $cb>
      <B>$text{'log_syslog_level'}</B>
     </TD>
     <TD $cb>
       <SELECT NAME="sysloglevel">
        <OPTION VALUE="1"$slevel1>1
        <OPTION VALUE="2"$slevel2>2
       </SELECT>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'log_notifications'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="notifications" VALUE=1 SIZE=35$lognot> $text{'yes'}
      <INPUT TYPE=radio NAME="notifications" VALUE=0 SIZE=35$nlognot> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'log_service_retries'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="serviceretries" VALUE=1 SIZE=35$serret> $text{'yes'}
      <INPUT TYPE=radio NAME="serviceretries" VALUE=0 SIZE=35$nserret> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'log_host_retries'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="hostretries" VALUE=1 SIZE=35$horet> $text{'yes'}
      <INPUT TYPE=radio NAME="hostretries" VALUE=0 SIZE=35$nhoret> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'log_event_handler'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="eventhandler" VALUE=1 SIZE=35$evha> $text{'yes'}
      <INPUT TYPE=radio NAME="eventhandler" VALUE=0 SIZE=35$nevha> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'log_rotate'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="logrotate">
       <OPTION VALUE="n"$lrot_n>$text{'log_rotate_n'}
       <OPTION VALUE="h"$lrot_h>$text{'log_rotate_h'}
       <OPTION VALUE="d"$lrot_d>$text{'log_rotate_d'}
       <OPTION VALUE="w"$lrot_w>$text{'log_rotate_w'}
       <OPTION VALUE="m"$lrot_m>$text{'log_rotate_m'}
      </SELECT>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'log_rotate_archive'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="logrotarch" VALUE="$logrotarch_value" SIZE=25> $logselector
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
&footer("", $text{'log_return'});


### END of index.cgi ###.
