%define name ndesk-dbus-glib
%define version 0.4.1
%define release %mkrel 6
%define pkgname ndesk-dbus-glib-1.0

Summary: Managed D-Bus implementation - GLib integration
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ndesk.org/archive/dbus-sharp/%{name}-%{version}.tar.gz
License: MIT
Group: System/Libraries
Url: http://www.ndesk.org/DBusSharp
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: ndesk-dbus-devel
BuildRequires: gtk-sharp2
Requires: glib2
BuildArch: noarch
%define _requires_exceptions lib.*glib2.0_0

%description
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%prep
%setup -q -n %name-%version

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
%_prefix/lib/mono/%pkgname
%_prefix/lib/mono/gac/NDesk.DBus.GLib/

%files devel
%defattr(-,root,root)
%doc examples
%_datadir/pkgconfig/%pkgname.pc
