Name:           adwcolor
Version:        1.0
Release:        4%{?dist}
Summary:        Easily modify and create Libadwaita color themes

License:        GPL v3
URL:            https://github.com/risiOS/adwcolor
Source0:        https://github.com/risiOS/adwcolor/archive/refs/heads/main.tar.gz

BuildArch:	noarch

BuildRequires:  python3-devel
Requires: 		python3
Recommends:		adw-gtk-theme

%description
Easily Modify and create Libadwaita color themes by modifying the ~/.config/gtk-4.0/gtk.css.

%prep
%autosetup -n %{name}-main

%build
%install
mkdir -p %{buildroot}%{python3_sitelib}/adwcolor
mkdir -p %{buildroot}%{_bindir}

install -m 0755 *.py %{buildroot}%{python3_sitelib}/adwcolor
install -m 0755 __main__.py %{buildroot}%{_bindir}/adwcolor

%files
# %license add-license-file-here
# %doc add-docs-here
%dir %{python3_sitelib}/adwcolor
%{python3_sitelib}/adwcolor/*.py
%{python3_sitelib}/adwcolor/__pycache__/*.pyc
%{_bindir}/adwcolor
%license LICENSE

%changelog
* Fri Jun 24 2022 PizzaLovingNerd
- First spec file
