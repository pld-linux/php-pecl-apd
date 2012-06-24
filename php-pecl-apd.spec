%define		_modname	apd
%define		_status		stable

Summary:	%{_modname} - full-featured engine-level profiler/debugger
Summary(pl):	%{_modname} - w pe�ni funkcjonalny profiler/debugger dla PHP
Name:		php-pecl-%{_modname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	470ea75cde09f7504c83441911c86f29
Patch0:		%{name}-build_fix.patch
URL:		http://pecl.php.net/package/apd/
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
APD is a full-featured profiler/debugger that is loaded as a
zend_extension. It aims to be an analog of C's gprof or Perl's
Devel::DProf.

In PECL status of this package is: %{_status}.

%description -l pl
APD to w pe�ni funkcjonalny profiler/debugger �adowany jako
rozszerzenie Zend. Ma by� odpowiednikiem gprof z C lub perlowego
Devel::DProf.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
%patch0 -p1

%build
cd %{_modname}-%{version}
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
