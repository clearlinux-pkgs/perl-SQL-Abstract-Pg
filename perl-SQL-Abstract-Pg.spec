#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SQL-Abstract-Pg
Version  : 1.0
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/SQL-Abstract-Pg-1.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/SQL-Abstract-Pg-1.0.tar.gz
Summary  : 'PostgreSQL features for SQL::Abstract'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-SQL-Abstract-Pg-license = %{version}-%{release}
Requires: perl-SQL-Abstract-Pg-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Moo)
BuildRequires : perl(SQL::Abstract)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Test::Deep)

%description
# SQL::Abstract::Pg [![](https://github.com/mojolicious/sql-abstract-pg/workflows/linux/badge.svg)](https://github.com/mojolicious/sql-abstract-pg/actions)

%package dev
Summary: dev components for the perl-SQL-Abstract-Pg package.
Group: Development
Provides: perl-SQL-Abstract-Pg-devel = %{version}-%{release}
Requires: perl-SQL-Abstract-Pg = %{version}-%{release}

%description dev
dev components for the perl-SQL-Abstract-Pg package.


%package license
Summary: license components for the perl-SQL-Abstract-Pg package.
Group: Default

%description license
license components for the perl-SQL-Abstract-Pg package.


%package perl
Summary: perl components for the perl-SQL-Abstract-Pg package.
Group: Default
Requires: perl-SQL-Abstract-Pg = %{version}-%{release}

%description perl
perl components for the perl-SQL-Abstract-Pg package.


%prep
%setup -q -n SQL-Abstract-Pg-1.0
cd %{_builddir}/SQL-Abstract-Pg-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-SQL-Abstract-Pg
cp %{_builddir}/SQL-Abstract-Pg-1.0/LICENSE %{buildroot}/usr/share/package-licenses/perl-SQL-Abstract-Pg/2f8018a02043ed1a43f032379e036bb6b88265f2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/SQL::Abstract::Pg.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-SQL-Abstract-Pg/2f8018a02043ed1a43f032379e036bb6b88265f2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/SQL/Abstract/Pg.pm
