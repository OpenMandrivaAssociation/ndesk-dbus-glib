%define pkgname ndesk-dbus-glib-1.0

Summary:	Managed D-Bus implementation - GLib integration
Name:		ndesk-dbus-glib
Version:	0.4.1
Release:	9
Source0:	http://www.ndesk.org/archive/dbus-sharp/%{name}-%{version}.tar.gz
License:	MIT
Group:		System/Libraries
Url:		http://www.ndesk.org/DBusSharp
BuildRequires:	mono-devel
BuildRequires:	ndesk-dbus-devel
BuildRequires:	gtk-sharp2
Requires:	glib2
BuildArch: noarch

%description
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc README COPYING
%{_prefix}/lib/mono/%pkgname
%{_prefix}/lib/mono/gac/NDesk.DBus.GLib/

%files devel
%doc examples
%{_datadir}/pkgconfig/%pkgname.pc


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-7mdv2011.0
+ Revision: 666603
- mass rebuild

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.4.1-6mdv2011.0
+ Revision: 567940
- split out devel package
- update build deps

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-5mdv2010.1
+ Revision: 523421
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.1-4mdv2010.0
+ Revision: 426248
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.4.1-3mdv2009.1
+ Revision: 351631
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-2mdv2009.0
+ Revision: 223338
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 21 2007 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 101057
- new version
- fix build
- drop patch and source 1
- filter out new automatic deps from mono-find-requires
- rebuild

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2008.0
+ Revision: 59478
- fix buildrequires
- fix pkgconfig path
- Import ndesk-dbus-glib



* Mon Aug  6 2007 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2008.0
- initial package
