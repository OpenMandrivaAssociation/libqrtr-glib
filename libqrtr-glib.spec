Summary:	Libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm IPC Router) bus.
Name:		libqrtr-glib
Version:	1.2.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/libqrtr-glib
Source0:	https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib/-/archive/%{version}/libqrtr-glib-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.32
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	gtk-doc

%description
Libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm IPC Router) bus.
  
%prep
%autosetup -p1

%build
%meson \
        -Dgtk_doc=true

%meson_build

%install
%meson_install

%files
