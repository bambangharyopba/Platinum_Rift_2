import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]

zone_link=[[] for i in range(link_count)]
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    
    zone_link[zone_1].append(zone_2)
    zone_link[zone_2].append(zone_1)


platinum_each_zone = [False for i in range(zone_id)]
# game loop
while True:
    a = 0
    b = 0
    no_of_pods=[]
    pod_zone = []
    pod_move=[]
    pod_link=[]

    
    my_platinum = int(input())  # your available Platinum
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        if visible == 1 and platinum_each_zone == False:
            platinum_each_zone[z_id] = platinum
            
            
        if my_id == 0 :
            if pods_p0 > 0:
                pod_zone.append(z_id)
                no_of_pods.append(pods_p0)
        else:
            if pods_p1 > 0:
                pod_zone.append(z_id)
                no_of_pods.append(pods_p1)
    
    for i in pod_zone:
        pod_link.append(len(zone_link[i]))
        
    #for i in pod_zone:
    #    for j in range(len(zone_link[i])):
    #        if a < platinum_each_zone[zone_link[i][j]]:
    #            a = platinum_each_zone[zone_link[i][j]]
    #            b = j
    #    pod_move.append(b)
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    printan = ""
    for i in range(len(pod_zone)):
        for j in range(pod_link[i]):
            if no_of_pods[i] > 1:
                printan+= str(no_of_pods[i]//pod_link[i]) + " " + str(pod_zone[i]) + " " + str(zone_link[pod_zone[i]][j]) + " "
            else:
                printan+= "1" + " " + str(pod_zone[i]) + " " + str(zone_link[pod_zone[i]][j]) + " "
    
    print(printan)
    print("WAIT")