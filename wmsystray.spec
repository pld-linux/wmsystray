Summary:	Window Maker dock app that provides system tray
Summary(pl):	Dock App Window Makera udostêpniaj±cy zasobnik systemowy
Name:		wmsystray
Version:	0.1.1
Release:	0.1
License:	GPL
Group:		X11/Window Manager/Tools
Source0:	http://kai.vm.bytemark.co.uk/~arashi/wmsystray/release/%{name}-%{version}.tar.bz2
# Source0-md5:	398cbc1139d53dbf65c00010bf2297fb
URL:		http://kai.vm.bytemark.co.uk/~arashi/wmsystray/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmsystray provides a system tray compatible with freedesktop.org's
System Tray Protocol specification. Basically, it serves as a system
tray that allows other programs to show icons in it. For example, if
you enable GAIM's System Tray Icon plugin, wmsystray will display
GAIM's systray icon. Its intended use is as a Window Maker dock app,
though it will run in other window managers as well.

%description -l pl
wmsystray dostarcza zasobnik systemowy kompatybilny ze specyfikacj±
Protoko³u Zasobnika Systemowego (System Tray Protocol) ze strony
freesktop.org. Zasadniczo udostêpnia on zasobnik systemowy pozwalaj±cy
innym programom na pokazywanie na nim swoich ikon. Dla przyk³adu,
je¶li uaktywnisz wtyczkê Zasobnika Systemowego GAIMa, wmsystray
wyswietli ikonê GAIMa. wmsystray zosta³ stworzony jako aplikacja
dokuj±ca Window Makera, jednak mo¿e byæ uruchamiana w innych
zarz±dcach okien.

%prep
%setup -q 

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/X11R6/include -I../xembed -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install wmsystray/wmsystray $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING README
%attr(755,root,root) %{_bindir}/*
