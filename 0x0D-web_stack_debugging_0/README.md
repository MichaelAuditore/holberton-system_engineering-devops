### 0x0D. Web stack debugging #0
    The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

    Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

    In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to	a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

    Let’s start with a very simple example. My server must:

    have a copy of the /etc/passwd file in /tmp
    have a file named /tmp/isworking containing the string OK

    Let’s pretend that without these 2 elements, my web application cannot work.

    Let’s go through this example and fix the server.

   0. Give me a page!

    Be sure to read the Docker concept page.
    In  this first debugging project, you will need to get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it.