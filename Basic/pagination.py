import asana
import csv
import sys

outputdir = ''
outputfilename = 'asana-export.csv'

personal_access_token = sys.argv[1] #taken from command line
client = asana.Client.access_token(personal_access_token) #start session
me = client.users.me() #get user info
workspace = me['workspaces'][0] #set main workspace
print('Initialising Asana session for ' + me['name'] + ' in workspace: ' + workspace['name'])
projects = client.projects.find_by_workspace(workspace['gid'], iterator_type=None) #find projects within workspace
tasklist = []

print('\nLooping through all the tasks within the projects...\n')
for project in projects:
    print(project['name'])
    #opt_expand delivers all attributes (not a compact view) for each field    
    tasks = client.tasks.find_by_project(project['gid'], {"opt_expand":"name, \
