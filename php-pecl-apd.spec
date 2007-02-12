%define		_modname	apd
%define		_status		stable
Summary:	%{_modname} - full-featured engine-level profiler/debugger
Summary(pl.UTF-8):   %{_modname} - w pełni funkcjonalny profiler/debugger dla PHP
Name:		php-pecl-%{_modname}
Version:	1.0.1
Release:	7
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	470ea75cde09f7504c83441911c86f29
Patch0:		%{name}-cvs.patch
URL:		http://pecl.php.net/package/apd/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_zend_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APD is a full-featured profiler/debugger that is loaded as a
zend_extension. It aims to be an analog of C's gprof or Perl's
Devel::DProf.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
APD to w pełni funkcjonalny profiler/debugger ładowany jako
rozszerzenie Zend. Ma być odpowiednikiem gprof z C lub perlowego
Devel::DProf.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
cd %{_modname}-%{version}
%patch0 -p1

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
zend_extension%{?zend_zts:_ts}=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
