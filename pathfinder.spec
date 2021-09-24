#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	PathFinder PKI Path Discovery and Validation Daemon
Summary(pl.UTF-8):	PathFinder - demon do rozpoznawania i sprawdzania poprawności ścieżek PKI
Name:		pathfinder
Version:	1.1.7
Release:	4
License:	LGPL v2.1 or BSD (libraries), LGPL v2.1 (programs)
Group:		Libraries
#Source0Download: http://code.google.com/p/pathfinder-pki/downloads/list
Source0:	http://pathfinder-pki.googlecode.com/files/%{name}-%{version}-Source.tar.gz
# Source0-md5:	8307b2297c1efa6c526ce4b656a2e4aa
Source1:	pathfinderd.init
Source2:	pathfinderd.sysconfig
Source3:	pathfinderd.ini
Patch0:		%{name}-c++.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-libdir.patch
Patch3:		%{name}-shared_ptr.patch
Patch4:		%{name}-includes.patch
Patch5:		%{name}-openssl.patch
Patch6:		%{name}-tests.patch
URL:		http://code.google.com/p/pathfinder-pki/
BuildRequires:	cmake >= 2.4.7
BuildRequires:	dbus-devel >= 1
BuildRequires:	libstdc++-devel
BuildRequires:	nss-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	wvstreams-devel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires:	rc-scripts
Provides:	group(pathfinderd)
Provides:	user(pathfinderd)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fpermissive

%description
PathFinder is designed to provide a mechanism for any program to
perform RFC-3280 compliant path validation of X.509 certificates, even
when some of the intermediate certificates are not present on the
local machine. By design, PathFinder automatically downloads any such
certificates from the Internet as needed using the AIA and CRL
distribution point extensions of the certificates it is processing. It
has the ability to do revocation status checking either using CRL or
OCSP, or both. And, given the recent vulnerabilities that have
rendered the MD5 algorithm highly suspect, it allows the administrator
to choose to not validate certificates using that algorithm anywhere
in the trust path.

For the convenience of those using OpenSSL or NSS (Netscape Security
Services), two libraries containing a PathFinder callback suitable for
use with an SSL connection are provided.

%description -l pl.UTF-8
PathFinder powstał w celu dostarczenia dowolnym programom mechanizmu
wykonywania zgodnej z RFC-3280 kontroli poprawności ścieżek
certyfikatów X.509, nawet kiedy niektóre z certyfikatów pośrednich nie
są dostępne na maszynie lokalnej. Zgodnie z projektem, PathFinder
automatycznie ściąga takie certyfikaty z Internetu w miarę potrzeb
przy użyciu rozszerzeń punktów dystrybucji AIA i CRL przetwarzanych
certyfikatów. Potrafi sprawdzać stan odwołań certyfikatów przy użyciu
CRL lub OCSP, albo obu tych mechanizmów. A także, ze względu na
wykryte niedawno luki czyniące algorytm MD5 niewiarygodnym, pozwala
także administratorowi zdecydować, by nie uznawać certyfikatów,
wykorzystujących ten algorytm, za poprawne.

Dla wygody wykorzystujących biblioteki OpenSSL oraz NSS (Netscape
Security Services), dostarczane są dwie biblioteki z odpowiednimi
wywołaniami wstecznymi PathFindera.

%package devel
Summary:	Common development files for PathFinder libraries
Summary(pl.UTF-8):	Wspólne pliki programistyczne bibliotek PathFindera
Group:		Development/Libraries

%description devel
Common development files for PathFinder libraries.

%description devel -l pl.UTF-8
Wspólne pliki programistyczne bibliotek PathFindera.

%package nss
Summary:	NSS PathFinder plugin library
Summary(pl.UTF-8):	Biblioteka wtyczki PathFinder dla NSS
Group:		Libraries
Requires:	dbus-libs >= 1.0
Requires:	nss >= 2.0.0

%description nss
Library that allows NSS (Netscape Security Services) to use PathFinder
for certificate validation.

%description nss -l pl.UTF-8
Biblioteka pozwalająca bibliotece NSS (Netscape Security Services) na
wykorzystywanie PathFindera do sprawdzania poprawności certyfikatów.

%package nss-devel
Summary:	Header file for NSS PathFinder plugin library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki wtyczki PathFinder dla NSS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-nss = %{version}-%{release}
Requires:	dbus-devel >= 1.0
Requires:	nss-devel >= 2.0.0

%description nss-devel
Header file for NSS PathFinder plugin library.

%description nss-devel -l pl.UTF-8
Plik nagłówkowy biblioteki wtyczki PathFinder dla NSS.

%package nss-static
Summary:	Static NSS PathFinder plugin library
Summary(pl.UTF-8):	Statyczna biblioteka wtyczki PathFinder dla NSS
Group:		Development/Libraries
Requires:	%{name}-nss-devel = %{version}-%{release}

%description nss-static
Static NSS PathFinder plugin library.

%description nss-static -l pl.UTF-8
Statyczna biblioteka wtyczki PathFinder dla NSS.

%package openssl
Summary:	OpenSSL PathFinder plugin library
Summary(pl.UTF-8):	Biblioteka wtyczki PathFinder dla OpenSSL
Group:		Libraries
Requires:	dbus-libs >= 1.0
Requires:	openssl >= 0.9.8

%description openssl
Library that allows OpenSSL to use PathFinder for certificate
validation.

%description openssl -l pl.UTF-8
Biblioteka pozwalająca bibliotece OpenSSL na wykorzystywanie
PathFindera do sprawdzania poprawności certyfikatów.

%package openssl-devel
Summary:	Header file for OpenSSL PathFinder plugin library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki wtyczki PathFinder dla OpenSSL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-openssl = %{version}-%{release}
Requires:	dbus-devel >= 1.0
Requires:	openssl-devel >= 0.9.8

%description openssl-devel
Header file for OpenSSL PathFinder plugin library.

%description openssl-devel -l pl.UTF-8
Plik nagłówkowy biblioteki wtyczki PathFinder dla OpenSSL.

%package openssl-static
Summary:	Static OpenSSL PathFinder plugin library
Summary(pl.UTF-8):	Statyczna biblioteka wtyczki PathFinder dla OpenSSL
Group:		Development/Libraries
Requires:	%{name}-openssl-devel = %{version}-%{release}

%description openssl-static
Static OpenSSL PathFinder plugin library.

%description openssl-static -l pl.UTF-8
Statyczna biblioteka wtyczki PathFinder dla OpenSSL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
# out-of-tree build is broken (missing -I$builddir)
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/pki/pathfinderd/trusted-certs

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/pathfinderd
install -D %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/pathfinderd
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/pathfinderd.ini

install -d $RPM_BUILD_ROOT%{systemdtmpfilesdir}
cat >$RPM_BUILD_ROOT%{systemdtmpfilesdir}/pathfinderd.conf <<EOF
D /var/run/pathfinderd 0755 pathfinderd pathfinderd -
EOF
install -d $RPM_BUILD_ROOT/var/run/pathfinderd

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 314 pathfinderd
%useradd -u 314 -d /var/run/pathfinderd -g pathfinderd -c "PathFinder User" -s /bin/false pathfinderd 

%post
/sbin/chkconfig --add pathfinderd
%service pathfinderd restart

%preun
if [ "$1" = "0" ]; then
	%service -q pathfinderd stop
	/sbin/chkconfig --del pathfinderd
fi

%postun
if [ "$1" = "0" ]; then
	%userremove pathfinderd
	%groupremove pathfinderd
fi

%post	nss -p /sbin/ldconfig
%postun	nss -p /sbin/ldconfig

%post	openssl -p /sbin/ldconfig
%postun	openssl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README pathfinderd.ini.sample
%attr(755,root,root) %{_bindir}/pathclient
%attr(755,root,root) %{_bindir}/pathverify
%attr(755,root,root) %{_sbindir}/pathfinderd
/etc/dbus-1/system.d/pathfinderd.conf
%dir /etc/pki/pathfinderd
%dir /etc/pki/pathfinderd/trusted-certs
%attr(754,root,root) /etc/rc.d/init.d/pathfinderd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/pathfinderd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pathfinderd.ini
%{systemdtmpfilesdir}/pathfinderd.conf
%attr(755,pathfinderd,pathfinderd) %dir /var/run/pathfinderd
%{_mandir}/man8/pathfinderd.8*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/pathfinder-1
%{_includedir}/pathfinder-1/libpathfinder.h
%{_mandir}/man3/pathclient.3*
%{_mandir}/man3/pathverify.3*

%files nss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpathfinder-nss-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpathfinder-nss-1.so.1

%files nss-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpathfinder-nss-1.so
%{_includedir}/pathfinder-1/libpathfinder-nss.h
%{_pkgconfigdir}/pathfinder-nss.pc

%if %{with static_libs}
%files nss-static
%defattr(644,root,root,755)
%{_libdir}/libpathfinder-nss-1.a
%endif

%files openssl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpathfinder-openssl-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpathfinder-openssl-1.so.1

%files openssl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpathfinder-openssl-1.so
%{_includedir}/pathfinder-1/libpathfinder-openssl.h
%{_pkgconfigdir}/pathfinder-openssl.pc

%if %{with static_libs}
%files openssl-static
%defattr(644,root,root,755)
%{_libdir}/libpathfinder-openssl-1.a
%endif
