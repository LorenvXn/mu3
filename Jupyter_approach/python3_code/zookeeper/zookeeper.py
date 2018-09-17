#!/usr/bin/python3

import os, sys
import argparse
import json

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.inventory.manager import InventoryManager
from ansible.utils.vars import load_extra_vars
from ansible.executor.task_queue_manager import TaskQueueManager

from ansible.playbook.helpers import load_list_of_tasks


Options = namedtuple('Options',
                   ['listtags', 
		    'listtasks', 
                    'listhosts', 
 		    'syntax', 
                    'connection',
		    'module_path',
		    'forks', 
		    'remote_user', 
                    'private_key_file', 
		    'ssh_common_args',
		    'ssh_extra_args', 
		    'sftp_extra_args', 
                    'scp_extra_args', 
		    'become', 
                    'become_method', 
                    'become_user', 
                    'verbosity', 
                    'check',
                    'diff'
                   ])


loader = DataLoader()
hosts_path = InventoryManager(loader=loader, sources="/etc/ansible/hosts")
variable_manager = VariableManager(loader=loader, inventory=hosts_path)


inventory=hosts_path

options = Options(listtags=False, 
		listtasks=False, 
		listhosts=False, 
 		syntax=False, 
		connection='ssh', 
		module_path=None, 
		forks=100, 
		remote_user='tron', 
	        private_key_file=None, 
		ssh_common_args=None, 
		ssh_extra_args=None, 
	        sftp_extra_args=None, 
		scp_extra_args=None, 
		become=True, 
		become_method='sudo', 
	        become_user='tron', 
		verbosity=None, 
		check=False, 
		diff=False)

passwords = {}


filename="/opt/test/conf.json"  # make sure you change the path accordingly

jj=open(filename, 'r')

confile=jj.read()

data = json.loads(confile)

variable_manager.extra_vars=data

variable_manager.set_inventory(inventory)

