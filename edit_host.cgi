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

$whatfailed=$text{'host_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});
@cgiconf=&parse_config($config{'cgi_config'});

@hosts=&find_struct('host', \@conf);

$host=0;
foreach $h (@hosts) {
 if ($h->{'value'} eq $in{'name'}) { $host=$h; last; }
}

if ($host) {
 $header=&text('host_header', $host->{'value'});
 $title=$text{'host_title_edit'};
} else {
 $header=$text{'host_create'};
 $title=$text{'host_title_create'};
}

&header($title, "", "host", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");


print <<EOM;
<HR>
<FORM ACTION="save_host.cgi" METHOD=POST>

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

if ($host) {
 print "<INPUT TYPE=hidden NAME=\"name\" VALUE=\"$in{'name'}\">";
} else {
 print "<TR><TD $cb><B>$text{'name'}</B></TD> <TD $cb COLSPAN=4><INPUT TYPE=text NAME=\"name\"></TD></TR>";
}

print <<EOM;
    <TR>
     <TD $cb>
      <B>$text{'host_alias'}</B>
     </TD>
     <TD $cb COLSPAN=3>
      <INPUT TYPE="text" NAME="hostalias" VALUE="$host->{'values'}->[0]" SIZE=45>
     </TD>
     <TD $cb ALIGN=right ROWSPAN=6 VALIGN=top>
      <TABLE BORDER=0 CELLPADDING=2 CELLSPACING=0>
       <TR>
        <TD $cb ALIGN=center COLSPAN=2>
         <B><U>$text{'host_notification'}</U></B>
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'host_not_period'}</B>
        </TD>
        <TD $cb>
         <SELECT NAME="notperiod">
EOM
print "         <OPTION VALUE=0";
 print ! $host->{'values'}->[6] ? " SELECTED" :"";
 print ">$text{'host_not_none'}\n";
 
 @periods=&find_struct('timeperiod', \@conf);

foreach $p (@periods) {
 print "         <OPTION VALUE=\"$p->{'value'}\"";
 print $p->{'value'} eq $host->{'values'}->[6] ? " SELECTED" :"";
 print ">$p->{'value'}\n";
}
if ($host->{'values'}->[7]) { $recovery=" CHECKED" }
                       else { $nrecovery=" CHECKED" }
if ($host->{'values'}->[8]) { $down=" CHECKED" }
                       else { $ndown=" CHECKED" }
if ($host->{'values'}->[9]) { $unreachable=" CHECKED" }
                       else { $nunreachable=" CHECKED" }
print <<EOM;
         </SELECT>
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'host_not_interval'}</B>
        </TD>
        <TD $cb>
         <INPUT TYPE="text" NAME="notinterval" VALUE="$host->{'values'}->[5]" SIZE=5>
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'host_not_recovery'}</B>
        </TD>
        <TD $cb COLSPAN=3>
         <INPUT TYPE=radio NAME="notrecovery" VALUE=1 SIZE=35$recovery> $text{'yes'}
         <INPUT TYPE=radio NAME="notrecovery" VALUE=0 SIZE=35$nrecovery> $text{'no'}
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'host_not_down'}</B>
        </TD>
        <TD $cb>
         <INPUT TYPE=radio NAME="notdown" VALUE=1 SIZE=35$down> $text{'yes'}
         <INPUT TYPE=radio NAME="notdown" VALUE=0 SIZE=35$ndown> $text{'no'}
        </TD>
       </TR>
       <TR>
        <TD $cb>
         <B>$text{'host_not_unreachable'}</B>
        </TD>
        <TD $cb>
         <INPUT TYPE=radio NAME="notunreachable" VALUE=1 SIZE=35$unreachable> $text{'yes'}
         <INPUT TYPE=radio NAME="notunreachable" VALUE=0 SIZE=35$nunreachable> $text{'no'}
        </TD>
       </TR>
      </TABLE>

     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'host_address'}</B>
     </TD>
     <TD $cb COLSPAN=3>
      <INPUT TYPE="text" NAME="address" VALUE="$host->{'values'}->[1]" SIZE=30>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'host_parent'}</B>
     </TD>
     <TD $cb COLSPAN=3>
      <SELECT NAME="parenthost">
EOM
print "      <OPTION VALUE=0";
 print ! $host->{'values'}->[2] ? " SELECTED" :"";
 print ">$text{'host_none'}\n";

foreach $h (@hosts) {
 next if ($h->{'value'} eq $host->{'value'});
 print "      <OPTION VALUE=\"$h->{'value'}\"";
 print $h->{'value'} eq $host->{'values'}->[2] ? " SELECTED" :"";
 print ">$h->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'host_check_command'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="checkcommand">
EOM
print "      <OPTION VALUE=0";
 print ! $host->{'values'}->[3] ? " SELECTED" :"";
 print ">$text{'host_check_command_none'}\n";

@commands=&find_struct('command', \@conf);

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print $c->{'value'} eq $host->{'values'}->[3] ? " SELECTED" :"";
 print ">$c->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
     <TD $cb>
      <B>$text{'host_max_attempts'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="maxattempts" VALUE="$host->{'values'}->[4]" SIZE=5>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'host_eventhandler'}</B>
     </TD>
     <TD $cb COLSPAN=3>
      <SELECT NAME="eventhandler">
EOM
print "      <OPTION VALUE=\"\"";
 print ! $host->{'values'}->[10] ? " SELECTED" :"";
 print ">$text{'host_eventhandler_none'}\n";

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print $c->{'value'} eq $host->{'values'}->[10] ? " SELECTED" :"";
 print ">$c->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
    </TR>
    <TR>
     <TD $cb VALIGN=center>
      <B>$text{'host_groups'}</B>
     </TD>
     <TD $cb COLSPAN=3>
      <SELECT NAME="groups" SIZE=4 MULTIPLE>
EOM

@hostgroups=&find_struct('hostgroup', \@conf);

foreach $g (@hostgroups) {
 local(@members);
 @members=split(/,/, $g->{'values'}->[2]);
 print "         <OPTION VALUE=\"$g->{'value'}\"";
 print indexof($host->{'value'}, @members) >= 0 ? " SELECTED" :"";
 print ">$g->{'value'}\n";
}

print <<EOM;
      </SELECT>
     </TD>
    </TR>
   </TABLE>
  </TD>
 </TR>
</TABLE>
<BR>

EOM


@cgihosts=&find_struct('hostextinfo', \@cgiconf);

foreach $h (@cgihosts) {
  if ($h->{'value'} eq $host->{'value'}) {
    $cgihost=$h;
    last;
  }
}

if ($cgihost) {
  $usecgiextinfo=" CHECKED";
} else {
  $nusecgiextinfo=" CHECKED";
}

print <<EOM;

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=4>
      <B>$text{'host_extinfo'}</B>
     </TD>
    </TR>
    <TR>

     <TD $cb>
      <B>$text{'host_use_cgiextinfo'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="usecgiextinfo" VALUE="1"$usecgiextinfo> $text{'yes'}
      <INPUT TYPE=radio NAME="usecgiextinfo" VALUE="0"$nusecgiextinfo> $text{'no'}
     </TD>

     <TD $cb>
      <B>$text{'host_notes_url'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="notesurl" SIZE=30 VALUE="$cgihost->{'values'}->[0]">
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'host_img_icon'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="imageicon" SIZE=30 VALUE="$cgihost->{'values'}->[1]">
     </TD>

     <TD $cb>
      <B>$text{'host_img_vrml'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="imagevrml" SIZE=30 VALUE="$cgihost->{'values'}->[2]">
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'host_img_gd2'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="imagegd" SIZE=30 VALUE="$cgihost->{'values'}->[3]">
     </TD>

     <TD $cb>
      <B>$text{'host_alt_tag'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=text NAME="alttag" SIZE=30 VALUE="$cgihost->{'values'}->[4]">
     </TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>
<BR>

EOM

if ($host) {
 print "<INPUT TYPE=submit VALUE=\"$text{'save'}\">\n";
 print "<INPUT NAME=\"delete\" TYPE=submit VALUE=\"$text{'host_delete'}\">";

print <<EOM;
</FORM>

<BR>

<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=2>
      <B>$text{'host_services'}</B>
     </TD>
    </TR>
    <TR>
     <TD>
      <TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 WIDTH=100%>
EOM

@services=&find_struct('service', \@conf);

$i=0;
foreach $s (@services) {

 next if ($s->{'value'} ne $host->{'value'});
 if ($i%4 == 0) { print "<TR>\n"; }
 print "<td><A HREF=\"edit_service.cgi?",
        "name=$s->{'values'}->[0]\&host=$host->{'value'}\">",
        "$s->{'values'}->[0]</A></TD>\n";

 if ($i%4 == 3) { print "</TR>\n"; }
 $i++;
}

if ((scalar(@services)-1)%4 != 3) { print "</TR>\n"; }
if (! @services) { print "<TR><TD><B>$text{'host_no_services'}</B></TD></TR>\n" }

print <<EOM;
      </TABLE>
     </TD>
    </TR>
   </TABLE>
  </TD>
 </TR>
</TABLE>
<A HREF="edit_service.cgi?host=$in{'name'}">$text{'host_new_service'}</A>
EOM


} else {
 print "<INPUT NAME=\"new\" TYPE=submit VALUE=\"$text{'host_create'}\"></FORM>";
}

print "<HR>\n";
&footer("list_hosts.cgi", $text{'host_return'});


### END of index.cgi ###.
