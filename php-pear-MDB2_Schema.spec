# TODO
# - do something with /usr/share/pear/www/mdb2_schematool
%define		_status		beta
%define		_pearname	MDB2_Schema
Summary:	%{_pearname} - XML based database schema manager
Summary(pl.UTF-8):	%{_pearname} - oparty na XML zarządca schematów baz danych
Name:		php-pear-%{_pearname}
Version:	0.8.6
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2708fcccb1d133af9f716095182b4460
URL:		http://pear.php.net/package/MDB2_Schema/
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.5.0-0.b1
Requires:	php-pear-XML_Parser >= 1.2.8
Suggests:	php-pear-XML_DTD
Suggests:	php-pear-XML_Serializer
Obsoletes:	php-pear-MDB2_Schema-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(XML/DTD.*)' pear(XML/Serializer.*)

%description
PEAR::MDB2_Schema enables users to maintain RDBMS independant schema
files in XML that can be used to create, alter and drop database
entities and insert data into a database. Reverse engineering database
schemas from existing databases is also supported. The format is
compatible with both PEAR::MDB and Metabase.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PEAR::MDB2_Schema pozwala użytkownikowi na zarządzanie niezależnymi od
RDBMS XMLowymi plikami schema, które mogą być użyte do tworzenia,
modyfikacji lub usuwania baz oraz wprowadzania danych. Możliwy jest
także reverse engineering schematów baz z już istniejących baz. Format
jest kompatybilny zarówno z PEAR::MDB jak i Metabase.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/www/mdb2_schematool

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Schema.php
%{php_pear_dir}/MDB2/Schema
%{php_pear_dir}/data/MDB2_Schema

%{_examplesdir}/%{name}-%{version}
