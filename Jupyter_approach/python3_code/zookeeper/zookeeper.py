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

#plain and simple approach

filename="/opt/test/conf.json"  # make sure you change the path accordingly

jj=open(filename, 'r')

confile=jj.read()

data = json.loads(confile)

variable_manager.extra_vars=data

variable_manager.set_inventory(inventory)

#Playbooks

play_source_one = dict (
        name = "copy locally blueprint param_run_container.sh into usable files.",
        hosts = '{{ master }}',
        gather_facts = 'yes',
        tasks = [
                 dict(action=dict(module='copy',
		 		  dest='/opt/local_shift/zookeeper/param_run_container.sh',
                		  src='/opt/local_blueprint/blueprint_param_run_container.sh',
				  owner='tron',
		 		  group='tron'))
                 ])

playOne=Play().load(play_source_one, variable_manager=variable_manager, loader=loader)


play_source_two = dict (
        name = "copy blueprint run_image into modified files, specific to server.",
        hosts = '{{ master }}',
        gather_facts = 'yes',
        tasks = [
                 dict(action=dict(module='copy',
		 		  dest = '/opt/local_shift/zookeeper/param_run_container.sh',
                 		  src = '/opt/local_blueprint/blueprint_param_run_container.sh',
		 		  owner = 'tron',
		 		  group = 'tron'))
                 ])

playTwo=Play().load(play_source_two, variable_manager=variable_manager, loader=loader)


play_source_three = dict(
	name = "copy Dockerfile  on remotezookeeper host",
        hosts = '{{ minion4 }}',
        gather_facts = 'yes',
        tasks = [
                 dict(action=dict(module='copy',
		 		  dest = '/opt/remote_shift/zookeeper/',
                 		  src = ' /opt/local_images/zookeeper/Dockerfile',
		 		  owner = 'tron',
		 		  group = 'tron'))
                 ])
	
playThree = Play().load(play_source_three, variable_manager=variable_manager, loader=loader)



play_source_four = dict (
	name = "replace container image locally to build the image",
	hosts = '{{ master }}',
	gather_facts = 'yes',
	tasks = [
		 dict(action=dict(module = 'replace',
                 		  path = '/opt/local_shift/zookeeper/run_image.sh',
                 		  regexp = 'container',
		 		  replace = '{{ container }}' ))
				 
                 ])

playFour = Play().load(play_source_four, variable_manager=variable_manager, loader=loader)


play_source_five = dict (
	name = "replace to build the image",
	hosts = '{{ master }}',
	gather_facts = 'yes',
	tasks = [
		 dict(action=dict(module = 'replace',
                 		  path = '/opt/local_shift/zookeeper/run_image.sh',
                 		  regexp = 'tagimage',
		 		  replace = '{{ tagimage }}' ))
				 
                 ])

playFive = Play().load(play_source_five, variable_manager=variable_manager, loader=loader)


play_source_six = dict(
	name = "copy to remotezookeeper to build image",
        hosts = '{{ minion4 }}',
        gather_facts = 'yes',
        tasks = [
                 dict(action=dict(module='copy',
		 		  dest = '/opt/remote_shift/zookeeper/',
                 		  src = '/opt/local_shift/zookeeper/run_image.sh',
		 		  owner = 'tron',
		 		  group = 'tron'))
                 ])

playSix = Play().load(play_source_six, variable_manager=variable_manager, loader=loader)


play_source_seven = dict (
	name = " add new name container ",
	hosts = '{{ master }}',
	gather_facts = 'yes',
	tasks = [
		 dict(action=dict(module = 'replace',
                 		  path = '/opt/local_shift/zookeeper/param_run_container.sh',
                 		  regexp = 'namecontainer',
		 		  replace = '{{ namecontainer }}' ))
				 
                 ])

playSeven = Play().load(play_source_seven, variable_manager=variable_manager, loader=loader)


play_source_eight = dict (
	name = " add new name container ",
	hosts = '{{ master }}',
	gather_facts = 'yes',
	tasks = [
		 dict(action=dict(module = 'replace',
                 		  path = '/opt/local_shift/zookeeper/param_run_container.sh',
                 		  regexp = 'portcontainer',
		 		  replace = '{{ portontainer }}' ))
				 
                 ])

playEight = Play().load(play_source_eight, variable_manager=variable_manager, loader=loader)


play_source_nine = dict (
	name = " replace tag image ",
	hosts = '{{ master }}',
	gather_facts = 'yes',
	tasks = [
		 dict(action=dict(module = 'replace',
                 		  path = '/opt/local_shift/zookeeper/param_run_container.sh',
                 		  regexp = 'tagimage',
		 		  replace = '{{ tagimage }}' ))
				 
                 ])

playNine = Play().load(play_source_nine, variable_manager=variable_manager, loader=loader)


play_source_ten = dict (
	name = " replace storage amount size",
	hosts = '{{ master }}',
	gather_facts = 'yes',
	tasks = [
		 dict(action=dict(module = 'replace',
                 		  path = '/opt/local_shift/zookeeper/param_run_container.sh',
                 		  regexp = 'amountgb',
		 		  replace = '{{ amountgb }}' ))
				 
                 ])

playTen = Play().load(play_source_ten, variable_manager=variable_manager, loader=loader)


play_source_eleven = dict(
	name = "copy files from controller to remotezookeeper",
        hosts = '{{ minion4 }}',
        gather_facts = 'yes',
        tasks = [
                 dict(action=dict(module='copy',
		 		  dest = '/opt/remote_shift/zookeeper/',
                 		  src = '/opt/local_shift/zookeeper/param_run_container.sh',
		 		  owner = 'tron',
		 		  group = 'tron'))
                 ])

playEleven = Play().load(play_source_eleven, variable_manager=variable_manager, loader=loader)


play_source_twelve = dict (
     name = "build the image on remotezookeeper host",
     hosts = '{{ minion4 }}',
     gather_facts = 'yes',
     tasks = [
  		 dict(action=dict(module='shell', 
				  args='bash /opt/remote_shift/zookeeper/run_image.sh'), 
		      		  register='shell_out'),
  		 dict(action=dict(module='debug', 
				  args=dict(msg='{{shell_out.stdout}}')))

         ])

playTwelve = Play().load(play_source_twelve, variable_manager=variable_manager, loader=loader)


play_source_thirteen = dict (
     name = " wait a minute...lmao!",
     hosts = '{{ minion4 }}',
     gather_facts = 'yes',
     tasks = [
  		 dict(action=dict(module='shell', 
				  args='sleep 5'), 
		      		  register='shell_out'),
  		 dict(action=dict(module='debug', 
				  args=dict(msg='{{shell_out.stdout}}')))

         ])

playThirteen = Play().load(play_source_thirteen, variable_manager=variable_manager, loader=loader)

play_source_fourteen = dict (
     name = " start container on remotezookeeper host ",
     hosts = '{{ minion4 }}',
     gather_facts = 'yes',
     tasks = [
  		 dict(action=dict(module='shell', 
				  args='bash /opt/remote_shift/zookeeper/param_run_container.sh '), 
		      		  register='shell_out'),
  		 dict(action=dict(module='debug', 
				  args=dict(msg='{{shell_out.stdout}}')))

         ])

playFourteen = Play().load(play_source_fourteen, variable_manager=variable_manager, loader=loader)


#queue'em, and run'em

final = TaskQueueManager(
             inventory=inventory,
             variable_manager=variable_manager,
             loader=loader,
             options=options,
             passwords=passwords,
             stdout_callback='default',
           )

#
# this approach of running playbooks takes too long:
# resultz = [ playOne, playTwo,...]
# for result in resultz
#	run_playbooks = final.run(result)

resultOne = final.run(playOne)

resultTwo = final.run(playTwo)

resultThree = final.run(playThree)

resultFour = final.run(playFour)

resultFive = final.run(playFive)

resultSix = final.run(playSix)

resultSeven = final.run(playSeven)

resultEight = final.run(playEight)

resultNine = final.run(playNine)

resultTen = final.run(playTen)

resultEleven= final.run(playEleven)

resultTwelve = final.run(playTwelve)

resultThirteen = final.run(playThirteen)

resultFourteen = final.run(playFourteen)


