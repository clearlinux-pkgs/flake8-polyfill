#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-polyfill
Version  : 1.0.1
Release  : 2
URL      : https://pypi.python.org/packages/71/6e/dd7e0f0ddf146213d0cc0b963b3d4c6434823ebe3992c29b523182bbf785/flake8-polyfill-1.0.1.tar.gz
Source0  : https://pypi.python.org/packages/71/6e/dd7e0f0ddf146213d0cc0b963b3d4c6434823ebe3992c29b523182bbf785/flake8-polyfill-1.0.1.tar.gz
Summary  : Polyfill package for Flake8 plugins
Group    : Development/Tools
License  : MIT
Requires: flake8-polyfill-python
Requires: flake8
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=============================
Polyfill for Flake8 Plugins
=============================

%package python
Summary: python components for the flake8-polyfill package.
Group: Default

%description python
python components for the flake8-polyfill package.


%prep
%setup -q -n flake8-polyfill-1.0.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487899907
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487899907
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
