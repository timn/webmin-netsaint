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

#    Created 08.04.2000


$whatfailed=$text{'sextcomm_error'};
require './netsaint-lib.pl';
require './extcommands-lib.pl';

@commands = &parse_extcommands();

$command=0;
foreach $c (@commands) {
 if ($c->{'line'} eq $in{'line'}) { $command=$c; last }
}

if ($command) {
 if ($in{'delete'}) {
  $access{'extcommdelete'} || &error($text{'sextcomm_notallowed_delete'});
 } else {
  $access{'extcommedit'} || &error($text{'sextcomm_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'extcommcreate'} || &error($text{'sextcomm_notallowed_create'});
 }
}


$cfile=&read_file_lines($config{'command_file'});

if ($command) {
 # the hostgroup exists, we change it
 if ($in{'delete'}) {
   # we delete an existing contact
   splice(@{$cfile}, $command->{'line'}, 1);
 } else {
   $cfile->[$command->{'line'}]="[" . time ."] $in{'comm'};$in{'arguments'}";
 }
} else {
 if ($in{'new'}) {
   $in{'line'} = scalar(@{$cfile});
   push(@{$cfile}, "[" . time ."] $in{'comm'};$in{'arguments'}");
 } else {
   &error(&text('sextcomm_notfound', $in{'line'}));
 }
}



&flush_file_lines();
if ($in{'delete'}) {
 &redirect("list_extcommands.cgi");
} else {
 &redirect("edit_extcommand.cgi?line=$in{'line'}");
}

### END of save_extcommand.cgi ###.
