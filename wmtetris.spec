Summary:	Tetris game for the WindowMaker dock
Summary(pl.UTF-8):	Gra Tetris dla Doku WindowMakera
Name:		wmtetris
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.fi.muni.cz/~xmichal5/wmaker/%{name}-%{version}.tar.gz
# Source0-md5:	711788e12a589e4733304a1a82c1fca2
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://www.dockapps.org/file.php/id/106
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Tetris game for the WindowMaker dock.

%description -l pl.UTF-8
Gra Tetris dla Doku WindowMakera.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C %{name} \
	OPT="%{rpmcflags}" \
	CC="%{__cc}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/wmtetris.desktop
