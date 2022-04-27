Erik Macik
Assignment 4 - SDN
Running instructions

To run part 1 code:
1. Install mininet and pox controller.
2. In Ubuntu VM, run the command "sudo python part1.py".
3. Run the commands "pingall", "dump", and "iperf".

To run part2 code:
1. Install mininet and pox controller.
2. Move the part2controller.py file into the directory ~/pox/ext/
3. In one terminal, run the command "./pox.py part2controller"
4. In another teminal, run the command "sudo python part2.py"
5. Run the commands "pingall", "iperf", and "dpctl dump-flows".

DEPLOYING POX CONTROLLER
In short, I deployed the controller to pox by putting it inside
the ext directory inside of the pox repository from GitHub, and ran
the pox controller with the command “./pox.py part2controller”. After
the controller was up and running, I then ran the provided topology
file with “sudo python part2.py”.