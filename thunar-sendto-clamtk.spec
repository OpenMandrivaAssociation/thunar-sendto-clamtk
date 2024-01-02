Name: thunar-sendto-clamtk
Version: 0.08
Release: 1
Summary: Simple virus scanning extension for Thunar
License: GPL+ or Artistic 2.0
Group:		Graphical desktop/Xfce
URL: https://github.com/dave-theunsub/thunar-sendto-clamtk
Source0: https://github.com/dave-theunsub/thunar-sendto-clamtk/releases/download/v%{version}/thunar-sendto-clamtk-%{version}.tar.xz
BuildArch: noarch
 
BuildRequires: desktop-file-utils
Requires: thunar 
Requires: clamtk >= 5.00
 
%description
This is a simple extension to add virus scanning to Thunar
in the send-to menu.
 
With this extension installed, it is easy to scan files for threats.
 
%prep
%setup -q
 
%build
 
%install
 
desktop-file-install --vendor "" \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/Thunar/sendto \
	%{name}.desktop
 
%files
%doc CHANGES DISCLAIMER LICENSE README.md
%{_datadir}/Thunar/sendto/%{name}.desktop
