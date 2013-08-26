%define upstream_name    Math-MatrixReal
%define upstream_version 2.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Manipulate NxN matrices
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/Math-MatrixReal-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
*Semi-Rings*
    A Semi-Ring (S, +, ., 0, 1) is characterized by the following
    properties:

    * 1)

      a) '(S, +, 0) is a Semi-Group with neutral element 0'

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.80.0-1mdv2011.0
+ Revision: 654103
- update to new version 2.08

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 2.50.0-1mdv2011.0
+ Revision: 624855
- import perl-Math-MatrixReal


