%define _builddir $PWD

Name: rscheck
Version: %(awk -F\' '/^__version__/ {print $2}' rscheck)
Release: 1%{?dist}
Summary: Real Server health Check
License: MIT
URL: https://github.com/AlekseyChudov/rscheck

BuildArch: noarch

Requires: python
Requires: python-dns
Requires: python2-pyroute2
Requires: PyYAML
Requires: systemd-python

%systemd_requires

%description
RSCheck is a simple daemon for checking a Real Server health before adding it to
a Load Balancing cluster.

%install
install -d %{buildroot}%{_sysconfdir}/rscheck
install -D rscheck %{buildroot}%{_libexecdir}/rscheck
install -D rscheck@.service %{buildroot}%{_unitdir}/rscheck@.service

%post
%systemd_post rscheck@*

%preun
%systemd_preun rscheck@*

%postun
%systemd_postun_with_restart rscheck@*

%files
%defattr(0644,root,root,0755)
%doc LICENSE README.md rscheck.conf rscheck.png
%attr(0750,root,root) %dir %{_sysconfdir}/rscheck
%attr(0755,root,root) %{_libexecdir}/rscheck
%{_unitdir}/rscheck@.service

%changelog
* Mon Jun 26 2017 Aleksey Chudov <aleksey.chudov@gmail.com>
- Initial spec file for CentOS 7
