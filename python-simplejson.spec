%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-simplejson
Version:        2.0.3
Release:        1%{?dist}
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

Group:          System Environment/Libraries
License:        MIT
URL:            http://undefined.org/python/#simplejson
Source0:        http://cheeseshop.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel


%description
simplejson is a simple, fast, complete, correct and extensible
JSON <http://json.org> encoder and decoder for Python 2.3+.  It is
pure Python code with no dependencies.

simplejson was formerly known as simple_json, but changed its name to
comply with PEP 8 module naming guidelines.

The encoder may be subclassed to provide serialization in any kind of
situation, without any special support by the objects to be serialized
(somewhat like pickle).

The decoder can handle incoming JSON strings of any specified encoding
(UTF-8 by default).



%prep
%setup -q -n simplejson-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT \
                                 --single-version-externally-managed


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc docs LICENSE.txt
%dir %{python_sitearch}/simplejson
%{python_sitearch}/simplejson-%{version}-py%{pyver}.egg-info
%{python_sitearch}/simplejson/*.py*
%{python_sitearch}/simplejson/tests/*.py*
%{python_sitearch}/simplejson/_speedups.so


%changelog
* Mon Oct 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.3-1
- update to 2.0.3

* Wed Oct 01 2008 Luke Macken <lmacken@redhat.com> - 2.0.1-1
- Update to 2.0.1, which contains many optimizations and bugfixes

* Wed Sep 24 2008 Luke Macken <lmacken@redhat.com> - 1.9.3-1
- Update to 1.9.3, which includes a significant decoding speed boost, and
  various bug fixes.

* Tue May 06 2008 Luke Macken <lmacken@redhat.com> - 1.9.1-1
- Update to 1.9.1

* Wed Apr 02 2008 Luke Macken <lmacken@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> - 1.7.4-1
- Update to 1.7.4

* Fri Feb  8 2008 Luke Macken <lmacken@redhat.com> - 1.7.3-3
- Rebuild for gcc 4.3

* Wed Oct 24 2007 Luke Macken <lmacken@redhat.com> - 1.7.3-2
- Include the LICENSE.txt

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> - 1.7.3-1
- 1.7.3

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 1.7.1-3
- Update for python-setuptools changes in rawhide

* Tue Aug 21 2007 Luke Macken <lmacken@redhat.com> - 1.7.1-2
- Rebuild

* Sun Jul  8 2007 Luke Macken <lmacken@redhat.com> - 1.7.1-1
- 1.7.1

* Wed Mar 21 2007 Luke Macken <lmacken@redhat.com> - 1.7-2
- Use python_sitearch instead of sitelib

* Tue Mar 20 2007 Luke Macken <lmacken@redhat.com> - 1.7-1
- 1.7 (Bug #233212)

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 1.5
- 1.5

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 1.4-4
- Add python-devel to BuildRequires

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 1.4-2
- Rebuild for new python

* Fri Nov 24 2006 Luke Macken <lmacken@redhat.com> - 1.4-1
- 1.4

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 1.3-4
- Rebuild for FC6

* Mon Aug 14 2006 Luke Macken <lmacken@redhat.com> - 1.3-3
- Include .pyo's instead of just ghosting them

* Wed Jul 12 2006 Luke Macken <lmacken@redhat.com> - 1.3-2
- Add --single-version-externally-managed flag to install

* Mon Jul 10 2006 Luke Macken <lmacken@redhat.com> - 1.3-1
- Initial package
