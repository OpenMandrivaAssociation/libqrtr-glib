%define major 0
%define libname %mklibname qrtr-glib-glib
%define girname %mklibname qrtr-glib-gir
%define devname %mklibname qrtr-glib -d

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
  
%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
Libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm IPC Router) bus.
    
%package -n %{girname}
Summary:        Introspection file for %{name}

%description -n %{girname}
Libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm IPC Router) bus.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
Libqrtr-glib is a glib-based library to use and manage the QRTR (Qualcomm IPC Router) bus.
  
%prep
%autosetup -p1

%build
%meson \
        -Dgtk_doc=true

%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libqrtr-glib.so.%{major}*
    
%files -n %{girname}
%{_libdir}/girepository-1.0/Qrtr-1.0.typelib
%{_datadir}/gir-1.0/Qrtr-1.0.gir

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/
%{_includedir}//libqrtr-glib/
%{_libdir}/libqrtr-glib.so
%{_libdir}/pkgconfig/qrtr-glib.pc
