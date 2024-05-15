Name:       ca-certificates-custom
Version:    0.0.1
Release:    rh1
Summary:    Custom CA Certificates
License:    BSD
Source0:    custom-ca.crt
Requires(post): ca-certificates
Requires(postun): ca-certificates
BuildArch:  noarch

%description
Custom CA certificates

# We are evil, we have no changelog !
%global source_date_epoch_from_changelog 0

%prep
##
## If you do not have a real CA certificate, you can generate one with:
##
# openssl req -new -nodes -keyout custom-ca.key -out custom-ca.crt -x509 -subj '/CN=Custom CA'
cp %{S:0} custom-ca.crt

%build

%install
install -m 0644 -D custom-ca.crt %{buildroot}/etc/pki/ca-trust/source/anchors/custom-ca.crt

%files
%config %attr(0644, root, root) /etc/pki/ca-trust/source/anchors/custom-ca.crt

%post
##
## You can verify the post script is working by running the following command
## after the RPM installation:
##
#
# user@localhost$ grep -i custom /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
# Custom CA
# user@localhost$ echo $?
# 0
#
update-ca-trust extract

%postun
##
## You can verify the postun script is working by running the following command
## after the RPM un-installation:
##
#
# user@localhost$ grep -i custom /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
# user@localhost$ echo $?
# 1
#
update-ca-trust extract

%changelog
