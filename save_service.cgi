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

#    Created 12.01.2000


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'sservice_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@services=&find_struct('service', \@conf);

$service=0;
foreach $s (@services) {
 if (($s->{'value'} eq $in{'host'}) && ($s->{'values'}->[0] eq $in{'name'})) { $service=$s; last; }
}

if ($service) {
 if ($in{'delete'}) {
  $access{'servicedelete'} || &error($text{'sservice_notallowed_delete'});
 } else {
  $access{'serviceedit'} || &error($text{'sservice_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'servicecreate'} || &error($text{'sservice_notallowed_create'});
 }
}

if ($service && $in{'new'}) {
 # The host already exists and we try to create another one with its name
 &error(&text("sservice_already_exists", $in{'name'}));
}


$in{'name'} || &error($text{'sservice_nodesc'});

if ($in{'notinterval'} !~ /^\d+$/) { &error(&text('sservice_miss_inv', $in{'notinterval'}, 'Notification interval')) }
if ($in{'maxattempts'} !~ /^\d+$/) { &error(&text('sservice_miss_inv', $in{'maxattempts'}, 'max attempts')) }
if ($in{'checkinterval'} !~ /^\d+$/) { &error(&text('sservice_miss_inv', $in{'checkinterval'}, 'check interval')) }
if ($in{'retryinterval'} !~ /^\d+$/) { &error(&text('sservice_miss_inv', $in{'retryinterval'}, 'retry interval')) }

if ($in{'notrecovery'} !~ /^[01]$/) {
 &error(&text('sservice_miss_inv', $in{'notrecovery'}, 'recovery notification (must be 0 or 1)'))
}
if ($in{'notcrit'} !~ /^[01]$/) {
 &error(&text('sservice_miss_inv', $in{'notcrit'}, 'critical notification (must be 0 or 1)'))
}
if ($in{'notwarn'} !~ /^[01]$/) {
 &error(&text('sservice_miss_inv', $in{'notwarn'}, 'warning notification (must be 0 or 1)'))
}

if ($in{'vanilla'} && !$in{'vanillacommand'}) { &error($text{'sservice_vanilla'}) }
if (!$in{'vanilla'} && !$in{'rawcommand'}) { &error($text{'sservice_rawcommand'}) }


if ($in{'vanilla'}) {
 $checkcommand=join("!", $in{'vanillacommand'}, split(/\s+/, $in{'vanillaarguments'}));
} else {
 $checkcommand=$in{'rawcommand'};
}

@cgroups=split(/\0/, $in{'contactgroups'});


$cfile=&read_file_lines($config{'host_config'});


if ($service) {
 # the service exists, we change it
 if ($in{'delete'}) {
   # we delete an existing contact
   splice(@{$cfile}, $service->{'line'}, 1);
   &flush_file_lines();
   @conf=&parse_config($config{'host_config'});
 } else {
    $cfile->[$service->{'line'}]=join('=',
                                      "service[$service->{'value'}]",
                                      join(';',
                                           $in{'name'},
                                           $in{'checkperiod'},
                                           $in{'maxattempts'},
                                           $in{'checkinterval'},
                                           $in{'retryinterval'},
                                           join(',', @cgroups),
                                           $in{'notinterval'},
                                           $in{'notperiod'},
                                           $in{'notrecovery'},
                                           $in{'notcrit'},
                                           $in{'notwarn'},
                                           $in{'eventhandler'},
                                           $checkcommand
                                           )
                                      );
 }
} else {
 if ($in{'delete'}) {
   &error(&text({'sservice_notfound'}, $in{'name'}));
 } else {
 push(@{$cfile}, join('=',
                      "service[$in{'host'}]",
                      join(';',
                           $in{'name'},
                           $in{'checkperiod'},
                           $in{'maxattempts'},
                           $in{'checkinterval'},
                           $in{'retryinterval'},
                           join(',', @cgroups),
                           $in{'notinterval'},
                           $in{'notperiod'},
                           $in{'notrecovery'},
                           $in{'notcrit'},
                           $in{'notwarn'},
                           $in{'eventhandler'},
                           $checkcommand
                           )
                       )
      );
 }
}


&flush_file_lines();
if ($in{'delete'}) {
  &redirect("edit_host.cgi?name=$in{'host'}");
} else {
  &redirect("edit_service.cgi?name=$in{'name'}&host=$in{'host'}");
}

### END of save_service.cgi ###.
