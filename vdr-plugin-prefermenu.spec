
%define plugin	prefermenu
%define name	vdr-plugin-%plugin
%define version	0.6.6
%define rel	17

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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* TODO




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.6.6-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.6.6-15mdv2009.1
+ Revision: 359750
- rediff SetAreas bugfix
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.6.6-14mdv2009.0
+ Revision: 197965
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.6.6-13mdv2009.0
+ Revision: 197710
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.3 (P0 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.6.6-12mdv2008.1
+ Revision: 145189
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.6.6-11mdv2008.1
+ Revision: 103184
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.6.6-10mdv2008.0
+ Revision: 50033
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.6.6-9mdv2008.0
+ Revision: 42120
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.6.6-8mdv2008.0
+ Revision: 22771
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.6.6-7mdv2007.0
+ Revision: 90962
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.6.6-6mdv2007.1
+ Revision: 74072
- rebuild for new vdr
- Import vdr-plugin-prefermenu

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.6.6-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.6.6-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.6.6-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.6.6-2mdv2007.0
- rebuild for new vdr

* Tue Jul 18 2006 Anssi Hannula <anssi@mandriva.org> 0.6.6-1mdv2007.0
- initial Mandriva release

