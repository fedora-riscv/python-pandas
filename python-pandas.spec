%global srcname pandas


Name:           python-%{srcname}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python library providing high-performance data analysis tools

License:        BSD
URL:            https://pandas.pydata.org/
Source0:        %{pypi_source}

%global _description %{expand:
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.}

%description %_description

%package -n python3-%{srcname}
Summary:        Python library providing high-performance data analysis tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-matplotlib
BuildRequires:  python3-Cython >= 0.29.13
Requires:       python3-pytz
Requires:       python3-dateutil
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-tables
Requires:       python3-matplotlib
Requires:       python3-Bottleneck
Requires:       python3-numexpr
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     python3-pandas-datareader
Recommends:     python3-xlrd
Recommends:     python3-xlwt
%endif

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1
# Cython is too old in RHEL8.0
%{!?el8:rm -f $(grep -rl '/\* Generated by Cython')}

%build
%py3_build

%install
%py3_install

%files -n python3-pandas
%doc RELEASE.md
%license LICENSE
%{python3_sitearch}/%{srcname}*

%changelog
* Wed Jul 21 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.3.0-1
- New release of pandas 1.3.0

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 1.2.4-2
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.4-1
- New release of pandas 1.2.4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Orion Poplawski <orion@nwra.com> - 1.2.1-1
- Update to 1.2.1

* Wed Jan 13 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.0-1
- New release of pandas 1.2.0

* Fri Nov 27 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.4-1
- New release of pandas 1.1.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.5-1
- Update to latest version

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Orion Poplawski <orion@nwra.com> - 1.0.1-1
- Update to 1.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.25.3-1
- New release of pandas 0.25.3 (python 3.8 support included)

* Fri Sep 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.1-2
- Backport patch for Python 3.8 compatibility

* Sat Aug 24 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.25.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.1-3
- Fix doc build with numpydoc 0.9

* Tue Jun 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.1-2
- Subpackage python2-pandas has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Mar 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.1-1
- Update to 0.24.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.4-1
- New release of pandas 0.23.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.0-1
- New release of pandas 0.23.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.22.0-1
- New release of pandas 0.22.0

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 0.20.3-2
- Update conditionals

* Sun Sep 10 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.20.3-1
- New upstream version (0.20.3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.20.1-1
- New upstream version (0.20.1)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.2-1
- New upstream version (0.19.2)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.1-1
- New upstream version (0.19.1)

* Wed Oct 19 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.0-1
- New upstream version (0.19.0)
- Brings pandas-datareader using recommends

* Sat Oct 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18.1-3
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18.1-1
- New upstream version (0.18.1)
- Update pypi url

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.18.0-3
- Fix broken deps

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.18.0-2
- Fix python_provide macros usage (FTBFS for some packages)

* Wed Mar 30 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18.0-1
- New upstream version (0.18.0)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.1-1
- New upstream version (0.17.1)
- Add new dependecy as weak dep (fixes bz #1288919)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 Orion Poplawski <orion@cora.nwra.com> - 0.17.0-2
- Use common build directory, new python macros
- Filter provides
- Fix provides

* Mon Oct 12 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.0-1
- New release of pandas 0.17.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.2-1
- New release of pandas 0.16.2

* Mon May 18 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.1-1
- New release of pandas 0.16.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.16.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 24 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.0-1
- New release of pandas 0.16.0
- Use license macro
- Don't use py3dir (new python guidelines)

* Tue Jan 20 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-3
- Pandas actually supports dateutil 2

* Mon Jan 19 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-2
- Update dependency on dateutil to dateutil15 (bz #1183368)

* Wed Dec 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-1
- New release of pandas 0.15.2

* Thu Nov 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.1-1
- New release of pandas 0.15.1

* Mon Oct 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-1
- New release of pandas 0.15.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-1
- New release of pandas 0.14.1

* Mon Jun 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.0-1
- New release of pandas 0.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.12.0-4
- Enable python3 build
- Set CFLAGS before build

* Fri Dec 13 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-3
- Fixed dependency name

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 0.12.0-2
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Fri Sep 20 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-1
- New release of pandas 0.12.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.9-1
- New release of pandas

* Fri Aug 03 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-2
- Fixes from review request

* Tue Jul 10 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-1
- Initial release in Fedora

