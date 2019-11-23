#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    runner.py
# @author  Lena Kalleske
# @author  Daniel Krajzewicz
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @date    2009-03-26
# @version $Id$

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random

# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa


def generate_routefile():
    random.seed(42)  # make tests reproducible
    N = 3600  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    with open("quickstart.rou.xml", "w") as routes:
        print("""<routes>
        <vType accel="3.0" decel="6.0" id="CarA" length="5.0" minGap="2.5" maxSpeed="50.0" sigma="0.5" />
  <vType accel="2.0" decel="6.0" id="CarB" length="7.5" minGap="2.5" maxSpeed="50.0" sigma="0.5" />
  <vType accel="1.0" decel="5.0" id="CarC" length="5.0" minGap="2.5" maxSpeed="40.0" sigma="0.5" />
  <vType accel="1.0" decel="5.0" id="CarD" length="7.5" minGap="2.5" maxSpeed="30.0" sigma="0.5" />
  <route id="route01" edges="gneE2 gneE3 "/>
  <route id="route02" edges="-gneE3 -gneE2 "/>""", file=routes)


        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="veh%i" type="CarA" route="route01" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="veh%i" type="CarB" route="route02" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="veh%i" type="CarC" route="route02" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="veh%i" type="CarD" route="route01" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
        print("</routes>", file=routes)

# The program looks like this
#    <tlLogic id="0" type="static" programID="0" offset="0">
# the locations of the tls are      NESW
#        <phase duration="31" state="GrGr"/>
#        <phase duration="6"  state="yryr"/>
#        <phase duration="31" state="rGrG"/>
#        <phase duration="6"  state="ryry"/>
#    </tlLogic>


def run():
    """execute the TraCI control loop"""
    step = 0
    # we start with phase 2 where EW has green
    # traci.trafficlight.setPhase("0", 2)
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        # if traci.trafficlight.getPhase("0") == 2:
        #     # we are not already switching
        #     if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
        #         # there is a vehicle from the north, switch
        #         traci.trafficlight.setPhase("0", 3)
        #     else:
        #         # otherwise try to keep green for EW
        #         traci.trafficlight.setPhase("0", 2)
        step += 1
    traci.close()
    sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    generate_routefile()
    
    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "quickstart.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()
