%define pkgname ndesk-dbus-glib-1.0

Summary:	Managed D-Bus implementation - GLib integration
Name:		ndesk-dbus-glib
Version:	0.4.1
Release:	10
License:	MIT
Group:		System/Libraries
Url:		http://www.ndesk.org/DBusSharp
Source0:	http://www.ndesk.org/archive/dbus-sharp/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(ndesk-dbus-1.0)
Requires:	glib2

%description
dbus-sharp is a C Sharp implementation of D-Bus. It's often referred to as
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
dbus-sharp is a C Sharp implementation of D-Bus. It's often referred to as
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
%{_prefix}/lib/mono/%{pkgname}
%{_prefix}/lib/mono/gac/NDesk.DBus.GLib/

%files devel
%doc examples
%{_datadir}/pkgconfig/%{pkgname}.pc

