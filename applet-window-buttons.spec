%global orig_name org.kde.windowbuttons

Name:           applet-window-buttons
Version:        0.9.0
Release:        1%{?dist}
Summary:        Plasma 5 applet to show window buttons in panels
License:        GPLv2+
URL:            https://github.com/psifidotos/applet-window-buttons
Source0:        https://github.com/psifidotos/applet-window-buttons/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  libSM-devel
BuildRequires:  kf5-plasma-devel

BuildRequires:  cmake(KDecoration2) 
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)


%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels. This plasmoid is coming from Latte land, but it can also
support Plasma panels.

%prep
%autosetup -n %{name}-%{version}


%build
%cmake
%cmake_build

%install
%cmake_install


%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/%{orig_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%files
%license LICENSE
%dir %{_kf5_datadir}/plasma/plasmoids/org.kde.windowbuttons
%{_kf5_datadir}/plasma/plasmoids/org.kde.windowbuttons
%{_qt5_qmldir}/org/kde/appletdecoration
%{_kf5_datadir}/kservices5/plasma-applet-%{orig_name}.desktop
%{_kf5_metainfodir}/%{orig_name}.appdata.xml

%{_kf5_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop
%{_kf5_datadir}/plasma/plasmoids/%{orig_name}/contents/
%{_kf5_datadir}/plasma/plasmoids/%{orig_name}/metadata.json
