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

#    Created 06.04.2000

$whatfailed=$text{'sextcommopt_error'};
require './netsaint-lib.pl';
$access{'extcommedit'} || &error($text{'sextcommopt_notallowed'});


@conf=&parse_config($config{'main_config'});
$cfile=&read_file_lines($config{'main_config'});


if ($in{'interval'} !~ /^\d+$/ ) { &error(&text('sextcommopt_invalid', $in{'interval'}, $text{'sextcommopt_interval'}, $text{'sextcommopt_integer'})) }
$tmp=&find_name('command_check_interval', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "command_check_interval", $in{'interval'});
} else {
 push(@{$cfile}, join('=', "command_check_interval", $in{'interval'}));
}


if ($in{'check'} !~ /^[01]$/) {
 &error(&text('sectcommopt_invalid', $in{'check'}, $text{'sextcommopt_check'}, $text{'sextcommopt_1or0'})) }
$tmp=&find_name('check_external_commands', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "check_external_commands", $in{'check'});
} else {
 push(@{$cfile}, join('=', "check_external_commands", $in{'check'}));
}



&flush_file_lines();
&redirect("edit_extcommandoptions.cgi");

### END of save_extcommandoptions.cgi ###.
