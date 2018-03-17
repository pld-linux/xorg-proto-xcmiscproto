# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	XCMisc extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XCMisc
Name:		xorg-proto-xcmiscproto
Version:	1.2.2
Release:	2.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/archive/individual/proto/xcmiscproto-%{version}.tar.bz2
# Source0-md5:	5f4847c78e41b801982c8a5e06365b24
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCMisc extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia XCMisc.

%package devel
Summary:	XCMisc extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XCMisc
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel

%description devel
XCMisc extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia XCMisc.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/xc-misc.html
%{_includedir}/X11/extensions/xcmisc*.h
%{_pkgconfigdir}/xcmiscproto.pc
