# SystemTuner-Swappiness

> Optimize Memory, Prioritize Performance.

This project provides a focused, automated toolkit for tuning the swappiness value on Linux systems. It is designed for system administrators and DevOps engineers who need to ensure that physical RAM is prioritized over swap space, which is critical for the performance of databases and applications.

## What is Swappiness?

Swappiness is a Linux kernel parameter that controls the relative weight given to swapping out runtime memory, as opposed to dropping pages from the system page cache. A high swappiness value means that the kernel will be more aggressive in swapping out memory pages, while a low value will make the kernel less aggressive.

Tuning this value is important for performance. For many applications, especially those that are memory-intensive like databases, it's better to keep the application's data in RAM and avoid swapping to disk, which is much slower.

## Usage

### Shell Script

The `set_swappiness.sh` script is a standalone utility that can be used to set the swappiness value on a Debian or RHEL-based system.

```bash
./scripts/set_swappiness.sh
```

### Ansible Playbook

The `set_swappiness.yml` playbook provides an Ansible-native way to configure swappiness.

```bash
ansible-playbook -i your_inventory playbooks/set_swappiness.yml
```