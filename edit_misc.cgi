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

$whatfailed=$text{'misc_error'};
require './netsaint-lib.pl';
$access{'misc'} || &error($text{'misc_notallowed'});

@conf=&parse_config($config{'main_config'});
@hostconf=&parse_config($config{'host_config'});

$tmp=&find_name('use_agressive_host_checking', \@conf);
if ($tmp->{'values'}->[0]) { $aggr=" CHECKED" }
                      else { $naggr=" CHECKED" }

$tmp=&find_name('program_mode', \@conf);
if ($tmp->{'values'}->[0] eq "a") { $progmode=" CHECKED" }
                             else { $nprogmode=" CHECKED" }

$tmp=&find_name('sleep_time', \@conf);
$sleeptime_value=$tmp->{'values'}->[0];

$tmp=&find_name('interval_length', \@conf);
$intervallength_value=$tmp->{'values'}->[0];
$useil=($intervallength_value) ? " CHECKED" : "";
$nuseil=($intervallength_value) ? "" : " CHECKED";


$tmp=&find_name('inter_check_delay_method', \@conf);
$icdm_v=$tmp->{'values'}->[0];

$icdm_smart=($icdm_v eq "s") ? " SELECTED" : "";
$icdm_no=($icdm_v eq "n") ? " SELECTED" : "";
$icdm_dumb=($icdm_v eq "d") ? " SELECTED" : "";

$tmp=&find_name('service_interleave_factor', \@conf);
$servintleavfact_value=($tmp->{'values'}->[0] ne "s") ? $tmp->{'values'}->[0] : "";
$servintleavsmart=($tmp->{'values'}->[0] eq "s") ? " CHECKED" : "";
$servintleavnsmart=($tmp->{'values'}->[0] ne "s") ? " CHECKED" : "";

$tmp=&find_name('max_concurrent_checks', \@conf);
$maxconcchk_value=$tmp->{'values'}->[0];

$tmp=&find_name('service_reaper_frequency', \@conf);
$servreapfreq_value=$tmp->{'values'}->[0];

$tmp=&find_name('global_host_event_handler', \@conf);
$global_host_event_handler_value=$tmp->{'values'}->[0];

$tmp=&find_name('global_service_event_handler', \@conf);
$global_service_event_handler_value=$tmp->{'values'}->[0];


&header($text{'misc_title'}, "", "misc", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");

print <<EOM;
<HR>
<FORM NAME="misc" ACTION="save_misc.cgi" METHOD=POST>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'misc_header'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_mode'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="progmode" VALUE="a" SIZE=35$progmode> $text{'misc_mode_active'}
      <INPUT TYPE=radio NAME="progmode" VALUE="s" SIZE=35$nprogmode> $text{'misc_mode_standby'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_aggressive'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="aggressivechecks" VALUE=1 SIZE=35$aggr> $text{'yes'}
      <INPUT TYPE=radio NAME="aggressivechecks" VALUE=0 SIZE=35$naggr> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_interval_length'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="useil" VALUE=0$nuseil> $text{'default'}
      <INPUT TYPE=radio NAME="useil" VALUE=1$useil>
      <INPUT TYPE="text" NAME="intervallength" VALUE="$intervallength_value" SIZE=5> $text{'seconds'}
     </TD>
    </TR>

    <TR>
     <TD $cb COLSPAN=2>
      <BR><BR><B><U>$text{'misc_eventh'}</U></B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_globeh_host'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="globhosteh">
EOM

@commands=&find_struct('command', \@hostconf);

print "      <OPTION VALUE=0";
 print ! $global_host_event_handler_value ? " SELECTED" :"";
 print ">$text{'host_check_command_none'}\n";

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print $c->{'value'} eq $global_host_event_handler_value ? " SELECTED" :"";
 print ">$c->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_globeh_serv'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="globserveh">
EOM

print "      <OPTION VALUE=0";
 print ! $global_service_event_handler_value ? " SELECTED" :"";
 print ">$text{'host_check_command_none'}\n";

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print $c->{'value'} eq $global_service_event_handler_value ? " SELECTED" :"";
 print ">$c->{'value'}\n";
}
print <<EOM;
      </SELECT>     </TD>
    </TR>

    <TR>
     <TD $cb COLSPAN=2>
      <BR><BR><B><U>$text{'misc_chkbehav'}</U></B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_sleep_time'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="sleeptime" VALUE="$sleeptime_value" SIZE=5> $text{'seconds'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_intchk_delmeth'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="intchkdelmeth">
       <OPTION VALUE="s"$icdm_smart>$text{'misc_intchk_smart'}
       <OPTION VALUE="n"$icdm_no>$text{'misc_intchk_no'}
       <OPTION VALUE="d"$icdm_dumb>$text{'misc_intchk_dumb'}
      </SELECT>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_serv_intleav_factor'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="servintleavsmart" VALUE=1$servintleavsmart> $text{'misc_servintleav_smart'}
      <INPUT TYPE=radio NAME="servintleavsmart" VALUE=0$servintleavnsmart> $text{'misc_servintleav_usrdef'}:
      <INPUT TYPE=text NAME="servintleavfact" VALUE="$servintleavfact_value">
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_max_conc_checks'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="maxconcchk" VALUE="$maxconcchk_value">
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'misc_serv_reap_freq'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="servreapfreq" VALUE="$servreapfreq_value">
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


### END of edit_misc.cgi ###.
