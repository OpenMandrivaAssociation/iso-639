%global srcname iso-639
%global common_summary  ISO 639 library for Python
%global common_description %{summary}.\
ISO 639-1, ISO 639-2, ISO 639-3, ISO 639-5 are supported.

Name:           python-%{srcname}
Version:        0.4.5
Release:        1
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        AGPLv3
URL:            https://github.com/noumar/iso639/
Source0:        https://github.com/noumar/iso639/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3egg(setuptools)
BuildRequires:  pythonegg(setuptools)
BuildArch:      noarch

%description
%{common_description}


%package -n python2-%{srcname}
Summary:        %{common_summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_description}


%package -n python3-%{srcname}
Summary:        %{common_summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}


%prep
%autosetup -n iso-639-%{version}


%build
%py2_build
%py_build


%install
%py2_install
%py_install


%check
# Tests mostly check compatibility with the pycountry library, not available in
# Fedora
# export PYTHONPATH=$PWD
# %%{__python2} tests/tests.py
# %%{__python3} tests/tests.py


%files -n python2-%{srcname}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python2_sitelib}/*


%files -n python3-%{srcname}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*
