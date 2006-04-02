%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Schema
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML based database schema manager
Summary(pl):	%{_pearname} - oparty na XML zarz±dca schematów baz danych
Name:		php-pear-%{_pearname}
Version:	0.4.3
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6a5e3b7dd70c3a4845cbdbc8e1a1db06
URL:		http://pear.php.net/package/MDB2_Schema/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.0.0-0.RC1
Requires:	php-pear-PEAR-core >= 1:1.0b1
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(XML/DTD.*)'

%description
PEAR::MDB2_Schema enables users to maintain RDBMS independant schema
files in XML that can be used to create, alter and drop database
entities and insert data into a database. Reverse engineering database
schemas from existing databases is also supported. The format is
compatible with both PEAR::MDB and Metabase.

In PEAR status of this package is: %{_status}.

%description -l pl
PEAR::MDB2_Schema pozwala u¿ytkownikowi na zarz±dzanie niezale¿nymi od
RDBMS XMLowymi plikami schema, które mog± byæ u¿yte do tworzenia,
modyfikacji lub usuwania baz oraz wprowadzania danych. Mo¿liwy jest
tak¿e reverse engineering schematów baz z ju¿ istniej±cych baz. Format
jest kompatybilny zarówno z PEAR::MDB jak i Metabase.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
