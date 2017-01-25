
Name: app-nginx
Epoch: 1
Version: 2.3.0
Release: 1%{dist}
Summary: NGINX - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-nginx-%{version}.tar.gz
Buildarch: noarch

%description
NGINX is web server, reverse proxy, load balancer and web cache.

%package core
Summary: NGINX - Core
Requires: app-base-core
Requires: nginx

%description core
NGINX is web server, reverse proxy, load balancer and web cache.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/nginx
cp -r * %{buildroot}/usr/clearos/apps/nginx/

install -d -m 0755 %{buildroot}/var/clearos/nginx
install -d -m 0755 %{buildroot}/var/clearos/nginx/backup
install -D -m 0644 packaging/nginx.php %{buildroot}/var/clearos/base/daemon/nginx.php

%post core
logger -p local6.notice -t installer 'app-nginx-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/nginx/deploy/install ] && /usr/clearos/apps/nginx/deploy/install
fi

[ -x /usr/clearos/apps/nginx/deploy/upgrade ] && /usr/clearos/apps/nginx/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-nginx-core - uninstalling'
    [ -x /usr/clearos/apps/nginx/deploy/uninstall ] && /usr/clearos/apps/nginx/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/nginx/packaging
%dir /usr/clearos/apps/nginx
%dir /var/clearos/nginx
%dir /var/clearos/nginx/backup
/usr/clearos/apps/nginx/deploy
/usr/clearos/apps/nginx/language
/usr/clearos/apps/nginx/libraries
/var/clearos/base/daemon/nginx.php
