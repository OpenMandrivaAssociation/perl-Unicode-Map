%define module Unicode-Map

Name:		perl-%{module}
Version:	0.112
Release:	17
Summary:	Maps charsets from and to utf16 unicode
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel

%description
This module converts strings from and to 2-byte Unicode UCS2 format. All
mappings happen via 2 byte UTF16 encodings, not via 1 byte UTF8 encoding. To
transform these use Unicode::String.

For historical reasons this module coexists with Unicode::Map8. Please use
Unicode::Map8 unless you need to care for two byte character sets, e.g. chinese
GB2312. Anyway, if you stick to the basic functionality (see documentation) you
can use both modules equivalently.


Practically this module will disappear from earth sooner or later as Unicode
mapping support needs somehow to get into perl's core. If you like to work on
this field please don't hesitate contacting Gisle Aas!

This module can't deal directly with utf8. Use Unicode::String to convert utf8
to utf16 and vice versa.

Character mapping is according to the data of binary mapfiles in Unicode::Map
hierarchy. Binary mapfiles can also be created with this module, enabling you
to install own specific character sets. Refer to mkmapfile or file REGISTRY in
the Unicode::Map hierarchy

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorarch}/Unicode
%{perl_vendorarch}/auto/Unicode
%{_mandir}/*/*
%{_bindir}/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.112-14mdv2012.0
+ Revision: 765796
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.112-13
+ Revision: 764301
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.112-12
+ Revision: 667406
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.112-11mdv2011.0
+ Revision: 564589
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.112-10mdv2011.0
+ Revision: 555206
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.112-9mdv2010.1
+ Revision: 426599
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.112-8mdv2009.0
+ Revision: 224583
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.112-7mdv2008.1
+ Revision: 151403
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.112-6mdv2007.0
+ Revision: 107903
- rebuild
- Import perl-Unicode-Map

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.112-5mdk
- spec cleanup
- %%mkrel
- better url

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.112-4mdk 
- rebuild for new perl

* Sat Jul 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.112-3mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.112-2mdk
- fixed dir ownership (distlint)

