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

#    Created 20.12.1999


$whatfailed=$text{'index_error'};
require './netsaint-lib.pl';


&header($text{'index_title'}, "", "intro", 1, 1, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");
print "<HR>\n<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=100%>\n<TR><TD>";

@links=("edit_misc.cgi", "edit_files.cgi", "edit_logging.cgi",
        "edit_notifications.cgi", "list_hosts.cgi", "list_contacts.cgi",
        "list_commands.cgi", "list_extcommands.cgi", "list_timeperiods.cgi",
        "edit_cgi.cgi", "edit_auth.cgi");
@texts=("Miscellaneous", "Files", "Logging", "Notifications",
        "Hosts", "Contacts", "Commands", "External Commands",
        "Time Periods", "CGI", $text{'index_icon_auth'});
@images=("images/misc.icon.gif", "images/files.icon.gif", "images/logging.icon.gif",
         "images/notification.icon.gif", "images/hosts.icon.gif",
         "images/contacts.icon.gif", "images/commands.icon.gif", "images/commands.icon.gif",
         "images/timeperiods.icon.gif", "images/cgi.icon.gif", "images/icon.auth.gif");

if ($config{'output_url'}) {
  push(@links, $config{'output_url'});
  push(@texts, $text{'index_icon_output'});
  push(@images, "images/html.icon.gif");
}

&icons_table(\@links, \@texts, \@images, $config{'icons_per_row'});

if ($config{'show_logo'}) {
  print "\n</TD><TD ALIGN=center><TABLE BORDER=1 CELLPADDING=5><TR><TD><IMG SRC=\"images/logo.gif\" BORDER=0></TD></TR></TABLE><BR><BR>";
  print "<FONT COLOR=#505050>[ NetSaint Configuration $version ]</FONT>\n</TD></TR></TABLE>\n";
} else {
  print "</TD></TR><TR><TD>";
  print "\n<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=100%>\n";
  print "<TR><TD ALIGN=right><FONT COLOR=#505050><BR>[ NetSaint Configuration $version ]</FONT></TD></TR></TABLE>\n";
  print "</TD></TR></TABLE>";
}

print "<HR>\n";
&footer("/", $text{'index'});


### END of index.cgi ###.
