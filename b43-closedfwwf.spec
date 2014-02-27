Name:           b43-closedfwwf
Version:        5.100.138
Release:        1%{?dist}
Summary:        Broadcom wireless proprietary firmware

License:        Proprietary
URL:            http://www.broadcom.com/support/802.11/linux_sta.php
Source0:        http://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.138.tar.bz2
BuildArch:      noarch

BuildRequires:  b43-fwcutter


%description

This package contains the proprietary software needed to use some
Broadcom wireless NICs.

See http://wireless.kernel.org/en/users/Drivers/b43#devicefirmware

%prep
%setup -q -n broadcom-wl-%{version}


%build
b43-fwcutter -w . linux/wl_apsta.o


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/lib/firmware/b43
cp b43/* $RPM_BUILD_ROOT/lib/firmware/b43


%files
/lib/firmware/b43


%changelog
* Thu Feb 27 2014 John Morris <john@zultron.com> - 5.100.138-1
- Initial package

