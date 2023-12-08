#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
Name     : minicom
Version  : 2.8
Release  : 6
URL      : https://fossies.org/linux/misc/minicom-2.8.tar.bz2
Source0  : https://fossies.org/linux/misc/minicom-2.8.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: minicom-bin = %{version}-%{release}
Requires: minicom-license = %{version}-%{release}
Requires: minicom-locales = %{version}-%{release}
Requires: minicom-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : ncurses-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n minicom-2.8
cd %{_builddir}/minicom-2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702033593
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702033593
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/minicom
cp %{_builddir}/minicom-%{version}/COPYING %{buildroot}/usr/share/package-licenses/minicom/9bcb992fead5b3bf88e5b07cbe868e187626260c || :
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

