Summary:	Tetris game for the WindowMaker dock
Summary(pl):	Gra Tetris dla Doku WindowMakera
Name:		wmtetris
Version: 	0.1
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
URL:		http://people.cornell.edu/pages/srs25/tumbolia/wmtetris.html
Source0:	%{name}-%{version}.tar.gz
Source1:	wmtetris.desktop
Patch:		wmtetris-makefile.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
Tetris game for the WindowMaker dock.

%description -l pl
Gra Tetris dla Doku WindowMakera.

%prep
%setup -q
%patch -p0

%build
make -C %{name} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/X11/applnk/Application}
install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Application

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/%{name}
/etc/X11/applnk/Application/wmtetris.desktop

%changelog
* Tue May 25 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.1-1]
- initial RPM release.
