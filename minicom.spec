#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : minicom
Version  : 2.7.1
Release  : 3
URL      : https://fossies.org/linux/misc/minicom-2.7.1.tar.gz
Source0  : https://fossies.org/linux/misc/minicom-2.7.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: minicom-bin = %{version}-%{release}
Requires: minicom-license = %{version}-%{release}
Requires: minicom-locales = %{version}-%{release}
Requires: minicom-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : pkg-config-dev
Patch1: 0001-Add-a-missing-va_end-call.patch
Patch2: 0002-Make-sure-strings-copied-by-strncpy-are-null-termina.patch
Patch3: 0003-Fix-file-descriptor-leaks.patch
Patch4: 0004-Fix-a-directory-handle-leak.patch
Patch5: 0005-Fix-a-read-past-end-of-buffer.patch
Patch6: 0006-Fix-a-warning-about-an-unused-variable.patch
Patch7: 0007-loadconv-Add-missing-fclose.patch
Patch8: 0008-Increase-used-automake-verstion-to-1.16.patch
Patch9: 0009-Drop-superfluous-global-variable-definitions.patch
Patch10: 0010-Drop-superfluous-global-variable-definitions.patch
Patch11: 0011-Drop-superfluous-global-variable-definitions.patch

%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

Run 'minicom -s' as root to create a system wide configuration.
Users need read/write permissions on the serial port devices in
order to use minicom.

It's recommended to install lrzsz if you want to transfer files
with minicom.

%package bin
Summary: bin components for the minicom package.
Group: Binaries
Requires: minicom-license = %{version}-%{release}

%description bin
bin components for the minicom package.


%package license
Summary: license components for the minicom package.
Group: Default

%description license
license components for the minicom package.


%package locales
Summary: locales components for the minicom package.
Group: Default

%description locales
locales components for the minicom package.


%package man
Summary: man components for the minicom package.
Group: Default

%description man
man components for the minicom package.


%prep
%setup -q -n minicom-2.7.1
cd %{_builddir}/minicom-2.7.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604099638
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604099638
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/minicom
cp %{_builddir}/minicom-2.7.1/COPYING %{buildroot}/usr/share/package-licenses/minicom/9bcb992fead5b3bf88e5b07cbe868e187626260c
%make_install
%find_lang minicom

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ascii-xfr
/usr/bin/minicom
/usr/bin/runscript
/usr/bin/xminicom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/minicom/9bcb992fead5b3bf88e5b07cbe868e187626260c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ascii-xfr.1
/usr/share/man/man1/minicom.1
/usr/share/man/man1/runscript.1
/usr/share/man/man1/xminicom.1

%files locales -f minicom.lang
%defattr(-,root,root,-)

