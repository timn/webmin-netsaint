
do '../web-lib.pl';
&init_config("netsaint");

# acl_security_form(&options)
# Output HTML for editing security options for the apache module
sub acl_security_form
{

print "<TR><TD><B><B>$text{'acl_files'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"files\" VALUE=\"1\"", ($_[0]->{'files'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"files\" VALUE=\"0\"", ($_[0]->{'files'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_logging'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"logging\" VALUE=\"1\"", ($_[0]->{'logging'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"logging\" VALUE=\"0\"", ($_[0]->{'logging'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_misc'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"misc\" VALUE=\"1\"", ($_[0]->{'misc'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"misc\" VALUE=\"0\"", ($_[0]->{'misc'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_html'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"html\" VALUE=\"1\"", ($_[0]->{'html'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"html\" VALUE=\"0\"", ($_[0]->{'html'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_not'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"not\" VALUE=\"1\"", ($_[0]->{'not'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"not\" VALUE=\"0\"", ($_[0]->{'not'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_cgi'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"cgi\" VALUE=\"1\"", ($_[0]->{'cgi'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"cgi\" VALUE=\"0\"", ($_[0]->{'cgi'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_host_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"hostedit\" VALUE=\"1\"", ($_[0]->{'hostedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"hostedit\" VALUE=\"0\"", ($_[0]->{'hostedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_host_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"hostcreate\" VALUE=\"1\"", ($_[0]->{'hostcreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"hostcreate\" VALUE=\"0\"", ($_[0]->{'hostcreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_host_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"hostdelete\" VALUE=\"1\"", ($_[0]->{'hostdelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"hostdelete\" VALUE=\"0\"", ($_[0]->{'hostdelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_hostgroup_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"hostgroupedit\" VALUE=\"1\"", ($_[0]->{'hostgroupedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"hostgroupedit\" VALUE=\"0\"", ($_[0]->{'hostgroupedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_hostgroup_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"hostgroupcreate\" VALUE=\"1\"", ($_[0]->{'hostgroupcreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"hostgroupcreate\" VALUE=\"0\"", ($_[0]->{'hostgroupcreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_hostgroup_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"hostgroupdelete\" VALUE=\"1\"", ($_[0]->{'hostgroupdelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"hostgroupdelete\" VALUE=\"0\"", ($_[0]->{'hostgroupdelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_contact_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"contactedit\" VALUE=\"1\"", ($_[0]->{'contactedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"contactedit\" VALUE=\"0\"", ($_[0]->{'contactedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_contact_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"contactcreate\" VALUE=\"1\"", ($_[0]->{'contactcreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"contactcreate\" VALUE=\"0\"", ($_[0]->{'contactcreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_contact_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"contactdelete\" VALUE=\"1\"", ($_[0]->{'contactdelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"contactdelete\" VALUE=\"0\"", ($_[0]->{'contactdelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_contactgroup_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"contactgroupedit\" VALUE=\"1\"", ($_[0]->{'contactgroupedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"contactgroupedit\" VALUE=\"0\"", ($_[0]->{'contactgroupedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_contactgroup_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"contactgroupcreate\" VALUE=\"1\"", ($_[0]->{'contactgroupcreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"contactgroupcreate\" VALUE=\"0\"", ($_[0]->{'contactgroupcreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_contactgroup_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"contactgroupdelete\" VALUE=\"1\"", ($_[0]->{'contactgroupdelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"contactgroupdelete\" VALUE=\"0\"", ($_[0]->{'contactgroupdelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_command_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"commandedit\" VALUE=\"1\"", ($_[0]->{'commandedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"commandedit\" VALUE=\"0\"", ($_[0]->{'commandedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_command_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"commandcreate\" VALUE=\"1\"", ($_[0]->{'commandcreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"commandcreate\" VALUE=\"0\"", ($_[0]->{'commandcreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_command_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"commanddelete\" VALUE=\"1\"", ($_[0]->{'commanddelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"commanddelete\" VALUE=\"0\"", ($_[0]->{'commanddelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_timeperiod_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"timeperiodedit\" VALUE=\"1\"", ($_[0]->{'timeperiodedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"timeperiodedit\" VALUE=\"0\"", ($_[0]->{'timeperiodedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_timeperiod_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"timeperiodcreate\" VALUE=\"1\"", ($_[0]->{'timeperiodcreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"timeperiodcreate\" VALUE=\"0\"", ($_[0]->{'timeperiodcreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_timeperiod_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"timeperioddelete\" VALUE=\"1\"", ($_[0]->{'timeperioddelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"timeperioddelete\" VALUE=\"0\"", ($_[0]->{'timeperioddelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_service_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"serviceedit\" VALUE=\"1\"", ($_[0]->{'serviceedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"serviceedit\" VALUE=\"0\"", ($_[0]->{'serviceedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_service_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"servicecreate\" VALUE=\"1\"", ($_[0]->{'servicecreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"servicecreate\" VALUE=\"0\"", ($_[0]->{'servicecreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_service_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"servicedelete\" VALUE=\"1\"", ($_[0]->{'servicedelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"servicedelete\" VALUE=\"0\"", ($_[0]->{'servicedelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";


print "<TR><TD><B>$text{'acl_extcomm_edit'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"extcommedit\" VALUE=\"1\"", ($_[0]->{'extcommedit'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"extcommedit\" VALUE=\"0\"", ($_[0]->{'extcommedit'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_extcomm_create'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"extcommcreate\" VALUE=\"1\"", ($_[0]->{'extcommcreate'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"extcommcreate\" VALUE=\"0\"", ($_[0]->{'extcommcreate'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

print "<TR><TD><B>$text{'acl_extcomm_delete'}</B></TD>";
print "<TD><INPUT TYPE=radio NAME=\"extcommdelete\" VALUE=\"1\"", ($_[0]->{'extcommdelete'}) ? " CHECKED" : "", "> $text{'yes'} ";
print "<INPUT TYPE=radio NAME=\"extcommdelete\" VALUE=\"0\"", ($_[0]->{'extcommdelete'}) ? "" : " CHECKED", "> $text{'no'}</TD><TR>\n";

}

# acl_security_save(&options)
# Parse the form for security options for the apache module
sub acl_security_save
{

 $_[0]->{'files'} = $in{'files'};
 $_[0]->{'html'} = $in{'html'};
 $_[0]->{'cgi'} = $in{'cgi'};
 $_[0]->{'misc'} = $in{'misc'};
 $_[0]->{'not'} = $in{'not'};
 $_[0]->{'logging'} = $in{'logging'};
 
 $_[0]->{'hostedit'} = $in{'hostedit'};
 $_[0]->{'hostcreate'} = $in{'hostcreate'};
 $_[0]->{'hostdelete'} = $in{'hostdelete'};

 $_[0]->{'hostgroupedit'} = $in{'hostgroupedit'};
 $_[0]->{'hostgroupcreate'} = $in{'hostgroupcreate'};
 $_[0]->{'hostgroupdelete'} = $in{'hostgroupdelete'};

 $_[0]->{'contactedit'} = $in{'contactedit'};
 $_[0]->{'contactcreate'} = $in{'contactcreate'};
 $_[0]->{'contactdelete'} = $in{'contactdelete'};

 $_[0]->{'contactgroupedit'} = $in{'contactgroupedit'};
 $_[0]->{'contactgroupcreate'} = $in{'contactgroupcreate'};
 $_[0]->{'contactgroupdelete'} = $in{'contactgroupdelete'};

 $_[0]->{'commandedit'} = $in{'commandedit'};
 $_[0]->{'commandcreate'} = $in{'commandcreate'};
 $_[0]->{'commanddelete'} = $in{'commanddelete'};

 $_[0]->{'timeperiodedit'} = $in{'timeperiodedit'};
 $_[0]->{'timeperiodcreate'} = $in{'timeperiodcreate'};
 $_[0]->{'timeperioddelete'} = $in{'timeperioddelete'};

 $_[0]->{'serviceedit'} = $in{'serviceedit'};
 $_[0]->{'servicecreate'} = $in{'servicecreate'};
 $_[0]->{'servicedelete'} = $in{'servicedelete'};

 $_[0]->{'extcommedit'} = $in{'extcommedit'};
 $_[0]->{'extcommcreate'} = $in{'extcommcreate'};
 $_[0]->{'extcommdelete'} = $in{'extcommdelete'};

}

### END.