Name:           SoapySDR
Version:	%{VERSION}
Release:        1%{?dist}
Summary:        Vendor and platform neutral SDR support library.
License:        Boost Software Licence
Group:          Development/Libraries/C and C++
Url:            https://github.com/pothosware/SoapySDR/wiki
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	doxygen

%description
Vendor and platform neutral SDR support library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:	%{name} = %{version}

%description    devel
Vendor and platform neutral SDR support library.

%package        python
Summary:        Python files for %{name}
Group:          Development/Libraries/C and C++
Requires:	%{name} = %{version}
Requires:	python

%description    python
Vendor and platform neutral SDR support library.

%prep
%setup -n %{name}-soapy-sdr-%{version}

%build
cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE_1_0.txt README.md
%{_bindir}/SoapySDRUtil
%{_libdir}/libSoapySDR.so.*
%{_mandir}/man1/SoapySDRUtil.1.gz


%files devel
%defattr(-,root,root)
%{_includedir}/SoapySDR
%{_libdir}/libSoapySDR.so
%{_libdir}/pkgconfig/SoapySDR.pc
%{_datarootdir}/cmake/SoapySDR/*

%files python
%defattr(-,root,root)
%{_libdir}/python2.7/site-packages/*SoapySDR.*

%changelog

