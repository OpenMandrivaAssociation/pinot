Summary:	Personal search and metasearch for the Free Desktop
Name:		pinot
Version:	1.05
Release:	2
Group:		File tools
License:	GPLv2+
URL:		https://code.google.com/p/pinot-search/
Source0:	http://pinot-search.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	libxapian-devel >= 1.0.5
BuildRequires:	libtextcat-devel
BuildRequires:	libtaglib-devel
BuildRequires:	libcurl-devel
BuildRequires:	pkgconfig(gmime-2.6)
BuildRequires:	libboost-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:	shared-mime-info
BuildRequires:	openssl-devel
BuildRequires:	libexif-devel
BuildRequires:	libarchive-devel
#BuildRequires:	libgmime2.2-devel
BuildRequires:	pkgconfig(exiv2)
Requires:	shared-mime-info
Requires:	unzip
Requires:	antiword
Requires:	unrtf
Requires:	poppler
Requires(post,postun):	desktop-file-utils

%description
Pinot is a D-Bus service that crawls, indexes your documents and monitors them
for changes, as well as a GTK-based user interface that enables to query
the index built by the service and your favourite Web engines, and display and
analyze the results.

%package deskbar
Summary:	Pinot plugin for deskbar applet
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}-%{release}
Requires:	deskbar-applet

%description deskbar
The included plugin enables Deskbar to search documents indexed by Pinot.

%prep
%setup -q

%build
%configure2_5x \
	--with-http=curl \
	--with-ssl=%{_libdir} \
	--enable-dbus \
	--enable-mempool \
	--enable-libarchive \
	--enable-gio

%make

%install
%makeinstall_std

desktop-file-install \
	--remove-category="Core" \
	--remove-category="Network" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %{_sysconfdir}/%{name}/
%dir %{_datadir}/%{name}
%{_bindir}/%{name}*
%{_datadir}/%{name}/*
%{_libdir}/pinot/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/de.berlios.Pinot.service
%{_sysconfdir}/xdg/autostart/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*

%files deskbar
%{_libdir}/deskbar-applet/*
