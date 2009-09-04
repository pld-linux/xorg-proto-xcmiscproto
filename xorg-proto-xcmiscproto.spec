Summary:	XCMisc protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XCMisc i pomocnicze
Name:		xorg-proto-xcmiscproto
Version:	1.2.0
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/proto/xcmiscproto-%{version}.tar.bz2
# Source0-md5:	7b83e4a7e9f4edc9c6cfb0500f4a7196
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCMisc protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu XCMisc i pomocnicze.

%package devel
Summary:	XCMisc protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu XCMisc i pomocnicze
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel

%description devel
XCMisc protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu XCMisc i pomocnicze.

%prep
%setup -q -n xcmiscproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xcmiscproto.pc
