# Python redis counter

A very simple counter app that increments a value stored in redis every time it's run.

The redis server address is read from an environment variable `REDIS_ADDR`.

The app will read a password for redis from `REDIS_PASS`.

## Vagrant project

Included is a Vagrant project that builds 2 VMs. One is a redis server and the other is a client on which to run the app. The `REDIS_ADDR` and `REDIS_PASS` variables are pre-configured for the vagrant user on the client VM.

The project has Python3.7.3 installed without overwriting the system Python3 version. To use it you'll need to run `python3.7` instead of just `python3`

The application's required python modules will be installed for the `vagrant` user and the `Python3.7` version.

### Prerequisites

* Install VirtualBox - [instructions](https://www.virtualbox.org/wiki/Downloads)
* Install Vagrant - [instructions](https://www.vagrantup.com/downloads.html)

### Using Vagrant

* Build machines - `vagrant up`
* Connect to client/server VM as `vagrant` user - `vagrant ssh client|redis`
* Destroy machines - `vagrant destroy`
