Summary:	Bandwidth tracking and limiting plugin for lighttpd
Summary(pl.UTF-8):	Wtyczka dla lighttpd śledząca i ograniczająca pasmo
Name:		lighttpd-mod_bandwidth
Version:	0.8
Release:	0.1
License:	BSD
Source0:	http://www.asmallorange.com/downloads/mod_bandwidth-%{version}.tar.gz
# Source0-md5:	032463ee6d16335d8e969f83a3da059e
Group:		Networking/Daemons/HTTP
URL:		http://www.asmallorange.com/products/opensource/mod_bandwidth.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/lighttpd
%define		_sysconfdir	/etc/lighttpd

%description
mod_bandwidth is a bandwidth tracking and limiting plugin for
lighttpd. It allows limiting on a per-context basis and for any
arbitrary period of time or bandwidth. It is intended to be accurate
bit-for-bit for any data sent from the server, despite large amounts
of data being transferred. It also allows users to track the
bandwidth used by their sites and get real-time feedback of how close
they are to their limits.

%description -l pl.UTF-8
mod_bandwidth to wtyczka dla lighttpd śledząca i ograniczająca pasmo.
Pozwala ograniczać w zależności od kontekstu i dla dowolnego okresu
czasu lub pasma. Ma być dokładna co do bitu dla wszystkich danych
wysyłanych z serwera, niezależnie od ilości przesłanych danych.
Pozwala także użytkownikom śledzić pasmo wykorzystywane przez ich
serwisy i uzyskiwać w czasie rzeczywistym informacje, na ile zbliżają
się do swoich limitów.

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
