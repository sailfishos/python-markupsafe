# Adapted from Fedora's packaging (2014-02-17)
# http://pkgs.fedoraproject.org/cgit/python-markupsafe.git/tree/python-markupsafe.spec

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

%prep
%setup -q -n %{name}-%{version}/markupsafe

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# C code errantly gets installed
rm $RPM_BUILD_ROOT/%{python_sitearch}/markupsafe/*.c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitearch}/*
