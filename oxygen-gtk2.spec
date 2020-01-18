
Name:    oxygen-gtk2
Summary: Oxygen GTK+2 theme
Version: 1.3.4
Release: 3%{?dist}

License: LGPLv2+
Group:   User Interface/Desktops
URL:     https://projects.kde.org/projects/playground/artwork/oxygen-gtk
Source0: http://download.kde.org/stable/oxygen-gtk2/%{version}/src/%{name}-%{version}.tar.bz2

## upstream patches

BuildRequires: cmake
BuildRequires: gtk2-devel

Conflicts: oxygen-gtk < 1.2.0-2

%description
Oxygen-Gtk is a port of the default KDE widget theme (Oxygen), to gtk.

It's primary goal is to ensure visual consistency between gtk-based and
qt-based applications running under KDE. A secondary objective is to also
have a stand-alone nice looking gtk theme that would behave well on other
Desktop Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this
attempt does not depend on Qt (via some Qt to Gtk conversion engine), 
nor does render the widget appearance via hard-coded pixmaps, which 
otherwise breaks every time some setting is changed in KDE.


%prep
%setup -q



%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} -DOXYGEN_FORCE_KDE_ICONS_AND_FONTS=0  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/oxygen-gtk-demo
%{_libdir}/gtk-2.0/*/engines/liboxygen-gtk.so
%{_datadir}/themes/oxygen-gtk/


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.3.4-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3.4-2
- Mass rebuild 2013-12-27

* Fri May 31 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.4-1
- oxygen-gtk2-1.3.4

* Mon Apr 22 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.3-1
- oxygen-gtk2-1.3.3

* Wed Feb 13 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.2.1-1
- oxygen-gtk2-1.3.2.1

* Fri Feb 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-2
- Upgrade to oxygen-gtk2 1.3.2 is buggy (kde#314545)

* Wed Jan 30 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.2-1
- oxygen-gtk2-1.3.2

* Fri Oct  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.1-1
- oxygen-gtk2-1.3.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.0-1
- oxygen-gtk2-1.3.0

* Fri Jun 15 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.5-1
- oxygen-gtk2-1.2.5

* Mon May 14 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.4-1
- oxygen-gtk2-1.2.4

* Sat Apr 14 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.3-1
- oxygen-gtk2-1.2.3

* Sat Mar 24 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.2.1-1
- oxygen-gtk2-1.2.2-1
- drop badwindow patch

* Tue Mar 20 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.2-2
- fix crash in claws-mail (#804790, kde#295875)

* Mon Mar 12 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.2-1
- oxygen-gtk2-1.2.2
- drop BR: dbus-glib-devel

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.1-1
- oxygen-gtk2-1.2.1

* Mon Jan 23 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-3
- drop Obsoletes: oxygen-gtk < 1.2.0-2

* Tue Jan 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-2
- renamed to oxygen-gtk2

* Tue Jan 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-1
- oxygen-gtk2-1.2.0
- License: LGPLv2+

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Fri Nov 18 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.5-1
- 1.1.5

* Fri Oct 28 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.4-3
- disable forcing KDE icons and fonts

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for glibc bug#747377

* Sun Oct 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.4-1
- 1.1.4

* Mon Oct  3 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-3
- fix mozilla applications detection kde#283251

* Fri Sep 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-2
- BR: dbus-glib-devel

* Fri Sep 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Sat Aug 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1.2-1
- 1.1.2

* Fri Jul 15 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Tue Jun 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-1
- 1.1.0

* Fri May 20 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- 1.0.5

* Tue Apr 12 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- 1.0.4

* Mon Mar 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-1
- 1.0.3

* Fri Feb 11 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-1
- 1.0.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-1
- oxygen-gtk-1.0.1

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-2
- drop extraneous BR: cairo-devel

* Sun Dec 12 2010 Rex Dieter <rdieter@fedoraproject.org> -  1.0.0-1
- first try




