# Adapted from Fedora's packaging (2014-02-17)
# http://pkgs.fedoraproject.org/cgit/python-markupsafe.git/tree/python-markupsafe.spec

# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name: python-markupsafe
Version: 0.18
Release: 1
Summary: Implements a XML/HTML/XHTML Markup safe string for Python
Group: Development/Languages
License: BSD
URL: http://pypi.python.org/pypi/%{upstream_name}
Source0: %{name}-%{version}.tar.gz
BuildRequires: python-devel
BuildRequires: python-setuptools-devel

%description
A library for safe markup escaping.

%package -n python3-markupsafe
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python 3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-markupsafe}

%description -n python3-markupsafe
A library for safe markup escaping. Python 3 version.

%prep
%setup -q -n %{name}-%{version}/markupsafe

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# C code errantly gets installed
rm $RPM_BUILD_ROOT/%{python_sitearch}/markupsafe/*.c

%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# C code errantly gets installed
rm %{buildroot}%{python3_sitearch}/markupsafe/*.c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitearch}/*

%files -n python3-markupsafe
%defattr(-,root,root,-)
%{python3_sitearch}/*
