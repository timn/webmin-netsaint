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


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';
$access{'not'} || &error($text{'ntfcs_notallowed'});

$whatfailed=$text{'ntfcs_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});

$tmp=&find_name('generic_summary', \@conf);
$summary_value=$tmp->{'values'}->[0];

$tmp=&find_name('admin_pager', \@conf);
$pager_value=$tmp->{'values'}->[0];

$tmp=&find_name('admin_email', \@conf);
$email_value=$tmp->{'values'}->[0];


&header($text{'ntfcs_title'}, "", "notifications", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

print <<EOM;
<HR>
<FORM NAME="notifications" ACTION="save_notifications.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'ntfcs_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'ntfcs_summary'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="summary" VALUE="$summary_value" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'ntfcs_pager'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="pager" VALUE="$pager_value" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'ntfcs_email'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="email" VALUE="$email_value" SIZE=35>
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
&footer("", $text{'ntfcs_return'});


### END of index.cgi ###.
