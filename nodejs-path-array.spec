%{?scl:%scl_package nodejs-path-array}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-path-array

%global npm_name path-array
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-path-array
Version:    1.0.1
Release:    1%{?dist}
Summary:	Treat your $PATH like a JavaScript Array
Url:		https://github.com/TooTallNate/node-path-array
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(mocha)
%endif

%description
Treat your $PATH like a JavaScript Array

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/path-array

%doc README.md

%changelog
* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- Rebuilt with updated metapackage

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- Initial build
