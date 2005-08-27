Summary:	XCMisc protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u XCMisc i pomocnicze
Name:		xorg-proto-xcmiscproto
Version:	1.1
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/xcmiscproto-%{version}.tar.bz2
# Source0-md5:	4ca773736b114e159969acac2217a347
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XCMisc protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u XCMisc i pomocnicze.

%package devel
Summary:	XCMisc protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u XCMisc i pomocnicze
Group:		X11/Development/Libraries

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
