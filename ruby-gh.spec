#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	gh
Summary:	Layered GitHub Client
Name:		ruby-%{pkgname}
Version:	0.14.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	b08fa6c05fd209725951215ca4e2b1a2
URL:		http://gh.rkh.im/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rspec
BuildRequires:	ruby-webmock
%endif
Requires:	ruby-addressable
Requires:	ruby-backports
Requires:	ruby-faraday < 1
Requires:	ruby-faraday >= 0.8
Requires:	ruby-multi_json < 2
Requires:	ruby-multi_json >= 1.0
Requires:	ruby-net-http-persistent >= 2.7
Requires:	ruby-net-http-pipeline
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-layer client for the GitHub API v3.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
