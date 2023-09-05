# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name: python-markupsafe
Version: 2.1.3
Release: 1
Summary: Implements a XML/HTML/XHTML Markup safe string for Python
License: BSD
URL: https://pypi.org/project/MarkupSafe/
Source0: %{name}-%{version}.tar.gz

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
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# C code errantly gets installed
rm %{buildroot}%{python3_sitearch}/markupsafe/*.c

%files -n python3-markupsafe
%defattr(-,root,root,-)
%license LICENSE.rst
%{python3_sitearch}/*
