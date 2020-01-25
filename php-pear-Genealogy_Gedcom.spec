%define		_class		Genealogy
%define		_subclass	Gedcom
%define		_status		stable
%define		_pearname	Genealogy_Gedcom
Summary:	%{_pearname} - Gedcom parser
Summary(pl.UTF-8):	%{_pearname} - parser Gedcom
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	113e819410248f30f0792b0d60ad8bb4
Patch0:	peardeps.patch
URL:		http://pear.php.net/package/Genealogy_Gedcom/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-25
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package was written to parse .ged (gedcom) file.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Narzędzie do przetwarzania plików .ged (gedcom).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1
mv docs/%{_pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Genealogy/Gedcom
%{php_pear_dir}/Genealogy/Gedcom.php

%{_examplesdir}/%{name}-%{version}
