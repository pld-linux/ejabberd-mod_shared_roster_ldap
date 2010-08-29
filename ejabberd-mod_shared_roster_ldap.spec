%define		pname mod_shared_roster_ldap

Summary:	LDAP-based shared roster module for ejabberd server
Name:		ejabberd-%{pname}
Version:	0.5.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	https://alioth.debian.org/frs/download.php/3343/%{pname}-%{version}.tgz
# Source0-md5:	df03ff5c61067fd82eb18c219e05287d
URL:		http://www.ejabberd.im/mod_shared_roster_ldap
BuildRequires:	ejabberd
BuildRequires:	erlang >= R9C
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	ejabberd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAP-based shared roster module for ejabberd server.

%prep
%setup -qc -n %{name}

%build
cd src
erlc -I%{_libdir}/ejabberd/include mod_shared_roster_ldap_helpers.erl
erlc -I%{_libdir}/ejabberd/include mod_shared_roster_ldap.erl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

install src/*.beam $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/ejabberd/ebin/*.beam
%doc doc/*
