Summary:	A Graphical FTP client
Summary(pl.UTF-8):	Graficzny klient FTP
Name:		deadftp
Version:	0.1.3
Release:	4
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/deadftp/%{name}-%{version}.tar.bz2
# Source0-md5:	b5bd88ef57c7d7a653621ef1c835f790
Patch0:		%{name}-desktop.patch
URL:		http://deadftp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	libglade-gnome-devel >= 0.11
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeadFTP is an FTP client for GNOME. DeadFTP provides all basic
functionality of an FTP client as well as a transfer queue and a
hostmanager.

%description -l pl.UTF-8
DeadFTP jest klientem FTP dla środowiska GNOME. DeadFTP zapewnia
podstawową funkcjonalność klienta FTP, jak również kolejkę transferów
i hostmanagera.

%prep
%setup -q
%patch -P0 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/deadftp
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
