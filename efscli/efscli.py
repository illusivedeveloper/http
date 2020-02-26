#!/usr/bin/python3

import sys
import json
import http.client
import argparse
import os
import logging
from commands import *
from api import *
"""
def efsctl_query(method, url, headers, content):
    conn.request(method, url, content, headers)

def efsctl_fs_create():
    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description='''FS create.''',
                usage="create name=NAME --options=OPTIONS")

    parser.add_argument('name', help='FS name.')            
    parser.add_argument('--options', '-o', help='FS options.')

    args = parser.parse_args(sys.argv[3:])
    name = args.name
    options = args.options

    method = "PUT"
    url = "/fs/create/"
    headers = {}

    options_list = []
    fs_create_data = {}
    fs_create_options = {}
    content = {}
    
    fs_create_request = {"type" : "fs_create", "id" : "0", "session_id" : "0"}

    fs_create_data["fs-name"] = name
    
    if options != None:
        option_list = options.split(',')
        for option_token in option_list:
            option = option_token.split(':')
            key = option[0]
            val = option[1]
            fs_create_options[key] = val

    fs_create_data["fs-option"] = fs_create_options

    fs_create_request["request"] = [fs_create_data]

    print(fs_create_request)
    content = json.dumps(fs_create_request).encode('utf-8')


    efsctl_query(method, url, headers, content)
    response = conn.getresponse()
    fs_create_response = response.read()
    print(fs_create_response)
    #fs_create_response_data = json.dumps(fs_create_response).decode('utf-8')

def efsctl_fs_delete():
    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description='''FS delete.''',
                usage="delete name=NAME")

    parser.add_argument('name', help='FS name.')

    args = parser.parse_args(sys.argv[3:])
    name = args.name

    method = "DELETE"
    url = "/fs/delete/"
    headers = {}

    fs_delete_data = {}
    content = {}

    fs_delete_request = {"type" : "fs_delete", "id" : "0", "session_id" : "0"}

    fs_delete_data["fs-name"] = name
    fs_delete_request["request"] = [fs_delete_data]

    content = json.dumps(fs_delete_request).encode('utf-8')

    efsctl_query(method, url, headers, content)
    fs_delete_response = conn.getresponse()
    #print(json.load(fs_delete_response))

def efsctl_fs(command):
    command_switcher = \
            {"create" : efsctl_fs_create,
             "delete" : efsctl_fs_delete
            }
    fs_command = command_switcher.get(command)
    if fs_command != None:
        fs_command()
    else:
        parser.print_help()

def efsctl_export(command):
    command_switcher = \
            {"create" : efsctl_export_create,
             "delete" : efsctl_export_delete
            }
    export_command = command_switcher.get(command)
    if export_command != None:
        export_command()
    else:
        parser.print_help()


def efsctl_execute():
    controller = args.controller
    command = args.command
    controller_switcher = \
            {
                "fs" : efsctl_fs,
                "export" : efsctl_export
            }
    controller = controller_switcher.get(controller)
    if controller != None:
        controller(command)
    else:
        parser.print_help()
"""

def main(argv):
    """
    Parse and execute command line to obtain command structure.
    Execute the CLI
    """
    cli_path = os.path.realpath(argv[0])
    sys.path.append(os.path.join(os.path.dirname(cli_path), '..', '..'))

    try:
        command = CommandFactory.get_command(argv[1:])
        #TODO: Implement efsapiclient
        client = EfsApiClient()
        response = client.call(command)
        rc = response.rc()
        if rc != 0:
            sys.stdout.write('error(%d): ' %rc)
            sys.stdout.write('%s\n' %response.output())
            return rc

    except Exception as exception:
        sys.stderr.write('%s\n' %exception)
        #Log.error(traceback.format_exc())
        # TODO - Extract rc from exception
        return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv)) 