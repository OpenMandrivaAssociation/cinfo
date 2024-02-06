Name:           cinfo
Version:        0.5.5
Release:        1
Summary:        Fast and minimal system information tool
Group:          Tools/Monitoring
License:        GPL-3.0-only
URL:            https://github.com/mrdotx/cinfo
Source0:        https://github.com/mrdotx/cinfo/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make

%description
%{summary}

%prep
%autosetup -p1

%build
# remove lines that build for pacman
sed -i -e '/\*PKGS_CMD/d' -e '/\*PKGS_DESC/d' config.def.h
# add lines to build for dnf
cat >> config.def.h << EOL
static const char *PKGS_CMD             = "rpm -qa | wc -l",
                  *PKGS_DESC            = " [dnf]";
EOL

%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
