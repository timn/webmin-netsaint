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

#    Created 26.12.1999


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'contact_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@contacts=&find_struct('contact', \@conf);

$contact=0;
foreach $c (@contacts) {
 if ($c->{'value'} eq $in{'name'}) { $contact=$c; break; }
}

if ($contact) {
 $header=&text('contact_header', $contact->{'value'});
 $title=$text{'contact_title_edit'};
} else {
 $header=$text{'contact_create'};
 $title=$text{'contact_title_create'};
}

&header($title, "", "contact", 1, 0, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");


print <<EOM;
<HR>
<FORM ACTION="save_contact.cgi" METHOD=POST>

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

if ($contact) {
 print "<INPUT TYPE=hidden NAME=\"name\" VALUE=\"$in{'name'}\">";
} else {
 print "<TR><TD $cb><B>$text{'name'}</B></TD> <TD $cb COLSPAN=4><INPUT TYPE=text NAME=\"name\"></TD></TR>";
}

print <<EOM;
    <TR>
     <TD $cb>
      <B>$text{'contact_alias'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="alias" VALUE="$contact->{'values'}->[0]" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'contact_email'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="email" VALUE="$contact->{'values'}->[11]" SIZE=35>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'contact_pager'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE="text" NAME="pager" VALUE="$contact->{'values'}->[12]" SIZE=35>
     </TD>
    </TR>
   </TABLE>
  </TD>
 </TR>
</TABLE>
<BR>
EOM

if ($contact->{'values'}->[3]) { $sr=" CHECKED" }
                          else { $nsr=" CHECKED" }
if ($contact->{'values'}->[4]) { $sc=" CHECKED" }
                          else { $nsc=" CHECKED" }
if ($contact->{'values'}->[5]) { $sw=" CHECKED" }
                          else { $nsw=" CHECKED" }
if ($contact->{'values'}->[6]) { $hr=" CHECKED" }
                          else { $nhr=" CHECKED" }
if ($contact->{'values'}->[7]) { $hd=" CHECKED" }
                          else { $nhd=" CHECKED" }
if ($contact->{'values'}->[8]) { $hu=" CHECKED" }
                          else { $nhu=" CHECKED" }


print <<EOM;
<TABLE BORDER=2 CELLPADDING=0 CELLSPACING=0 WIDTH=100% $cb>
 <TR>
  <TD>
   <TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100% $cb>
    <TR>
     <TD $tb COLSPAN=5>
      <B>$text{'contact_notifications'}</B>
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'contact_serv_rec'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="notservrec" VALUE=1 SIZE=35$sr> $text{'yes'}
      <INPUT TYPE=radio NAME="notservrec" VALUE=0 SIZE=35$nsr> $text{'no'}
     </TD>
     <TD $cb>
      <B>$text{'contact_host_rec'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="nothostrec" VALUE=1 SIZE=35$hr> $text{'yes'}
      <INPUT TYPE=radio NAME="nothostrec" VALUE=0 SIZE=35$nhr> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'contact_serv_crit'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="notservcrit" VALUE=1 SIZE=35$sc> $text{'yes'}
      <INPUT TYPE=radio NAME="notservcrit" VALUE=0 SIZE=35$nsc> $text{'no'}
     </TD>
     <TD $cb>
      <B>$text{'contact_host_down'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="nothostdown" VALUE=1 SIZE=35$hd> $text{'yes'}
      <INPUT TYPE=radio NAME="nothostdown" VALUE=0 SIZE=35$nhd> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'contact_serv_warn'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="notservwarn" VALUE=1 SIZE=35$sw> $text{'yes'}
      <INPUT TYPE=radio NAME="notservwarn" VALUE=0 SIZE=35$nsw> $text{'no'}
     </TD>
     <TD $cb>
      <B>$text{'contact_host_unre'}</B>
     </TD>
     <TD $cb>
      <INPUT TYPE=radio NAME="nothostunre" VALUE=1 SIZE=35$hu> $text{'yes'}
      <INPUT TYPE=radio NAME="nothostunre" VALUE=0 SIZE=35$nhu> $text{'no'}
     </TD>
    </TR>
    <TR>
     <TD $cb>
      <B>$text{'contact_svc_period'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="svcperiod">
EOM
print "      <OPTION VALUE=0";
 print ! $contact->{'values'}->[1] ? " SELECTED" :"";
 print ">$text{'contact_not_none'}\n";
 
 @periods=&find_struct('timeperiod', \@conf);

foreach $p (@periods) {
 print "      <OPTION VALUE=\"$p->{'value'}\"";
 print $p->{'value'} eq $contact->{'values'}->[1] ? " SELECTED" :"";
 print ">$p->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>

     <TD $cb>
      <B>$text{'contact_host_period'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="hostperiod">
EOM
print "      <OPTION VALUE=0";
 print ! $contact->{'values'}->[2] ? " SELECTED" :"";
 print ">$text{'contact_not_none'}\n";
 
foreach $p (@periods) {
 print "      <OPTION VALUE=\"$p->{'value'}\"";
 print $p->{'value'} eq $contact->{'values'}->[2] ? " SELECTED" :"";
 print ">$p->{'value'}\n";
}
print <<EOM;
      </SELECT>
     </TD>
    </TR>

    <TR>
     <TD $cb VALIGN=top>
      <B>$text{'contact_serv_comm'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="servcomm" SIZE=5 MULTIPLE>
EOM

@commands=&find_struct('command', \@conf);
@serv_comm=split(/,/, $contact->{'values'}->[9]);

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print indexof($c->{'value'}, @serv_comm) >= 0 ? " SELECTED" :"";
 print ">$c->{'value'}\n";
}

print <<EOM;
      </SELECT>
     </TD>
     <TD $cb VALIGN=top>
      <B>$text{'contact_host_comm'}</B>
     </TD>
     <TD $cb>
      <SELECT NAME="hostcomm" SIZE=5 MULTIPLE>
EOM

@host_comm=split(/,/, $contact->{'values'}->[10]);

foreach $c (@commands) {
 print "      <OPTION VALUE=\"$c->{'value'}\"";
 print indexof($c->{'value'}, @host_comm) >= 0 ? " SELECTED" :"";
 print ">$c->{'value'}\n";
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

if ($contact) {
 print "<INPUT TYPE=submit VALUE=\"$text{'save'}\">\n";
 print "<INPUT NAME=\"delete\" TYPE=submit VALUE=\"$text{'contact_delete'}\">";
} else {
 print "<INPUT TYPE=submit NAME=\"new\" VALUE=\"$text{'contact_create'}\">";
}

print "</FORM><HR>\n";
&footer("list_contacts.cgi", $text{'contact_return'});


### END of edit_contact.cgi ###.
