Summary:	Personal search and metasearch for the Free Desktop
Name:		pinot
Version:	0.95
Release:	%mkrel 1
Group:		File tools
License:	GPLv2+
URL:		http://pinot.berlios.de
Source0:	http://download.berlios.de/pinot/%{name}-%{version}.tar.gz
Patch0:		pinot-0.83-language-path.patch
BuildRequires:	libsqlite3-devel
BuildRequires:	libxapian-devel >= 1.0.5
BuildRequires:	libtextcat-devel
BuildRequires:	libtaglib-devel
BuildRequires:	libcurl-devel
BuildRequires:	libgmime-devel
BuildRequires:	libboost-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libxml++2.6-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:	shared-mime-info
BuildRequires:	openssl-devel
BuildRequires:	libexif-devel
BuildRequires:	libarchive-devel
BuildRequires:	libgmime2.2-devel
Requires:	shared-mime-info
Requires:	unzip
Requires:	antiword
Requires:	unrtf
Requires:	poppler
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1

%build
%configure2_5x \
	--with-http=curl \
	--with-ssl=%{_libdir} \
	--disable-soap \
	--disable-xesam-glib \
	--enable-dbus \
	--enable-mempool \
	--enable-libarchive \
	--enable-gio

%make

%install
rm -rf %{buildroot}

%makeinstall_std

desktop-file-install \
	--remove-category="Core" \
	--remove-category="Network" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
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
%defattr(-,root,root)
%{_libdir}/deskbar-applet/*
