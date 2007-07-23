Summary:	Bandwidth tracking and limiting plugin for lighttpd
Name:		lighttpd-mod_bandwidth
Version:	0.8
Release:	0.1
License:	BSD
Source0:	http://www.asmallorange.com/downloads/mod_bandwidth-%{version}.tar.gz
# Source0-md5:	032463ee6d16335d8e969f83a3da059e
Group:		Networking/Daemons
URL:		http://www.asmallorange.com/products/opensource/mod_bandwidth.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/lighttpd
%define		_sysconfdir	/etc/lighttpd

%description
mod_bandwidth is a bandwidth tracking and limiting plugin for
lighttpd. It allows for limiting on a per-context basis and for any
arbitrary period of time or bandwidth. It is intended to be accurate
bit-for-bit for any data sent from the server, despite large amounts
of data being transferred. It also allows for users to track the
bandwidth used by their sites and get real-time feedback of how close
they are to their limits.

%prep
%setup -q -n mod_bandwidth-%{version}

%build
exit 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING INSTALL README TODO