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

2. Import the function to find a fighter

   .. code-block:: python

      from ufcpy import find_fighter_by_fullname

3. Call the function and define it.

   .. code-block:: python

      fighter = find_fighter_by_fullname('Jon Jones')

4. Use the class returned via the previous function to return anything about the specified fighter

   .. code-block:: python

      fighter.nickname
      # Returns 'Bones'

===================================
Example
===================================

.. code-block:: python
   
   from ufcpy import find_fighter_by_fullname

   f = find_fighter_by_fullname('Jon Jones')

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

.. autoclass:: ufcpy.Champion
   :members:
   :show-inheritance:

===================================
Exception Classes
===================================

.. autoclass:: ufcpy.UFCPyError
   :members: