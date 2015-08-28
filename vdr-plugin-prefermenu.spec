%define plugin	prefermenu

Summary:	VDR plugin: Preferred channels menu
Name:		vdr-plugin-%plugin
Version:	0.6.6
Release:	19
Group:		Video
License:	GPL
URL:		http://famillejacques.free.fr/vdr/prefermenu/
Source:		http://famillejacques.free.fr/vdr/prefermenu/vdr-%plugin-%{version}.tar.bz2
Patch0:		90_prefermenu-0.6.6-1.5.3+SetAreas-bugfix.dpatch
Patch1:		prefermenu-0.6.6-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
PreferMenu is a plugin that implements a preferred channel menu.
It makes it easy to recall (switch to) your favorite channels.

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README* TODO




