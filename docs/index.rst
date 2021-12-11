Welcome to UFCPy!
===================================
A fast and easy way to access the UFC roster

.. toctree::
   :maxdepth: 2
   :caption: Contents:

===================================
Features
===================================
* Scrapes everything off the UFC website
* Synchronous
* Easy

===================================
First Steps
===================================
1. Install the package

   .. code-block:: bash

      python3 -m pip install ufcpy

2. Import the package

   .. code-block:: python

      from ufcpy import Fighter

3. Make a class and get a fighter with their name

   .. code-block:: python

      fighter = Fighter()
      fighter.get_fighter('Conor Mcgregor')

4. Use the class to return anything about the specified fighter

   .. code-block:: python

      fighter.nickname

===================================
Example
===================================

.. code-block:: python
   
   from ufcpy import Fighter

   f = Fighter()
   f.get_fighter('Jon Jones')

   print(f.nickname, f.hometown)

===================================
Classes
===================================

-----------------------------------
Fighter
-----------------------------------

.. autoclass:: ufcpy.Fighter
   :members:
   :show-inheritance:

===================================
Exception Classes
===================================

.. autoclass:: ufcpy.UFCPyError
   :members: