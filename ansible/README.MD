# Installation on RHEL 9 Automatisation

Ansible Playbook allowing to create ostree images for edge using Ansible.

## Pre-requisites

RHEL 9 pre-requisites :

- RHEL 9 is installed
- The Red Hat repositories **baseos** and **appstream** are reachable

Microshift pre-requisites :

- RHEL 9.2 or 9.3
- LVM volume group (VG) with unused space

## Pre-requisites on the target machine

```sh
sudo subscription-manager register --username $RHN_LOGIN --auto-attach
sudo subscription-manager attach --pool=$RHN_POOL_ID
```

## Ansible Config

Create a `inventory.yaml` file inside the ansible folder or define the inventory path inside the `ansible.cfg` file  

Update `config.yaml` in `ansible/group_vars/all/` to match your environment.

Create an ansible vault named `vault.yaml` in `ansible/group_vars/all/` with the following content.

```yaml
blueprint_admin_password_hash: # Generate one with "mkpasswd -m bcrypt"
kickstart_microshift_pull_secret: # Generate one on https://console.redhat.com/openshift/install/pull-secret
```

Install the required collections.

```sh
ansible-galaxy collection install -r requirements.yaml
```

## Prepare the target machine

```sh
ansible-playbook prerequisites.yaml
ansible-playbook bootstrap-ostree.yaml
```

## Regular builds

```sh
ansible-playbook build.yaml
```
