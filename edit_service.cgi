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

#    Created 27.12.1999


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'service_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@services=&find_struct('service', \@conf);

$service=0;
foreach $h (@services) {
 if (($h->{'value'} eq $in{'host'}) && ($h->{'values'}->[0] eq $in{'name'})) { $service=$h; last; }
}

if ($service) {
 $header=&text('service_header', $service->{'values'}->[0], $service->{'value'});
 $title=$text{'service_title_edit'};
} else {
 $header=$text{'service_create'};
 $title=$text{'service_title_create'};
}


&header($title, "", "service", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");


print <<EOM;
<HR>
<FORM ACTION="save_service.cgi" METHOD=POST>
<INPUT TYPE=hidden NAME="host" VALUE="$in{'host'}">

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

if ($service) {
 print "<INPUT TYPE=hidden NAME=\"name\" VALUE=\"$in{'name'}\">";
} else {
print <<EOM;
    <TR>
     <TD $cb>
      <B>$text{'service_description'}</B>
     </TD>
     <TD $cb COLSPAN=3>
      <INPUT TYPE="text" NAME="name" VALUE="$service->{'values'}->[0]" SIZE=45>
     </TD>
EOM
}

print <<EOM;
    <TR>
     <TD $cb>
      <B>$text{'service_check_period'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="checkperiod">
EOM
print "       <OPTION VALUE=0";
 print ! $service->{'values'}->[1] ? " SELECTED" :"";
 print ">$text{'service_check_period_none'}\n";

 @periods=&find_struct('timeperiod', \@conf);
 
foreach $p (@periods) {
 print "       <OPTION VALUE=\"$p->{'value'}\"";
 print $p->{'value'} eq $service->{'values'}->[1] ? " SELECTED" :"";
 print ">$p->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
     <TD $cb>
      <B>$text{'service_max_attempts'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="maxattempts" VALUE="$service->{'values'}->[2]" SIZE=5>
     </TD>
     <TD $cb ALIGN=right ROWSPAN=5 VALIGN=top>
      <TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0>
       <TR>
        <TD $cb ALIGN=center COLSPAN=2>
         <B><U>$text{'service_notification'}</U></B>
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'service_not_period'}</B>
        </TD>
        <TD $cb>
         <SELECT NAME="notperiod">
EOM
print "         <OPTION VALUE=0";
 print ! $service->{'values'}->[7] ? " SELECTED" :"";
 print ">$text{'service_not_none'}\n";
 
foreach $p (@periods) {
 print "         <OPTION VALUE=\"$p->{'value'}\"";
 print $p->{'value'} eq $service->{'values'}->[7] ? " SELECTED" :"";
 print ">$p->{'value'}\n";
}
if ($service->{'values'}->[8]) { $recovery=" CHECKED" }
                       else { $nrecovery=" CHECKED" }
if ($service->{'values'}->[9]) { $crit=" CHECKED" }
                       else { $ncrit=" CHECKED" }
if ($service->{'values'}->[10]) { $warn=" CHECKED" }
                       else { $nwarn=" CHECKED" }
print <<EOM;
         </SELECT>
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'service_not_interval'}</B>
        </TD>
        <TD $cb>
         <INPUT TYPE="text" NAME="notinterval" VALUE="$service->{'values'}->[6]" SIZE=5>
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'service_not_recovery'}</B>
        </TD>
        <TD $cb COLSPAN=3>
         <INPUT TYPE=radio NAME="notrecovery" VALUE=1 SIZE=35$recovery> $text{'yes'}
         <INPUT TYPE=radio NAME="notrecovery" VALUE=0 SIZE=35$nrecovery> $text{'no'}
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'service_not_crit'}</B>
        </TD>
        <TD $cb>
         <INPUT TYPE=radio NAME="notcrit" VALUE=1 SIZE=35$crit> $text{'yes'}
         <INPUT TYPE=radio NAME="notcrit" VALUE=0 SIZE=35$ncrit> $text{'no'}
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'service_not_warn'}</B>
        </TD>
        <TD $cb>
         <INPUT TYPE=radio NAME="notwarn" VALUE=1 SIZE=35$warn> $text{'yes'}
         <INPUT TYPE=radio NAME="notwarn" VALUE=0 SIZE=35$nwarn> $text{'no'}
        </TD>
       </TR>
      </TABLE>

     </TD>
    </TR>

    <TR>
     <TD $cb>
      <B>$text{'service_check_interval'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="checkinterval" VALUE="$service->{'values'}->[3]" SIZE=5>
     </TD>
     <TD $cb>
      <B>$text{'service_retry_interval'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="retryinterval" VALUE="$service->{'values'}->[4]" SIZE=5>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'service_eventhandler'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="eventhandler">
EOM
print "      <OPTION VALUE=\"\"";
 print ! $service->{'values'}->[11] ? " SELECTED" :"";
 print ">$text{'service_eventhandler_none'}\n";

@commands=&find_struct('command', \@conf);

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print $c->{'value'} eq $service->{'values'}->[11] ? " SELECTED" :"";
 print ">$c->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
     <TD $cb VALIGN=top>
      <B>$text{'service_contactgroups'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="contactgroups" SIZE=4 MULTIPLE>
EOM

@contactgroups=&find_struct('contactgroup', \@conf);
@contacts=split(/,/, $service->{'values'}->[5]);

foreach $c (@contactgroups) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print &indexof($c->{'value'}, @contacts) >= 0 ? "SELECTED" : "";
 print ">$c->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
    </TR>
    <TR>
     <TD $cb COLSPAN=4>
      <B>$text{'service_command'}</B>
     </TD>
    </TR>
EOM

@parsedcommand=split(/!/, $service->{'values'}->[12]);

$commandfound=0;
foreach $c (@commands) {
 $commandfound++ if ($c->{'value'} eq $parsedcommand[0]);
}

if ($commandfound) {
 $vanilla=" CHECKED";
} else {
 $nvanilla=" CHECKED";
 $rawcommand=$service->{'values'}->[12];
}

print <<EOM;
    <TR>
     <TD $cb COLSPAN=4>
      <INPUT TYPE=radio NAME="vanilla" VALUE=1$vanilla> $text{'service_vanilla_command'}
      <SELECT NAME="vanillacommand">
EOM
print "      <OPTION VALUE=0";
 print ! $service->{'values'}->[12] ? " SELECTED" :"";
 print ">$text{'service_eventhandler_none'}\n";

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print $c->{'value'} eq $parsedcommand[0] ? " SELECTED" :"";
 print ">$c->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
    </TR>

    <TR>
     <TD $cb VALIGN=top ALIGN=right>
      $text{'service_vanilla_arguments'} <BR> $text{'service_vanilla_args_cmnt'}
     </TD>
     <TD $cb>
<TEXTAREA NAME="vanillaarguments" ROWS=4 COLS=40>
EOM
for (my $i=1; $i<@parsedcommand; $i++) {
print "$parsedcommand[$i]\n";
}
print <<EOM;
</TEXTAREA>
     </TD>
    </TR>

    <TR>
     <TD $cb>
      <INPUT TYPE=radio NAME="vanilla" VALUE=0$nvanilla> $text{'service_raw_command'}
     </TD>
     <TD $cb COLSPAN=3>
      <INPUT TYPE="text" NAME="rawcommand" VALUE="$rawcommand" SIZE=45>
     </TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>
EOM

if ($service) {
 print "<INPUT TYPE=submit VALUE=\"$text{'save'}\">\n";
 print "<INPUT NAME=\"delete\" TYPE=submit VALUE=\"$text{'service_delete'}\">";
} else {
 print "<INPUT TYPE=submit NAME=\"new\" VALUE=\"$text{'service_create'}\">";
}



print "</FORM><HR>\n";
&footer("edit_host.cgi?name=$in{'host'}", &text('service_return', $in{'host'}));


### END of edit_service.cgi ###.
