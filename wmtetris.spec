Summary:	Tetris game for the WindowMaker dock
Summary(pl):	Gra Tetris dla Doku WindowMakera
Name:		wmtetris
Version:	0.1
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://people.cornell.edu/pages/srs25/tumbolia/wmtetris/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://people.cornell.edu/pages/srs25/tumbolia/wmtetris.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Tetris game for the WindowMaker dock.

%description -l pl
Gra Tetris dla Doku WindowMakera.

%prep
%setup -q
%patch -p0

%build
%{__make} -C %{name} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
#%{_applnkdir}/DockApplets/wmtetris.desktop
