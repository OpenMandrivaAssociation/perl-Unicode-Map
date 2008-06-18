%define module	Unicode-Map
%define name	perl-%{module}
%define version	0.112
%define release	%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Maps charsets from and to utf16 unicode
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Unicode/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Unicode
%{perl_vendorarch}/auto/Unicode
%{_mandir}/*/*
%{_bindir}/*


