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

#    Created 23.12.1999


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';
$access{'html'} || &error($text{'html_notallowed'});

$whatfailed=$text{'html_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});

$phys_html_selector=&file_chooser_button('log', 1, 0);

$tmp=&find_name('auto_generate_html', \@conf);
if ($tmp->{'values'}->[0]) { $autohtml=" CHECKED" }
                      else { $nautohtml=" CHECKED" }

$tmp=&find_name('physical_html_path', \@conf);
$phys_html_value=$tmp->{'values'}->[0];

$tmp=&find_name('url_html_path', \@conf);
$url_html_path_value=$tmp->{'values'}->[0];

$tmp=&find_name('url_cgibin_path', \@conf);
$url_cgibin_path_value=$tmp->{'values'}->[0];


&header($text{'html_title'}, "", "html", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

print <<EOM;
<HR>
<FORM NAME="html" ACTION="save_html.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'html_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'html_autohtml'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="autohtml" VALUE=1 SIZE=35$autohtml> $text{'yes'}
      <INPUT TYPE=radio NAME="autohtml" VALUE=0 SIZE=35$nautohtml> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'html_physical_html_path'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="physicalhtmlpath" VALUE="$phys_html_value" SIZE=35> $phys_html_selector
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'html_url_html_path'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="urlhtmlpath" VALUE="$url_html_path_value" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'html_url_cgibin_path'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="urlcgibinpath" VALUE="$url_cgibin_path_value" SIZE=35>
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
&footer("", $text{'misc_return'});


### END of index.cgi ###.
