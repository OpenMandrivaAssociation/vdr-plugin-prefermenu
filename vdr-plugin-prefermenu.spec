
%define plugin	prefermenu
%define name	vdr-plugin-%plugin
%define version	0.6.6
%define rel	16

Summary:	VDR plugin: Preferred channels menu
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://famillejacques.free.fr/vdr/prefermenu/
Source:		http://famillejacques.free.fr/vdr/prefermenu/vdr-%plugin-%version.tar.bz2
Patch0:		90_prefermenu-0.6.6-1.5.3+SetAreas-bugfix.dpatch
Patch1:		prefermenu-0.6.6-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
PreferMenu is a plugin that implements a preferred channel menu.
It makes it easy to recall (switch to) your favorite channels.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

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


