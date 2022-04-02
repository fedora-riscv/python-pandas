%global srcname pandas

# Break cycles with optional dependencies
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        1.3.5
Release:        1%{?dist}
Summary:        Python library providing high-performance data analysis tools

License:        BSD
URL:            https://pandas.pydata.org/
Source0:        %{pypi_source %{srcname}}

# Partial backport of upstream commit d437902f46acbff4a03d748b30620bc75fa5ea1f:
# “CI: Migrate Python 3.10 testing to Posix GHA/Azure Pipelines (#45120)”
#
# Fixes error in TestDataFramePlots.test_raise_error_on_datetime_time_data
Patch:          pandas-1.3.5-d437902.patch

# Partial backport of upstream commit 560172832922594fe9e75ca4a6060ff0cb7f7089
# “CI: Merge database workflow into posix workflow (#45060)”
#
# Fixes error in TestToDatetime.test_to_datetime_tz_psycopg2
Patch:          pandas-1.3.5-5601728.patch

# Partial backport of upstream commit 2dd75ca5e04a18db9d79d9bed01726b40b6268e9
# “TST: Ensure tm.network has pytest.mark.network (#45732)”
#
# Fixes error in test_wrong_url[lxml] when the “network” mark is deselected
Patch:          pandas-1.3.5-2dd75ca.patch

# Fix a few test failues on big-endian systems
# https://github.com/pandas-dev/pandas/pull/46681
# (PR is for main branch; this version of the patch is for 1.3.5)
Patch:          pandas-1.3.5-pr-46681.patch

# Do not install C sources in binary distributions
# https://github.com/pandas-dev/pandas/pull/46739
# (PR is for main branch; this version of the patch is for 1.3.5)
Patch:          pandas-1.3.5-pr-46739.patch

%global _description %{expand:
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  python3-devel

# pyproject.toml: [build-system] requires
BuildRequires:  python3dist(setuptools) >= 51
BuildRequires:  python3dist(wheel)
BuildRequires:  ((python3dist(cython) >= 0.29.24) with (python3dist(cython) < 3))

# setup.cfg: [options] install_requires
BuildRequires:  python3dist(numpy) >= 1.21
BuildRequires:  python3dist(python-dateutil) >= 2.7.3
BuildRequires:  python3dist(pytz) >= 2017.3

# doc/source/getting_started/install.rst “Recommended dependencies”
# Since these provide large speedups, we make them hard dependencies.
BuildRequires:  python3dist(numexpr) >= 2.7
Requires:       python3dist(numexpr) >= 2.7
BuildRequires:  python3dist(bottleneck) >= 1.2.1
Requires:       python3dist(bottleneck) >= 1.2.1

# doc/source/getting_started/install.rst “Optional dependencies”
# We BR all weak dependencies to ensure they are installable.

# Visualization
BuildRequires:  python3dist(setuptools) >= 38.6
Recommends:     python3dist(setuptools) >= 38.6
BuildRequires:  python3dist(matplotlib) >= 2.2.3
Recommends:     python3dist(matplotlib) >= 2.2.3
BuildRequires:  python3dist(jinja2) >= 2.10
Recommends:     python3dist(jinja2) >= 2.10
%if %{without bootstrap}
BuildRequires:  python3dist(tabulate) >= 0.8.7
Recommends:     python3dist(tabulate) >= 0.8.7
%endif

# Computation
# Documented minimum SciPy version is 1.12, but this is a typo since that
# version does not exist yet.
BuildRequires:  python3dist(scipy)
Recommends:     python3dist(scipy)
# python-numba is not currently packaged:
# BuildRequires:  python3dist(numba) >= 0.46
# Recommends:     python3dist(numba) >= 0.46
BuildRequires:  python3dist(xarray) >= 1.12.3
Recommends:     python3dist(xarray) >= 1.12.3

# Excel files
BuildRequires:  python3dist(xlrd) >= 1.2
Recommends:     python3dist(xlrd) >= 1.2
BuildRequires:  python3dist(xlwt) >= 1.3
Recommends:     python3dist(xlwt) >= 1.3
BuildRequires:  python3dist(xlsxwriter) >= 1.0.2
Recommends:     python3dist(xlsxwriter) >= 1.0.2
BuildRequires:  python3dist(openpyxl) >= 3
Recommends:     python3dist(openpyxl) >= 3
# python-pyxlsb is not currently packaged:
# BuildRequires:  python3dist(pyxlsb) >= 1.0.6
# Recommends:     python3dist(pyxlsb) >= 1.0.6

# HTML
BuildRequires:  python3dist(beautifulsoup4) >= 4.6
Recommends:     python3dist(beautifulsoup4) >= 4.6
BuildRequires:  python3dist(html5lib) >= 1.0.1
Recommends:     python3dist(html5lib) >= 1.0.1
# lxml handled below:

# XML
BuildRequires:  python3dist(lxml) >= 4.3
Recommends:     python3dist(lxml) >= 4.3

# SQL databases
BuildRequires:  python3dist(sqlalchemy) >= 1.3
Recommends:     python3dist(sqlalchemy) >= 1.3
BuildRequires:  python3dist(psycopg2) >= 2.7
Recommends:     python3dist(psycopg2) >= 2.7
BuildRequires:  python3dist(pymysql) >= 0.8.1
Recommends:     python3dist(pymysql) >= 0.8.1

# Other data sources
BuildRequires:  python3dist(tables) >= 3.5.1
Recommends:     python3dist(tables) >= 3.5.1
# Dependencies on blosc and zlib are indirect, via PyTables, so we do not
# encode them here. Note also that the minimum blosc version in the
# documentation seems to be that of the blosc C library, not of the blosc PyPI
# package.
# python-fastparquet is not currently packaged:
# BuildRequires:  python3dist(fastparquet) >= 0.4
# Recommends:     python3dist(fastparquet) >= 0.4
# python-pyarrow is not currently packaged:
# BuildRequires:  python3dist(pyarrow) >= 0.17
# Recommends:     python3dist(pyarrow) >= 0.17
# python-pyreadstat is not currently packaged:
# BuildRequires:  python3dist(pyreadstat)
# Recommends:     python3dist(pyreadstat)

# Access data in the cloud
BuildRequires:  python3dist(fsspec) >= 0.7.4
Recommends:     python3dist(fsspec) >= 0.7.4
BuildRequires:  python3dist(gcsfs) >= 0.6
Recommends:     python3dist(gcsfs) >= 0.6
# python-pandas-gbq is not currently packaged:
# BuildRequires:  python3dist(pandas-gbq) >= 0.12
# Recommends:     python3dist(pandas-gbq) >= 0.12
# python-s3fs is not currently packaged:
# BuildRequires:  python3dist(s3fs) >= 0.4
# Recommends:     python3dist(s3fs) >= 0.4

# Clipboard
BuildRequires:  python3dist(pyqt5)
Recommends:     python3dist(pyqt5)
BuildRequires:  python3dist(qtpy)
Recommends:     python3dist(qtpy)
BuildRequires:  xclip
Recommends:     xclip
BuildRequires:  xsel
Recommends:     xsel

# This is just an “ecosystem” package in the upstream documentation, but there
# is an integration test for it. This package historically had a weak
# dependency on it, which we keep around until we package 1.4.0 to ensure
# backward compatibility.
BuildRequires:  python3dist(pandas-datareader)
Recommends:     python3dist(pandas-datareader)

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p1

# Ensure Cython-generated sources are re-generated
rm -vf $(grep -rl '/\* Generated by Cython')

# We just want to build with the numpy in Fedora:
sed -r -i '/\boldest-supported-numpy\b/d' pyproject.toml


%build
%py3_build


%install
%py3_install


%files -n python3-pandas
%doc README.md
%doc RELEASE.md
%license LICENSE
%{python3_sitearch}/%{srcname}*


%changelog
* Sat Apr 02 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.5-1
- Update to 1.3.5
- Drop compatibility with old RHEL releases that will not get this version anyway
- Update weak dependencies from documentation
- Also package README.md
- Do not install C sources

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.3.3-2
- New release of pandas 1.3.3
- Add missing sources

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

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

