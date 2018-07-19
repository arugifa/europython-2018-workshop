# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "bootstrap.sh"

  # Create a private network, to access to the VM from the machine host.
  # IP address chosen randomly (taken from the Vagrant tutorial in fact).
  config.vm.network "private_network", ip: "192.168.50.4"
end
