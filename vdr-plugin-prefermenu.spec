
%define plugin	prefermenu
%define name	vdr-plugin-%plugin
%define version	0.6.6
%define rel	9

Summary:	VDR plugin: Preferred channels menu
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://famillejacques.free.fr/vdr/prefermenu/
Source:		http://famillejacques.free.fr/vdr/prefermenu/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
PreferMenu is a plugin that implements a preferred channel menu.
It makes it easy to recall (switch to) your favorite channels.

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* TODO


