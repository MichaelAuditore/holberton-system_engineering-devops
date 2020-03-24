### 0x0B. SSH
### General

    What is a server
    Where servers usually live
    What is SSH
    How to create an SSH RSA key pair
    How to connect to a remote host using an SSH RSA key pair
    The advantage of using #!/usr/bin/env bash instead of /bin/bash

 0. Use a private key

    Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

 1. Create an SSH key pair

    Write a Bash script that creates an RSA key pair.

 2. Client configuration file

    Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client,
    let’s configure it to our needs so that you can connect to a server without typing a password.
    Share your SSH client configuration in your answer file.

    Requirements:

      Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
      Your SSH client configuration must be configured to refuse to authenticate using a password

 3. Let me in!

      Now that you have successfully connected to your server, we would also like to join the party.

      Add the SSH public key below to your server so that we can connect using the ubuntu user.

 4. Client configuration file (w/ Puppet) #advanced

    Let’s practice using Puppet to make changes to our configuration file.
    Just as in the previous configuration file task,
    we’d like you to set up your client SSH configuration
    file so that you can connect to a server without typing a password.

    Requirements:

      Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
      Your SSH client configuration must be configured to refuse to authenticate using a password