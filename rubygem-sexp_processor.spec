%define oname sexp_processor

Name:       rubygem-%{oname}
Version:    3.0.5
Release:    2
Summary:    Branches from ParseTree bringing all the generic sexp processing tools with it
Group:      Development/Ruby
License:    MIT
URL:        http://rubyforge.org/projects/parsetree/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(rubyforge) >= 2.0.4
Requires:   rubygem(minitest) >= 1.6.0
Requires:   rubygem(hoe) >= 2.6.0
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.


%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
ruby -pi -e 'sub(/\/usr\/local\/bin\/ruby/, "/usr/bin/env ruby")' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/*
chmod 755 %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/*

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sun Oct 10 2010 Rémy Clouard <shikamaru@mandriva.org> 3.0.5-1mdv2011.0
+ Revision: 584526
- import rubygem-sexp_processor

