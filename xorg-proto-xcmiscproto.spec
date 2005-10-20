Summary:	XCMisc protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u XCMisc i pomocnicze
Name:		xorg-proto-xcmiscproto
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/xcmiscproto-%{version}.tar.bz2
# Source0-md5:	e3e6ee6862982f2b2d7a0fc7f483869e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCMisc protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u XCMisc i pomocnicze.

%package devel
Summary:	XCMisc protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u XCMisc i pomocnicze
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel

%description devel
XCMisc protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u XCMisc i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xcmiscproto.pc
