%define		php_name	php%{?php_suffix}
%define		modname	apd
%define		status	stable
Summary:	%{modname} - full-featured engine-level profiler/debugger
Summary(pl.UTF-8):	%{modname} - w pełni funkcjonalny profiler/debugger dla PHP
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.1
Release:	9
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	470ea75cde09f7504c83441911c86f29
Patch0:		php-pecl-%{modname}-cvs.patch
URL:		http://pecl.php.net/package/apd/
BuildRequires:	%{php_name}-devel >= 4:5.2.17-8
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_zend_extension}
Provides:	php(%{modname}) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APD is a full-featured profiler/debugger that is loaded as a
zend_extension. It aims to be an analog of C's gprof or Perl's
Devel::DProf.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
APD to w pełni funkcjonalny profiler/debugger ładowany jako
rozszerzenie Zend. Ma być odpowiednikiem gprof z C lub perlowego
Devel::DProf.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .
%patch0 -p1

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
zend_extension=%{modname}.so
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
%doc README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
