Summary:	Personal search and metasearch for the Free Desktop
Name:		pinot
Version:	0.80
Release:	%mkrel 1
Group:		Text tools      
License:	GPLv2+
URL:		http://pinot.berlios.de
Source0:	http://download2.berlios.de/pinot/%{name}-%{version}.tar.bz2
BuildRequires:	libsqlite3-devel
BuildRequires:	libxapian-devel
BuildRequires:	libtextcat-devel
BuildRequires:	taglib-devel
BuildRequires:	curl-devel
BuildRequires:	gmime-devel
BuildRequires:	boost-devel
BuildRequires:	libgtkmm2.4-devel
BuildRequires:	libxml++-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:	shared-mime-info
Requires:	shared-mime-info
Requires:	unzip
Requires:	antiword
Requires:	unrtf
Requires:	poppler-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std


%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config(noreplace) %{_sysconfdir}/%{name}/
%dir %{_datadir}/%{name}
%{_bindir}/%{name}*
%{_datadir}/%{name}/*
#%{_libdir}/pinot/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/de.berlios.Pinot.service
%{_sysconfdir}/xdg/autostart/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*

%files deskbar
%defattr(-,root,root,-)
%{_libdir}/deskbar-applet/handlers/%{name}*
