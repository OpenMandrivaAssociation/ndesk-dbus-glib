%define name ndesk-dbus-glib
%define version 0.3
%define release %mkrel 2
%define oname dbus-sharp-glib
%define pkgname ndesk-dbus-glib-1.0

Summary: Managed D-Bus implementation - GLib integration
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ndesk.org/archive/dbus-sharp/%{oname}-%{version}.tar.gz
Source1: include.mk
Patch: dbus-sharp-glib-0.3-pkgconfig.patch
License: MIT
Group: System/Libraries
Url: http://www.ndesk.org/DBusSharp
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: ndesk-dbus
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

%prep
%setup -q -n %oname-%version
%patch -p1
cp %SOURCE1 .
cp %_prefix/lib/mono/ndesk-dbus-1.0/*.dll glib

%build
make DBUS_SHARP_PREFIX=`pwd`
make DBUS_SHARP_PREFIX=`pwd` -C examples


%install
rm -rf $RPM_BUILD_ROOT
cd glib
%makeinstall DBUS_SHARP_PREFIX=..
cd ..
install -m 644 -D %pkgname.pc.in %buildroot%_datadir/pkgconfig/%pkgname.pc
perl -pi -e "s^\@prefix\@^%_prefix^" %buildroot%_datadir/pkgconfig/%pkgname.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING examples
%_prefix/lib/mono/%pkgname
%_prefix/lib/mono/gac/NDesk.DBus.GLib/
%_datadir/pkgconfig/%pkgname.pc
