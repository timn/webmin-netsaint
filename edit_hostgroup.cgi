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

#    Created 22.12.1999


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'hostgroup_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@hostgroups=&find_struct('hostgroup', \@conf);

$host=0;
foreach $h (@hostgroups) {
 if ($h->{'value'} eq $in{'name'}) { $host=$h; break; }
}

if ($host) {
$header=&text('hostgroup_header', $host->{'value'});
 $title=$text{'hostgroup_title_edit'};
} else {
 $header=$text{'hostgroup_create'};
 $title=$text{'hostgroup_title_create'};
}

@members=split(/,/, $host->{'values'}->[2]);
@contacts=split(/,/, $host->{'values'}->[1]);

&header($title, "", "hostgroup", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");


print <<EOM;
<HR>
<FORM ACTION="save_hostgroup.cgi" METHOD=POST>

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
      <B>$text{'hostgroup_alias'}</B>
     </TD>
     <TD $cb COLSPAN=3>
      <INPUT TYPE="text" NAME="hostgroupalias" VALUE="$host->{'values'}->[0]" SIZE=45>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'hostgroup_members'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="members" SIZE=5 MULTIPLE>
EOM

@hosts=&find_struct('host', \@conf);
@hosts = sort { $a->{'value'} cmp $b->{'value'} } @hosts;

foreach $h (@hosts) {
 print "      <OPTION VALUE=\"$h->{'value'}\"";
 print indexof($h->{'value'}, @members) >= 0 ? " SELECTED" :"";
 print ">$h->{'value'}\n";
}

print <<EOM;
      </SELECT>
     </TD>
     <TD $cb>
      <B>$text{'hostgroup_contactgroups'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="contactgroups" SIZE=5 MULTIPLE>
EOM

@contactgroups=&find_struct('contactgroup', \@conf);
@contactgroups = sort { $a->{'value'} cmp $b->{'value'} } @contactgroups;

foreach $g (@contactgroups) {
 print "      <OPTION VALUE=\"$g->{'value'}\"";
 print indexof($g->{'value'}, @contacts) >= 0 ? " SELECTED" :"";
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

EOM

if ($host) {
 print "<INPUT TYPE=submit VALUE=\"$text{'save'}\">\n";
 print "<INPUT NAME=\"delete\" TYPE=submit VALUE=\"$text{'hostgroup_delete'}\">";
} else {
 print "<INPUT TYPE=submit NAME=\"new\" VALUE=\"$text{'hostgroup_create'}\">";
}

print "</FORM><HR>\n";
&footer("list_hosts.cgi", $text{'hostgroup_return'});


### END of index.cgi ###.
