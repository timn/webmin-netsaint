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
$access{'cgi'} || &error($text{'cgi_notallowed'});

$whatfailed=$text{'cgi_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

$maincfgselector=&file_chooser_button('hostcfg', 0, 0);

@conf=&parse_config($config{'cgi_config'});

$tmp=&find_name('main_config_file', \@conf);
$main_config_file_value=$tmp->{'values'}->[0];

&header($text{'cgi_title'}, "", "cgi", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

print <<EOM;
<HR>
<FORM NAME="cgi" ACTION="save_cgi.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'cgi_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'cgi_main_config_file'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="mainconfig" VALUE="$main_config_file_value" SIZE=35> $maincfgselector
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
&footer("", $text{'cgi_return'});


### END of index.cgi ###.
