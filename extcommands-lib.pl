
#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999/2000 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
#    Written by Tim Niemueller <tim@niemueller.de> - http://www.niemueller.de
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    Created: 03.04.2000

@posscomm = ("ADD_HOST_COMMENT", "ADD_SVC_COMMENT", "DEL_HOST_COMMENT",
             "DEL_ALL_HOST_COMMENTS", "DEL_SVC_COMMENT", "DEL_ALL_SVC_COMMENTS",
             "DELAY_HOST_NOTIFICATION", "DELAY_SVC_NOTIFICATION",
             "SCHEDULE_SVC_CHECK", "SCHEDULE_HOST_SVC_CHECKS",
             "ENABLE_SVC_CHECK", "DISABLE_SVC_CHECK", "ENABLE_SVC_NOTIFICATIONS",
             "DISABLE_HOST_SVC_NOTIFICATIONS", "ENABLE_HOST_SVC_CHECKS",
             "DISABLE_HOST_SVC_CHECKS", "ENABLE_HOST_NOTIFICATIONS",
             "DISABLE_HOST_NOTIFICATIONS", "ENABLE_ALL_NOTIFICATIONS_BEYOND_HOST",
             "DISABLE_ALL_NOTIFICATIONS_BEYOND_HOST", "ENTER_STANDBY_MODE",
             "ENTER_ACTIVE_MODE", "SHUTDOWN_PROGRAM", "RESTART_PROGRAM");
@posscomm = sort @posscomm;

sub commselect {
 local($output, $o);
 $output = "<SELECT NAME=\"comm\">\n";
 foreach $o (@posscomm) {
  $output .= "<OPTION";
  $output .= $_[0] eq $o ? " SELECTED" : "";
  $output .= ">$o\n";
 }
 $output .= "</SELECT>\n";
}


sub parse_extcommands {
 local(@lines, @commands);
 open(FILE, $config{'command_file'}) || &error("Could not open file $config{'command_file'}");
  @lines=<FILE>;
 close(FILE);

 @commands=();
 for (my $i=0; $i<@lines; $i++) {
   local $comm;
   chomp($lines[$i]);
   next if ($lines[$i] =~ /^#/);
   ($comm->{'time'}, $lines[$i]) = split(/ /, $lines[$i], 2);
   ($comm->{'comm'}, $comm->{'args'}) = split (/;/, $lines[$i], 2);
   $comm->{'line'} = $i;
   push(@commands, $comm);
 }

return @commands;
}

### END.