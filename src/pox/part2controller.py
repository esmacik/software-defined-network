# Edited by Erik Macik

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

    # add switch rules here
    # src and dst: ipv4
    # protocol: icmp
    # action: accept
    # Create rule and send to controller
    rule1 = of.ofp_flow_mod()
    rule1.match.dl_type = 0x800
    rule1.match.nw_proto = 1
    rule1.actions.append(of.ofp_action_output(port = of.OFPP_ALL))
    self.connection.send(rule1)

    # src and dst: any
    # protocol: arp
    # action: accept
    # Create rule and send to controller
    rule2 = of.ofp_flow_mod()
    rule2.match.dl_type = 0x0806
    rule2.actions.append(of.ofp_action_output(port = of.OFPP_ALL))
    self.connection.send(rule2)

    # src and dst: ipv4
    # protocol: -
    # action: drop
    # Create rule and send to controller
    rule3 = of.ofp_flow_mod()
    rule3.match.dl_type = 0x800
    self.connection.send(rule3)

  def _handle_PacketIn (self, event):
    """
    Packets not handled by the router rules will be
    forwarded to this method to be handled by the controller
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    print ("Unhandled packet :" + str(packet.dump()))

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
