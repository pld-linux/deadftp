%define nam     deadftp
%define ver     0.0.9
%define rel     1

%define prefix          /usr
%define sysconfdir      /etc

Summary:	A Graphical FTP client
Name:		%nam
Version:	%ver
Release:	%rel
Copyright:	GPL
Group:		Applications/Internet
Source:		http://download.sourceforge.net/deadftp/%{nam}-%{ver}.tar.gz
URL:		http://deadftp.sourceforge.net/ 
BuildRoot: 	/var/tmp/%{name}-buildroot
Docdir:		%{prefix}/doc
Packager:	Brandon Lees <brandon2@users.sourceforge.net>

Requires:       gnome-libs >= 1.2.0
Requires:       libglade >= 0.11
Requires:	libxml >= 1.8.9

%description
DeadFTP is a graphical FTP client for GNOME.  

%changelog

* Sat Sep 16 2000  Brandon <brandon2@users.sourceforge.net>

- Released deadftp-0.0.9

* Wed Aug 30 2000  Brandon Lees <brandon2@users.sourceforge.net>

- Released deadftp-0.0.8

* Wed Aug 23 2000  Brandon Lees <brandon2@users.sourceforge.net>

- Added changelog section to spec file.  

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure   \
      --prefix=%{prefix} --sysconfdir=%{sysconfdir}

make

%install
make install-strip \
	prefix=%{prefix} \
	sysconfdir=%{sysconfdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README TODO

%{prefix}/bin/*
%{prefix}/share/*
