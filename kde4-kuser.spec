# TODO
#   %{_pkgconfigdir}/system-tools-backends.pc
%define		_state		stable
%define		orgname		kuser
%define		qtver		4.8.1

%include	/usr/lib/rpm/macros.perl

Summary:	KDE User management tool
Summary(pl.UTF-8):	Administracja kontami dla KDE
Summary(pt_BR.UTF-8):	Ferramenta para administração de usuários
Name:		kde4-%{orgname}
Version:	4.12.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	59e31e834787836501c89f2ffd7c021c
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdebase >= %{version}
Requires:	shadow
Obsoletes:	kde4-kdeadmin-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple tool for managing system groups and user accounts from
system.

%description -l pl.UTF-8
Narzędzie do dodawania/usuwania użytkowników oraz do zmiany danych o
nich.

%description -l pt_BR.UTF-8
Ferramenta para administração de usuários do sistema.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_datadir}/config.kcfg/kuser.kcfg
%{_desktopdir}/kde4/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png
