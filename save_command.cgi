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

#    Created 09.01.2000


$whatfailed=$text{'scommand_error'};
require './netsaint-lib.pl';


@conf=&parse_config($config{'host_config'});

@commands=&find_struct('command', \@conf);

$command=0;
foreach $c (@commands) {
 if ($c->{'value'} eq $in{'name'}) { $command=$c; last; }
}

if ($command && $in{'new'}) {
 # The host already exists and we try to create another one with its name
 &error(&text("scommand_already_exists", $in{'name'}));
}

if ($command) {
 if ($in{'delete'}) {
  $access{'commanddelete'} || &error($text{'scommand_notallowed_delete'});
 } else {
  $access{'commandedit'} || &error($text{'scommand_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'commandcreate'} || &error($text{'scommand_notallowed_create'});
 }
}


$cfile=&read_file_lines($config{'host_config'});

if ($command) {
 # the hostgroup exists, we change it
 if ($in{'delete'}) {
   # we delete an existing contact
   splice(@{$cfile}, $command->{'line'}, 1);
   &flush_file_lines();
   @conf=&parse_config($config{'host_config'});
 } else {

 $cfile->[$command->{'line'}]=join('=',
                                   "command[$command->{'value'}]",
                                   $in{'command'}
                                   );
 }
} else {
 if ($in{'delete'}) {
  &error(&text({'scommand_notfound'}, $in{'name'}));
 } else {
 push(@{$cfile}, join('=',
                      "command[$in{'name'}]",
                      $in{'command'}
                      )
      );
 }
}


&flush_file_lines();
if ($in{'delete'}) {
 &redirect("list_commands.cgi");
} else {
 &redirect("edit_command.cgi?name=$in{'name'}");
}

### END of save_command.cgi ###.
