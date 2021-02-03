Name:       my-app
Version:    1.0
Release:    %{RELEASE}%{?dist}
Summary:    Test UI
License:    test
URL:        https://github.com/chandrasekhar1996/libvips-issue

%description
Test UI

%install
mkdir -p %{buildroot}/home/chandu/var/%{name}/
mkdir -p %{buildroot}/home/chandu/var/%{name}/src/
mkdir -p %{buildroot}/home/chandu/logs/%{name}/

cp -r %{SOURCE_DIR}/.next %{buildroot}/home/chandu/var/%{name}/
cp -r %{SOURCE_DIR}/pages %{buildroot}/home/chandu/var/%{name}/
cp -r %{SOURCE_DIR}/public %{buildroot}/home/chandu/var/%{name}/
cp -r %{SOURCE_DIR}/node_modules %{buildroot}/home/chandu/var/%{name}/
cp -r %{SOURCE_DIR}/styles %{buildroot}/home/chandu/var/%{name}/
cp -r %{SOURCE_DIR}/package.json %{buildroot}/home/chandu/var/%{name}/
cp -r %{SOURCE_DIR}/package-lock.json %{buildroot}/home/chandu/var/%{name}/

%files
/home/chandu/logs/%{name}/
/home/chandu/var/%{name}/
