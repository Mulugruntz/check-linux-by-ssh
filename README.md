io-shinken-checks-linux
=======================

Specifics checks for linux based on pure ssh polling, with nothing to install on the target


Dependencies
======================
 * python
 * python-paramiko




Connexion
======================
This check is for checking the SSH connexion to the distant server. This is done by the `check_ssh_connexion.py` script.

[//]: # (begin generate_help: check_ssh_connexion.py)
### Usage
```
Usage: check_ssh_connexion.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -w WARNING, --warning=WARNING
                        Warning value for physical used memory. In percent.
                        Default : 75%
  -c CRITICAL, --critical=CRITICAL
                        Critical value for physical used memory. In percent.
                        Must be superior to warning value. Default : 90%

```
[//]: # (end generate_help)

###Example
```shell
check_ssh_connexion.py -H localhost -u shinken
```


Memory
======================
The Memory check is done by the `check_memory_by_ssh.py` script.

[//]: # (begin generate_help: check_memory_by_ssh.py)
### Usage
```
Usage: check_memory_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -m, --measurement     Measurement in absolute value of the memory behavior.
                        Absolute value currently can not be used as a check
  -s, --swap            Enable swap value measurement. Swap value currently
                        can not be used as a check
  -w WARNING, --warning=WARNING
                        Warning value for physical used memory. In percent.
                        Default : 75%
  -c CRITICAL, --critical=CRITICAL
                        Critical value for physical used memory. In percent.
                        Must be superior to warning value. Default : 90%

```
[//]: # (end generate_help)

### Example
```shell
check_memory_by_ssh.py -H localhost -u shinken -w "75%" -c "90%"
```




Uptime
======================
The Uptime check is done by the `check_uptime_by_ssh.py` script. It only take a `-c` option, the number of second : below it's critical, higher it's ok. By default it's 3600s.

[//]: # (begin generate_help: check_uptime_by_ssh.py)
### Usage
```
Usage: check_uptime_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -c CRITICAL, --critical=CRITICAL
                        Critical value for uptime in seconds. Less means
                        critical error. Default : 3600

```
[//]: # (end generate_help)

### Example
```shell
check_uptime_by_ssh.py -H localhost -u shinken -c 3600
```



NTP Sync
======================
The NTP sync check is done by the `check_ntp_sync_by_ssh.py` script. It will go in warning if no ntp server is the reference, and -w/-c options will set the maximum delay values.

[//]: # (begin generate_help: check_ntp_sync_by_ssh.py)
### Usage
```
Usage: check_ntp_sync_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -w WARNING, --warning=WARNING
                        Warning delay for ntp, like 10. couple delay,offset
                        value for chrony 0.100,0.0025
  -c CRITICAL, --critical=CRITICAL
                        Warning delay for ntp, like 10. couple delay,offset
                        value for chrony 0.150,0.005
  -C, --chrony          check Chrony instead of ntpd
  -n NTPQ, --ntpq=NTPQ  remote ntpq bianry path

```
[//]: # (end generate_help)

### Example
```shell
check_ntp_sync_by_ssh.py -H localhost -u shinken -w 10 -c 60
```


Processes (Memory)
=====================
Look at the memory of a process, or a pack of processes. It's done by the `check_processes_by_ssh` script

[//]: # (begin generate_help: check_processes_by_ssh.py)
### Usage
```
Usage: check_processes_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -w WARNING, --warning=WARNING
                        Warning value for RSS used memory. In MB. Default :
                        100
  -c CRITICAL, --critical=CRITICAL
                        Critical value for RSS used memory. In MB. Must be
                        superior to warning value. Default : 200
  -C COMMAND, --command=COMMAND
                        Command name to match for the check
  -S, --sum             Sum all consomtion of matched processes for the check

```
[//]: # (end generate_help)

### Examples
* Look that the sum of all *chrome* processes are not over 700 or 800MB
  ```shell
  check_processes_by_ssh.py -H localhost -u shinken -C chrome -w 700 -c 800 -S
  ```

* Look for each *chrome* processe if they are not over 100 or 200MB
  ```shell
  check_processes_by_ssh.py -H localhost -u shinken -C chrome -w 100 -c 200
  ```
  
* Look for all process, and warn if one is over 100/200MB
  ```shell
  check_processes_by_ssh.py -H localhost -u shinken -w 100 -c 200
  ``` 


Disks
======================
The Disks check is done by the `check_disks_by_ssh.py` script.

[//]: # (begin generate_help: check_disks_by_ssh.py)
### Usage
```
Usage: check_disks_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -t MODNAME            Check to load
  -l                    List all checks available
  -w WARNING, --warning=WARNING
                        Warning value for physical used memory. In percent.
                        Default : 75%
  -c CRITICAL, --critical=CRITICAL
                        Critical value for physical used memory. In percent.
                        Must be superior to warning value. Default : 90%
  -m MOUNTS, --mount-points=MOUNTS
                        comma separated list of mountpoints to check. Default
                        all mount points except if mounted in /dev, /sys and
                        /run
  -U UNIT, --unit=UNIT  Unit of Disk Space. B, KB, GB, TB. Default : B

```
[//]: # (end generate_help)

### Example
```shell
check_disks_by_ssh.py -H localhost -u shinken -w "75%" -c "90%"
```



Load average
=====================
The load average values are checks with the `check_load_average_by_ssh.py` script.
There are two modes : strict values, and cpu based values. default : strict)

[//]: # (begin generate_help: check_load_average_by_ssh.py)
### Usage
```
Usage: check_load_average_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -w WARNING, --warning=WARNING
                        Warning value for load average, as 3 values, for
                        1m,5m,15m. Default : 1,1,1
  -c CRITICAL, --critical=CRITICAL
                        Critical value for load average, as 3 values, for
                        1m,5m,15m. Default : 2,2,2
  -C, --cpu-based       Set the warning/critical number of cpu based values.
                        For example 1,1,1 will warn if the load if over the
                        number of CPUs. Default : False

```
[//]: # (end generate_help)

### Examples
* Will warn if the load average is higher than 1 or 2
  ```shell
  check_load_average_by_ssh.py -H localhost -u shinken -w 1,1,1 -c 2,2,2
  ```

* Will warn if the load average is higher than 1*nb_cpus or 2*nb_cpus
  ```shell
  check_load_average_by_ssh.py -H localhost -u shinken -w 1,1,1 -c 2,2,2 -C
  ```
  
  
CPU activities
====================
The cpu states are checks by the `check_cpu_stats_by_ssh.py` script. There is no warning or critical values need here.

[//]: # (begin generate_help: check_cpu_stats_by_ssh.py)
### Usage
```
Usage: check_cpu_stats_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void

```
[//]: # (end generate_help)

### Example
```shell
check_cpu_stats_by_ssh.py -H localhost -u shinken
```



DISKS activities
===================
The disks I/O are checked by the `check_disks_stats_by_ssh.py`. No warning nor critical values need.

[//]: # (begin generate_help: check_disks_stats_by_ssh.py)
### Usage
```
Usage: check_disks_stats_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -t MODNAME            Check to load
  -l                    List all checks available

```
[//]: # (end generate_help)

### Example
```shell
check_disks_stats_by_ssh.py -H localhost -u shinken
```



TCP states
==================
The TCP states are checked by the `check_tcp_states_by_ssh.py` plugin. No warning nor critical values need.

[//]: # (begin generate_help: check_tcp_states_by_ssh.py)
### Usage
```
Usage: check_tcp_states_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void

```
[//]: # (end generate_help)

### Example
```shell
check_tcp_states_by_ssh.py - H localhost -u shinken
```


KERNEL stats
==================
The KERNEL states are checked by the `check_kernel_stats_by_ssh.py` script. No warning nor critical values need.

[//]: # (begin generate_help: check_kernel_stats_by_ssh.py)
### Usage
```
Usage: check_kernel_stats_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void

```
[//]: # (end generate_help)

### Example
```shell
check_kernel_stats_by_ssh.py - H localhost -u shinken
```


NFS stats
==================
The NFS states are checked by the `check_nfs_stats_by_ssh.py` plugin. No warning nor critical values need.

[//]: # (begin generate_help: check_nfs_stats_by_ssh.py)
### Usage
```
Usage: check_nfs_stats_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -w WARNING, --warning=WARNING
                        Warning value for physical used memory. In percent.
                        Default : 75%
  -c CRITICAL, --critical=CRITICAL
                        Critical value for physical used memory. In percent.
                        Must be superior to warning value. Default : 90%

```
[//]: # (end generate_help)

### Example
```shell
check_nfs_stats_by_ssh.py - H localhost -u shinken
```



Interface activities
=================
The network activity is checked by the `check_net_stats_by_ssh.py` plugin. No need for warning nor critical.

[//]: # (begin generate_help: check_net_stats_by_ssh.py)
### Usage
```
Usage: check_net_stats_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -w WARNING, --warning=WARNING
                        Warning value for physical used memory. In percent.
                        Default : 75%
  -c CRITICAL, --critical=CRITICAL
                        Critical value for physical used memory. In percent.
                        Must be superior to warning value. Default : 90%
  -e EXCLUDE, --exclude=EXCLUDE
                        Interfaces to exclude. Can appear several time.

```
[//]: # (end generate_help)

### Example
```shell
check_net_stats_by_ssh.py - H localhost -u shinken
```

Read Only file systems
==================
The file system mount are checks. If a FS is in read only, it will raise a critical error. This is done by the `check_ro_filesystem_by_ssh.py` script.

[//]: # (begin generate_help: check_ro_filesystem_by_ssh.py)
### Usage
```
Usage: check_ro_filesystem_by_ssh.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -H HOSTNAME, --hostname=HOSTNAME
                        Hostname to connect to
  -p PORT, --port=PORT  SSH port to connect to. Default : 22
  -i SSH_KEY_FILE, --ssh-key=SSH_KEY_FILE
                        SSH key file to use. By default will take
                        ~/.ssh/id_rsa.
  -u USER, --user=USER  remote use to use. By default shinken.
  -P PASSPHRASE, --passphrase=PASSPHRASE
                        SSH key passphrase. By default will use void
  -e EXCLUDE, --exclude=EXCLUDE
                        Mount point to exclude. Can appear several time.
  -w WARNING, --warning=WARNING
                        Warning value for physical used memory. In percent.
                        Default : 75%
  -c CRITICAL, --critical=CRITICAL
                        Critical value for physical used memory. In percent.
                        Must be superior to warning value. Default : 90%

```
[//]: # (end generate_help)

### Example
```shell
check_ro_filesystem_by_ssh.py - H localhost -u shinken
```
