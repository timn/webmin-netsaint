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


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'index_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));


&header($text{'index_title'}, "", "intro", 1, 1, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de>Home://page</A>");
print "<HR>\n";

@links=("edit_files.cgi", "edit_logging.cgi", "edit_misc.cgi" , "edit_html.cgi",
        "edit_notifications.cgi", "list_hosts.cgi", "list_contacts.cgi",
        "list_commands.cgi", "list_timeperiods.cgi",
        "edit_cgi.cgi");
@texts=("Files", "Logging", "Miscellaneous", "HTML", "Notifications",
        "Hosts", "Contacts", "Commands", "Time Periods", "CGI");
@images=("images/files.icon.gif", "images/logging.icon.gif", "images/misc.icon.gif",
         "images/html.icon.gif", "images/notification.icon.gif", "images/hosts.icon.gif",
         "images/contacts.icon.gif", "images/commands.icon.gif",
         "images/timeperiods.icon.gif", "images/cgi.icon.gif");

&icons_table(\@links, \@texts, \@images, $config{'icons_per_row'});

print "\n<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=100%>\n";
print "<TR><TD ALIGN=right><FONT COLOR=#505050>[ NetSaint Configuration $version ]</FONT></TD></TR></TABLE>\n";
print "<HR>\n";
&footer("/", $text{'index'});


### END of index.cgi ###.
