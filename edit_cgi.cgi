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

#    Created 22.12.1999

$whatfailed=$text{'cgi_error'};
require './netsaint-lib.pl';
$access{'cgi'} || &error($text{'cgi_notallowed'});


$maincfgselector=&file_chooser_button('hostcfg', 0, 0);
$phys_html_selector=&file_chooser_button('physicalhtmlpath', 0, 0);

@conf=&parse_config($config{'cgi_config'});

$tmp=&find_name('main_config_file', \@conf);
$main_config_file_value=$tmp->{'values'}->[0];

$tmp=&find_name('physical_html_path', \@conf);
$phys_html_value=$tmp->{'values'}->[0];

$tmp=&find_name('url_html_path', \@conf);
$url_html_path_value=$tmp->{'values'}->[0];

$tmp=&find_name('url_cgibin_path', \@conf);
$url_cgibin_path_value=$tmp->{'values'}->[0];

$tmp=&find_name('process_check_command', \@conf);
$process_check_command_value=$tmp->{'values'}->[0];

$tmp=&find_name('suppress_alert_window', \@conf);
if ($tmp->{'values'}->[0]) { $suppalwin=" CHECKED" }
                      else { $nsuppalwin=" CHECKED" }

$tmp=&find_name('refresh_rate', \@conf);
$refresh_rate_value=$tmp->{'values'}->[0];

$tmp=&find_name('html_table_fg_color', \@conf);
$table_fg_color_value=$tmp->{'values'}->[0];

$tmp=&find_name('html_table_bg_color', \@conf);
$table_bg_color_value=$tmp->{'values'}->[0];

$tmp=&find_name('html_table_bg_odd_color', \@conf);
$table_bg_odd_color_value=$tmp->{'values'}->[0];

$tmp=&find_name('html_table_bg_even_color', \@conf);
$table_bg_even_color_value=$tmp->{'values'}->[0];


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
    <TR>
     <TD $cb>
      <B>$text{'cgi_physical_html_path'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="physicalhtmlpath" VALUE="$phys_html_value" SIZE=35> $phys_html_selector
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'cgi_url_html_path'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="urlhtmlpath" VALUE="$url_html_path_value" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'cgi_url_cgibin_path'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="urlcgibinpath" VALUE="$url_cgibin_path_value" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'cgi_process_check_command'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="processcheckcommand" VALUE="$process_check_command_value" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'cgi_suppress_alert_window'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="suppalwin" VALUE=1 SIZE=35$suppalwin> $text{'yes'}
      <INPUT TYPE=radio NAME="suppalwin" VALUE=0 SIZE=35$nsuppalwin> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'cgi_refresh_rate'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="refreshrate" VALUE="$refresh_rate_value" SIZE=5> $text{'seconds'} $text{'cgi_norefresh'}
     </TD>
    </TR>
     <TD $cb>
      <B>$text{'cgi_table_fg_color'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="tablefgcolor" VALUE="$table_fg_color_value" SIZE=8>
     </TD>
    </TR>
    </TR>
     <TD $cb>
      <B>$text{'cgi_table_bg_color'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="tablebgcolor" VALUE="$table_bg_color_value" SIZE=8>
     </TD>
    </TR>
    </TR>
     <TD $cb>
      <B>$text{'cgi_table_bg_odd_color'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="tablebgoddcolor" VALUE="$table_bg_odd_color_value" SIZE=8>
     </TD>
    </TR>
    </TR>
     <TD $cb>
      <B>$text{'cgi_table_bg_even_color'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="tablebgevencolor" VALUE="$table_bg_even_color_value" SIZE=8>
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


### END of edit_cgi.cgi ###.
