%define		_modname	apd
%define		_status		stable
Summary:	%{_modname} -
Summary(pl):	%{_modname} -
Name:		php-pecl-%{_modname}
Version:	0.4p2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	7b13b405033e693e67ac8b9ff5ae93c2
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description

This extension has in PEAR status: %{_status}.

%description -l pl

To rozszerzenie ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
chmod 644 build/*.{awk,mk}
chmod 755 build/{shtool,fastgen.sh}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/README
%attr(755,root,root) %{extensionsdir}/%{_modname}.so