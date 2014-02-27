%global old_fw 0

Name:           b43-closedfwwf
Version:        5.100.138
%global pre_32_fw_ver 5.10.56.27.3
Release:        1%{?dist}
Summary:        Broadcom wireless proprietary firmware

License:        Proprietary
URL:            http://www.broadcom.com/support/802.11/linux_sta.php
Source0:        http://www.lwfinger.com/b43-firmware/broadcom-wl-%{version}.tar.bz2
Source1:        http://mirror2.openwrt.org/sources/broadcom-wl-%{pre_32_fw_ver}_mipsel.tar.bz2
BuildArch:      noarch

BuildRequires:  b43-fwcutter


%description

This package contains the proprietary software needed to use some
Broadcom wireless NICs.

See http://wireless.kernel.org/en/users/Drivers/b43#devicefirmware

%prep
%setup -q -n broadcom-wl-%{version}
%setup -q -D -T -a 1 -n broadcom-wl-%{version}


%build
%if 0%{?old_fw}
# older firmmware; is this needed anywhere?
b43-fwcutter -w . broadcom-wl-%{pre_32_fw_ver}/driver/wl_apsta/wl_prebuilt.o
%else
# newer firmware for linux 3.2+
b43-fwcutter -w . linux/wl_apsta.o
%endif


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/lib/firmware/b43
cp b43/* $RPM_BUILD_ROOT/lib/firmware/b43


%files
/lib/firmware/b43


%changelog
* Thu Feb 27 2014 John Morris <john@zultron.com> - 5.100.138-1
- Initial package

