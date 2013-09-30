Name:		puppet-openstack	
Version:	0.5
Release:	1cisco%{?dist}
Summary:	Puppet Openstack module

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-openstack.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define tmpname %(echo %{name} | cut -d- -f 2-)

%description
The Openstack Puppet Modules are a flexible Puppet implementation capable of configuring the core Openstack services

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/

%files
%dir %{_usr}/share/puppet/modules/%{tmpname}/
%{_usr}/share/puppet/modules/%{tmpname}/*


%defattr(-,root,root,-)
%doc README.md CHANGELOG LICENSE examples/

%clean
rm -rf %{buildroot}

%changelog
* Mon Sep 30 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.5-1cisco
- Added license file (pkilambi@cisco.com)

* Tue Jul 09 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.4-1cisco
- 

* Thu May 16 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.3-1cisco
- 

* Tue May 07 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.2-1cisco
- new package built with tito

* Tue Apr 24 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

