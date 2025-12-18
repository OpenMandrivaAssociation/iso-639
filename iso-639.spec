%global srcname iso-639
%global common_summary  ISO 639 library for Python
%global common_description %{summary}.\
ISO 639-1, ISO 639-2, ISO 639-3, ISO 639-5 are supported.

Name:           python-%{srcname}
Version:        0.4.5
Release:        6
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        AGPLv3
URL:            https://github.com/noumar/iso639/
Source0:        https://github.com/noumar/iso639/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
BuildArch:      noarch

%{?python_provide:%python_provide python3-%{srcname}}
Provides:   python3-%{srcname}

%description
%{common_description}

%prep
%autosetup -n iso639-%{version}

%build
%py_build

%install
%py_install

%files
#doc CHANGES.rst README.rst
#license LICENSE.txt
%{python_sitelib}/*
