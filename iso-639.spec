%global srcname iso-639
%global common_summary  ISO 639 library for Python
%global common_description %{summary}.\
ISO 639-1, ISO 639-2, ISO 639-3, ISO 639-5 are supported.

Name:           python-%{srcname}
Version:        0.4.5
Release:        4
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        AGPLv3
URL:            https://github.com/noumar/iso639/
Source0:        https://github.com/noumar/iso639/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python2dist(setuptools)
BuildArch:      noarch

%{?python_provide:%python_provide python3-%{srcname}}
Provides:   python3-%{srcname}

%description
%{common_description}

%package -n python2-%{srcname}
Summary:        %{common_summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_description}

%prep
%autosetup -n iso639-%{version}

%build
%py2_build
%py_build

%install
%py2_install
%py_install

%files -n python2-%{srcname}
#doc CHANGES.rst README.rst
#license LICENSE.txt
%{python2_sitelib}/*

%files
#doc CHANGES.rst README.rst
#license LICENSE.txt
%{python_sitelib}/*
