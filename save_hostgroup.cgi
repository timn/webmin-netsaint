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


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'shostgroup_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@hostgroups=&find_struct('hostgroup', \@conf);

$hostgroup=0;
foreach $h (@hostgroups) {
 if ($h->{'value'} eq $in{'name'}) { $hostgroup=$h; last; }
}

if ($hostgroup) {
 if ($in{'delete'}) {
  $access{'hostgroupdelete'} || &error($text{'shostgroup_notallowed_delete'});
 } else {
  $access{'hostgroupedit'} || &error($text{'shostgroup_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'hostgroupcreate'} || &error($text{'shostgroup_notallowed_create'});
 }
}

if ($hostgroup && $in{'new'}) {
 # The hostgroup already exists and we try to create another one with its name
 &error(&text("shostgroup_already_exists", $in{'name'}));
}


$in{'hostgroupalias'} || &error($text{'shostgroup_noalias'});


@hosts=&find_struct('host', \@conf);
@chosts=split(/\0/, $in{'members'});

foreach $h (@hosts) {
 if (&indexof($h->{'value'}, @chosts) < 0) {
  $mgroups=0;
  foreach $g (@hostgroups) {
   next if ($g->{'value'} eq $in{'name'});
   local(@lg);
   @lg=split(/,/, $g->{'values'}->[2]);
   if (&indexof($h->{'value'}, @lg) >= 0) { $mgroups++ }
  }
 if (!$mgroups) { &error(&text('shostgroup_cannotremove', $h->{'value'})) }
 }
}

@cgroups=split(/\0/, $in{'contactgroups'});


$cfile=&read_file_lines($config{'host_config'});


if ($hostgroup) {
 # the hostgroup exists, we change it

 if ($in{'delete'}) {
   # we delete an existing host
   splice(@{$cfile}, $hostgroup->{'line'}, 1);
   &flush_file_lines();
   @conf=&parse_config($config{'host_config'});
 } else {
   # we save an existing host
   $cfile->[$hostgroup->{'line'}]=join('=',
                                       "hostgroup[$hostgroup->{'value'}]",
                                        join(';',
                                             $in{'hostgroupalias'},
                                             join(',', @cgroups),
                                             join(',', @chosts)
                                             )
                                        );
 }
} else {
 if ($in{'delete'}) {
  &error(&text({'shostgroup_notfound'}, $in{'name'}));
 } else {
 push(@{$cfile}, join('=',
                      "hostgroup[$in{'name'}]",
                      join(';',
                           $in{'hostgroupalias'},
                           join(',', @cgroups),
                           join(',', @chosts)
                           )
                           )
      );
 }
}


&flush_file_lines();
if ($in{'delete'}) {
  &redirect("list_hosts.cgi");
} else {
  &redirect("edit_hostgroup.cgi?name=$in{'name'}");
}

### END of save_hostgroup.cgi ###.
