Name:           nginx
Version:        1.12.2
Release:        1%{?dist}
Summary:        nginx

License:        commercial
URL:            http://www.nginx.org
Source0:        nginx-1.12.2.tar.gz

BuildRequires:  perl-devel, zlib-devel
BuildRequires:  openssl, openssl-devel
Requires:       perl-devel, zlib-devel, openssl-devel

%description
the extremely high-performance web server.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--with-http_ssl_module
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp %{_sourcedir}/nginx.service %{buildroot}/usr/lib/systemd/system/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

%attr(755,root,root) %{_prefix}/lib/systemd/system/nginx.service

%doc
%{_sbindir}/nginx
%{_prefix}/conf
%{_prefix}/html
%{_prefix}/lib
%{_prefix}/logs
%{_prefix}/src

%changelog
