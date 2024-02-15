import sys
from os.path import dirname
sys.path.append(".")
from mgtoolkit import *
from mgtoolkit.library import Metagraph, ConditionalMetagraph, Edge
import json
import os
from nodes import *
from utils import *
from collections import *
import itertools
import pandas as pd
import openpyxl
from datetime import datetime
import matplotlib.pyplot as plt

def get_combination_pairs(arr):
    n = len(arr)
    combinations = []
    result = []
    for size in range(1, n + 1):
        for i in range(n - size + 1):
            combinations.append(arr[i:i+size])
    for i in range(len(combinations)):
        for j in range(n):
            if i != j:
                result.append([combinations[i], [arr[j]]])
    return result

def get_json_files(folder_path):
    json_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files

# Example usage
path_to_json = '../DATA'
json_files = get_json_files(path_to_json)

# Print the list of JSON files
for file in json_files:
    print(file)


#json_files = [pos_json for pos_json in os.listdir(
#    path_to_json) if pos_json.endswith('.json')]
ignore_files = ["JP Morgan Breach.json",
                "FIN13 Case 2.json", "Gootloader.json", "Target Breach.json", "Hancitor DLL.json", "NotPetya.json", "Ragnar Locker.json"]
big_files = ["FIN13 Case 1.json", "Cobalt Kitty Campaign.json", "apt-chaining-vulnerabilities.json", "SolarWinds.json", "Conti Ransomware.json", "WhisperGate.json", "IcedID.json", "cleared-defense-contractor-networks.json"]

for i in range(len(json_files)):
    if (i<78): #a quick hack to ignore incorrect format files
        file = json_files[i]
        print("Building metagraph " + str(i) + " out of " + str(len(json_files)))
        print(file) 
        f = open(file)
        data = json.load(f)

        try:
            objects = data["objects"]
        except KeyError:
            print(file + " may not have correct format!!! Skip")    
        
        print(len(objects))
        
        # Create nodes from json file

        nodeById, allNodes = convertAllToNodes(objects)

        # Create list for metagraph and add "attack-action", "attack-asset" and "STIX Common Properties" node to the list
        generating_set = set()
        for node in allNodes["actions"]:
            generating_set.add(node)
        # Create metagraph
        mg = Metagraph(generating_set)

        elementsSum = 0
        for k, v in allNodes.items():
            if k != 'operators':
                elementsSum += len(v)

        flow_dict = defaultdict(list)
        
        # set outNodes for each operator
        for node in allNodes["operators"]:
            outnodes = []
            for ref in node.effect_refs:
                for outNode in generating_set:
                    if outNode.getId() == ref:
                        outnodes.append(outNode)
                node.setOutNodes(outnodes)
                
        # Generate edges for the metagraph
        mg, flow_dict = createAttackEdge(mg, generating_set, nodeById, flow_dict)

        mg, flow_dict = createOperatorEdge(mg, allNodes["operators"], flow_dict)

        for node in allNodes["operators"]:
            print(node.inNodes)
        # from relationships
        mg, flow_dict = createRelationshipEdge(
            mg, allNodes["relationships"], nodeById, flow_dict)

        # metagraph adjacency matrix and incidence
        A = mg.adjacency_matrix()
        I = mg.incidence_matrix()

        combination_pairs = get_combination_pairs(list(generating_set))

        print(mg.nodes)
        print(mg.edges)
""" 
        number_of_metapaths = 0
        avg_edge_list = 0
        avg_include_nodes = 0
        metapaths_set = set()
        longest_metapath = float('-inf')
        shortest_metapath = float('inf')
        freq_nodes = {}
        for pair in combination_pairs:
            if ((set(pair[0]) != set(pair[1])) and (len(pair[0])>0) and (len(pair[1])>0)):
                metapaths = mg.get_all_metapaths_from(set(pair[0]), set(pair[1]))
                if metapaths != None and len(metapaths) > 0:
                    metapaths_set.update(metapaths)
                    for metapath in metapaths:
                        number_of_metapaths += 1
                        longest_metapath = max(longest_metapath, len(metapath.edge_list))
                        shortest_metapath = min(shortest_metapath, len(metapath.edge_list))
                        included_nodes = set()
                        avg_edge_list += len(metapath.edge_list)
                        for edge in metapath.edge_list:
                            for tmp_node in edge.invertex.union(edge.outvertex):
                                if tmp_node not in freq_nodes:
                                    freq_nodes[tmp_node] = 1
                                else:
                                    freq_nodes[tmp_node]+=1
                                included_nodes.add(tmp_node)
                        avg_include_nodes += len(included_nodes)
        sorted_tuples = sorted(freq_nodes.items(), key=lambda x: x[1], reverse=True)
        number_of_metapaths = len(metapaths_set)
        avg_include_nodes = avg_include_nodes//number_of_metapaths
        avg_edge_list = avg_edge_list//number_of_metapaths
        x.append(len(mg.edges))
        y.append(sorted_tuples[0][1])
        print('number of nodes:', len(generating_set))
        print('number of edges:', len(mg.edges))
        print('Number of metapaths:', number_of_metapaths)
        print('Average number of include nodes:', avg_include_nodes)
        print('Average path length:', avg_edge_list)
        print('Highest degree nodes:', mg.get_most_degree_nodes())
        print('Highest rank nodes:', mg.get_most_rank_nodes())
        print(f'Attackflow {file[:-5]} has {len(generating_set)} nodes, {len(mg.edges)} edges, \\\
              {number_of_metapaths} metapaths (longest: {longest_metapath}, shortest: {shortest_metapath}), the average paths length is \\\
              {avg_edge_list}, the nodes with highest degree is {mg.get_most_degree_nodes()}, the nodes with highest rank is {mg.get_most_rank_nodes()}.')
"""