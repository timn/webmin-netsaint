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

$whatfailed=$text{'scontactgroup_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@contactgroups=&find_struct('contactgroup', \@conf);

$contactgroup=0;
foreach $h (@contactgroups) {
 if ($h->{'value'} eq $in{'name'}) { $contactgroup=$h; last; }
}

if ($contactgroup) {
 if ($in{'delete'}) {
  $access{'contactgroupdelete'} || &error($text{'scontactgroup_notallowed_delete'});
 } else {
  $access{'contactgroupedit'} || &error($text{'scontactgroup_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'contactgroupcreate'} || &error($text{'scontactgroup_notallowed_create'});
 }
}

if ($contactgroup && $in{'new'}) {
 # The contactgroup already exists and we try to create another one with its name
 &error(&text("scontactgroup_already_exists", $in{'name'}));
}


$in{'contactgroupalias'} || &error($text{'scontactgroup_noalias'});


## @contacts=&find_struct('contact', \@conf);
@ccontacts=split(/\0/, $in{'members'});

foreach $h (@contacts) {
 if (&indexof($h->{'value'}, @ccontacts) < 0) {
  $mgroups=0;
  foreach $g (@contactgroups) {
   next if ($g->{'value'} eq $in{'name'});
   local(@lg);
   @lg=split(/,/, $g->{'values'}->[1]);
   if (&indexof($h->{'value'}, @lg) >= 0) { $mgroups++ }
  }
 if (!$mgroups) { &error(&text('scontactgroup_cannotremove', $h->{'value'})) }
 }
}


$cfile=&read_file_lines($config{'host_config'});


if ($contactgroup) {
 # the contactgroup exists, we change it
 if ($in{'delete'}) {
   # we delete an existing contact
   splice(@{$cfile}, $contactgroup->{'line'}, 1);
   &flush_file_lines();
   @conf=&parse_config($config{'host_config'});
 } else {

 $cfile->[$contactgroup->{'line'}]=join('=',
                                        "contactgroup[$contactgroup->{'value'}]",
                                        join(';',
                                             $in{'contactgroupalias'},
                                             join(',', @ccontacts)
                                             )
                                        );
 }
} else {
 if ($in{'delete'}) {
  &error(&text({'scontactgroup_notfound'}, $in{'name'}));
 } else {
 push(@{$cfile}, join('=',
                      "contactgroup[$in{'name'}]",
                      join(';',
                           $in{'contactgroupalias'},
                           join(',', @ccontacts)
                           )
                      )
      );
 }
}


&flush_file_lines();
if ($in{'delete'}) {
  &redirect("list_contacts.cgi");
} else {
  &redirect("edit_contactgroup.cgi?name=$in{'name'}");
}

### END of save_contactgroup.cgi ###.
