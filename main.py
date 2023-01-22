#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Project Name: Email Validator
# Author: [@zanzanimax]
# Copyright: [2023]
# Licensed under the [BSD License]


import argparse
import termcolor
import pyfiglet
import os
import time
from validate_email import validate_email
from tqdm import tqdm
from colorama import Fore, init

# Initializing colorama
init() 

# Define color variables
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
green = Fore.LIGHTGREEN_EX

def banner():

    """
    Prints a banner to the terminal
    """
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format("Email Checker", font="slant", justify="center")
    print(cyan + my_banner)
    print(f"\t\t{cyan}[ {green}Created By ZANZAN {white}] - [V 1.0] @zanzanimax \n")


def check_email(email, output_file):

    """
    Check if the provided email is valid and write it to the output file if it is

    :param email: The email address to check
    :type email: str
    :param output_file: The file to write valid emails to
    :type output_file: str
    :return: True if the email is valid, False otherwise
    :rtype: bool
    """

    if validate_email(email, verify=True):
        with open(output_file, 'a') as f:
            f.write(email+'\n')
        print(f'{green}[*] [VALID] - {email}')
        return True
    else:
        print(f'{red}[!] [NOT VALID] - {email}')
        return False

def main():
    input_file = input("[?] Enter input file Name or email addresses separated by commas: ")
    emails = input_file.split(",")
    if len(emails)>1:
        for email in emails:
            check_email(email.strip(), 'valid.tx')
    elif validate_email(input_file):
        check_email(input_file, 'valid.txt')
    else:
        output_file = input("[?] Enter output file Name: ")
        delay = int(input("[?] Enter delay in seconds: "))
        valid_emails = 0
        invalid_emails = 0
        try:
            with open(input_file) as f:
                for email in tqdm(f.readlines()):
                    if check_email(email.strip(), output_file):
                        valid_emails += 1
                    else:
                        invalid_emails += 1
                    if delay > 0:
                        print(f'{Fore.WHITE}Waiting for {delay} seconds')
                        time.sleep(delay)

        except FileNotFoundError:
            print(f"{input_file} not found")
        except Exception as e:
            print("An error occurred: ",e)

        print(f'-----------------------------------')
        print(f'{green}[*] [VALID] [{valid_emails}')
        print(f'{red}[!] [NOT VALID] [{invalid_emails}]')
        print(f'-----------------------------------')

if __name__ == '__main__':
    main()
