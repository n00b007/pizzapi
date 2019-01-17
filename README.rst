pizzapy
=======

Disclaimer
-----------
This is my fork of https://github.com/Magicjarvis/pizzapi
It has been modified to add a new package called code_for_pizza.

There are modifications to the original code, sorry! in advance for the messy documentation.

Setup
-----

1. install python3
2. download this repository
3. install the requirements of the repository `pip install -r requirements.txt`
4. start a python3 interpreter inside of the folder called pizzapy, so it will be in the PYTHONPATH
5. import pizzapy and if it works, great !


Description
-----------

This is a Python wrapper for the Dominos Pizza API.

It's a port of `the pizzapi node.js module <https://github.com/RIAEvangelist/node-dominos-pizza-api>`_ written by `RIAEvangelist <https://github.com/RIAEvangelist>`_.

Quick Start
-----------

First go to code_for_pizza/dominos_test_order.py and change the details in Customer to your details.

The details already entered in the python file are a sample and do not actually work.

Just replace the details inside the ``Customer`` block to yours.

.. code-block:: python

    customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111', '700 Pennsylvania Avenue NW, Washington, DC, 20408')

.. code-block:: python3
    
    customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111', '700 Pennsylvania Avenue NW, Washington, DC, 20408')

Now switch over to code_for_pizza/order_pizza.py and add your github user_id and password.

.. code-block:: python3

    g = Github('your_username','your_password')

Then simply type the following command from the pizzapy folder, which is one folder up:

.. code-block:: bash

    python3 code_for_pizza/order_pizza.py

And just like that it should place the order for you !

Optional Step:
--------------

1. You can put the user_id and password in a config file and read it programmatically from the python script,
than just hardcoding it.

2. Integrate twilio's API to send an SMS alert when an order is placed.
