%global orig_name org.kde.windowbuttons

Name:           applet-window-buttons
Version:        0.9.0
Release:        1
Summary:        Plasma 5 applet to show window buttons in panels
License:        GPLv2+
URL:            https://github.com/psifidotos/applet-window-buttons
Source0:        https://github.com/psifidotos/applet-window-buttons/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KDecoration2) 
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5PlasmaQuick)

BuildRequires:  pkgconfig(sm)


%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels. This plasmoid is coming from Latte land, but it can also
support Plasma panels.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSE
#dir %{_kf5_datadir}/plasma/plasmoids/org.kde.windowbuttons
#{_kf5_datadir}/plasma/plasmoids/org.kde.windowbuttons
#{_qt5_qmldir}/org/kde/appletdecoration
#{_kf5_datadir}/kservices5/plasma-applet-%{orig_name}.desktop
#{_kf5_metainfodir}/%{orig_name}.appdata.xml

#{_kf5_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop
#{_kf5_datadir}/plasma/plasmoids/%{orig_name}/contents/
#{_kf5_datadir}/plasma/plasmoids/%{orig_name}/metadata.json
