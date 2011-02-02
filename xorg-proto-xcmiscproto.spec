Summary:	XCMisc extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XCMisc
Name:		xorg-proto-xcmiscproto
Version:	1.2.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/proto/xcmiscproto-%{version}.tar.bz2
# Source0-md5:	cd7372cd827bfd7ca7e9238f2ce274b1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
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
%doc COPYING ChangeLog README specs/*.{html,css}
%{_includedir}/X11/extensions/xcmisc*.h
%{_pkgconfigdir}/xcmiscproto.pc
