Summary:	Window Maker dock app that provides system tray.
Summary(pl):	Dock App Window Makera udostêpniaj±cy zasobnik systemowy. 
Name:		wmsystray
Version:	0.1
Release:	0.1
License:	GPL	
Group:		X11/Window Manager/Tools
Source0:	http://kai.vm.bytemark.co.uk/~arashi/wmsystray/release/%{name}-%{version}.tar.gz
# Source0-md5:	6c251428d1d4ab563fd8d38ac7afb43d
URL:		http://kai.vm.bytemark.co.uk/~arashi/wmsystray/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmsystray provides a system tray compatible with freedesktop.org's
System Tray Protocol specification. Basically, it serves as a system
tray that allows other programs to show icons in it. For example, if you
enable GAIM's System Tray Icon plugin, wmsystray will display GAIM's
systray icon. Its intended use is as a Window Maker dock app, though it
will run in other window managers as well.

#%description -l pl

%prep
%setup -q 

%build
%{__make}

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
