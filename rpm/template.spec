Name:           ros-melodic-mcl-3dl
Version:        0.1.5
Release:        1%{?dist}
Summary:        ROS mcl_3dl package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-mcl-3dl-msgs
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-pcl-ros
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf2
Requires:       ros-melodic-tf2-geometry-msgs
Requires:       ros-melodic-tf2-ros
Requires:       ros-melodic-tf2-sensor-msgs
Requires:       ros-melodic-visualization-msgs
BuildRequires:  eigen3-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-mcl-3dl-msgs
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-pcl-ros
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf2
BuildRequires:  ros-melodic-tf2-geometry-msgs
BuildRequires:  ros-melodic-tf2-ros
BuildRequires:  ros-melodic-tf2-sensor-msgs
BuildRequires:  ros-melodic-visualization-msgs

%description
3-D/6-DOF localization for mobile robots with 3-D LIDAR(s)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Aug 16 2019 Atsushi Watanabe <atsushi.w@ieee.org> - 0.1.5-1
- Autogenerated by Bloom

* Fri Dec 21 2018 Atsushi Watanabe <atsushi.w@ieee.org> - 0.1.4-0
- Autogenerated by Bloom

* Sat Jun 23 2018 Atsushi Watanabe <atsushi.w@ieee.org> - 0.1.3-0
- Autogenerated by Bloom

