.. image:: https://cdn.discordapp.com/emojis/1140027508427857960.webp?size=80&quality=lossless
    :target: https://cdn.discordapp.com/emojis/1140027508427857960.webp?size=80&quality=lossless

Cython Tutorial: Boosting Python Performance with C
===================================================
.. image:: https://img.shields.io/pypi/v/cython.svg
    :target: https://pypi.python.org/pypi/cython
.. image:: https://img.shields.io/pypi/pyversions/cython.svg
    :target: https://pypi.python.org/pypi/cython
.. image:: https://img.shields.io/pypi/l/cython.svg
    :target: https://pypi.python.org/pypi/cython
.. image:: https://img.shields.io/pypi/dm/cython.svg
    :target: https://pypi.python.org/pypi/cython

Introduction
------------

Welcome to the Cython Tutorial! If you're new to the world of Python or even if you're an experienced Python developer, you might have heard about Cython and its potential to significantly boost Python's performance. In this tutorial, we'll explore what Cython is, how it relates to C, and why it's relevant for Python developers.

What is Cython?
---------------

Cython is an open-source programming language and compiler that makes it easy to write Python code that runs as fast as C. It's designed to bridge the gap between Python's ease of use and C's performance. Cython allows you to write code using Python syntax while taking advantage of C's performance optimizations. This makes it an attractive choice for tasks that require high performance, such as numerical computations, scientific simulations, and more.

Python and C: A Powerful Combination
-------------------------------------

Python is a high-level programming language known for its simplicity and readability. However, it's an interpreted language, which can sometimes lead to slower execution speeds, especially for computationally intensive tasks. C, on the other hand, is a low-level programming language that is compiled directly into machine code, resulting in faster execution speeds.

Cython bridges this gap by allowing you to write code that looks like Python but gets compiled into C, providing the best of both worlds. This combination enables Python developers to achieve performance similar to C while maintaining the ease of use and readability of Python.

Proving the Concept: Performance Comparison
--------------------------------------------

To illustrate the performance benefits of using Cython, I've prepared a sample Python program that calculates Fibonacci numbers. I've implemented the Fibonacci calculation in both pure Python and Cython. The goal is to demonstrate how Cython's compilation into C code can lead to significant speed improvements.

Running the Experiment
----------------------

In the ``test.py`` file included in this repository, I've set up a comparison between the Python and Cython implementations of the Fibonacci calculation. By measuring the execution time of each implementation, we can quantify the performance gain achieved through Cython.

To run the experiment yourself, follow these steps:

#. Clone this repository to your local machine.

.. code-block:: bash

    git clone Cython-Tutorial

2. Navigate to the root directory of the repository.

.. code-block:: bash

    cd Cython-Tutorial

3. Activate a virtual environment, and install the dependencies.

.. code-block:: bash

    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt

3. Build the Cython module.

.. code-block:: bash

    python setup.py build_ext --inplace

4. Run the experiment.

.. code-block:: bash

    python test.py

Results
-------

After running the experiment, we observed the following results:

.. code-block :: text

    Python time for Fibonacci(30): Approximately 917.5 nanoseconds
    Cython time for Fibonacci(30): Approximately 115.4 nanoseconds

This comparison clearly shows that the Cython implementation outperforms the pure Python implementation by a significant margin. The faster execution time of the Cython implementation is a testament to Cython's ability to compile Python-like code into optimized C code.

Conclusion
----------

In conclusion, Cython offers a powerful way to combine the convenience of Python with the performance benefits of C. By writing code that leverages Cython's compilation capabilities, Python developers can achieve faster execution times for computationally intensive tasks.

This repository serves as a proof of concept, showcasing the potential speed improvements that Cython can bring to Python code. We encourage you to explore the code provided and dive deeper into the world of Cython to harness its performance benefits for your own projects.

Read More
---------

- `Cython Documentation <https://cython.readthedocs.io/en/latest/>`_
- `Cython on GitHub <https://github.com/cython/cython>`_
- `Cython on PyPI <https://pypi.org/project/Cython/>`_
- `Differences between Python and CPython (Jython, IronPython, PyPy) <https://stackoverflow.com/questions/17130975/python-vs-cpython>`_
- `Dag Sverre Seljebotn. "Fast numerical computations with Cython." Proceedings of the 8th Python in Science Conference (SciPy 2009). <https://conference.scipy.org/proceedings/scipy2009/paper_2/full_text.pdf>`_
