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


require './netsaint-lib.pl';
$access{'logging'} || &error($text{'log_notallowed'});

$whatfailed=$text{'slogging_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});
$cfile=&read_file_lines($config{'main_config'});


if ($in{'loglevel'} !~ /^[12]$/) { &error(&text('slogging_invalid', $in{'loglevel'}, 'Log Level', '1 or 2')) }
$tmp=&find_name('log_level', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_level", $in{'loglevel'});
} else {
 push(@{$cfile}, join('=', "log_level", $in{'loglevel'}));
}


if ($in{'usesyslog'} !~ /^[01]$/) { &error(&text('slogging_invalid', $in{'usesyslog'}, 'Syslog Facility', '0 or 1')) }
$tmp=&find_name('use_syslog', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "use_syslog", $in{'usesyslog'});
} else {
 push(@{$cfile}, join('=', "use_syslog", $in{'usesyslog'}));
}

if ($in{'sysloglevel'} !~ /^[12]$/) { &error(&text('slogging_invalid', $in{'sysloglevel'}, 'Syslog Level', '1 or 2')) }
$tmp=&find_name('syslog_level', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "syslog_level", $in{'sysloglevel'});
} else {
 push(@{$cfile}, join('=', "syslog_level", $in{'sysloglevel'}));
}


if ($in{'notifications'} !~ /^[01]$/) {
 &error(&text('slogging_invalid', $in{'notifications'}, 'Log Notifications', '0 or 1'))
}
$tmp=&find_name('log_notifications', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_notifications", $in{'notifications'});
} else {
 push(@{$cfile}, join('=', "log_notifications", $in{'notifications'}));
}


if ($in{'serviceretries'} !~ /^[01]$/) {
 &error(&text('slogging_invalid', $in{'serviceretries'}, 'Log service retries', '0 or 1'))
}
$tmp=&find_name('log_service_retries', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_service_retries", $in{'serviceretries'});
} else {
 push(@{$cfile}, join('=', "log_service_retries", $in{'serviceretries'}));
}


if ($in{'hostretries'} !~ /^[01]$/) {
 &error(&text('slogging_invalid', $in{'hostretries'}, 'Log host retries', '0 or 1'))
}
$tmp=&find_name('log_host_retries', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_host_retries", $in{'hostretries'});
} else {
 push(@{$cfile}, join('=', "log_host_retries", $in{'hostretries'}));
}


if ($in{'eventhandler'} !~ /^[01]$/) {
 &error(&text('slogging_invalid', $in{'eventhandler'}, 'Log even handlers', '0 or 1'))
}
$tmp=&find_name('log_event_handlers', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_event_handlers", $in{'eventhandler'});
} else {
 push(@{$cfile}, join('=', "log_event_handlers", $in{'event_handler'}));
}


if ($in{'logrotate'} !~ /^[nhdwm]$/) {
 &error(&text('slogging_invalid', $in{'logrotate'}, $text{'slogging_err_inv_logrotate'}, $text{'slogging_err_inv_logrotate2'}))
}
$tmp=&find_name('log_rotation_method', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_rotation_method", $in{'logrotate'});
} else {
 push(@{$cfile}, join('=', "log_rotation_method", $in{'logrotate'}));
}


if (!$in{'logrotarch'}) {
 &error(&text('slogging_invalid', $in{'logrotarch'}, $text{'slogging_err_logrotarch'}, $text{'slogging_err_logrotarch2'}))
}
$tmp=&find_name('log_archive_path', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_archive_path", $in{'logrotarch'});
} else {
 push(@{$cfile}, join('=', "log_archive_path", $in{'logrotarch'}));
}


&flush_file_lines();
&redirect("edit_logging.cgi");

### END of save_logging.cgi ###.
